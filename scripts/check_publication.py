"""Structural publication checks. These never approve research or translations."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"research", "note", "protocol", "playful"}
LABELS = {
    "research": ("深度研究", "Research"),
    "note": ("研究短札", "Research note"),
    "protocol": ("研究方案", "Protocol"),
    "playful": ("趣味论文", "Playful essay"),
}
REQUIRED = {
    "paper.json", "zh.qmd", "en.qmd", "references.bib", "evidence.csv",
    "glossary.csv", "CHANGELOG.md", "reproduce.md", "review.json",
}
CHECKS = {"content", "sources", "bilingual", "multilingual", "web_desktop_mobile", "pdf_zh_en", "pdf_all_languages", "public_scope"}
# Match explicit editorial markers, not ordinary Spanish/Portuguese words such as "todo".
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b")


def fingerprints(folder: Path) -> dict[str, str]:
    result = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symbolic link not allowed: {path.name}")
        if path.is_file() and path.name != "review.json":
            path.resolve().relative_to(folder.resolve())
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"Missing front matter: {path.name}")
    return yaml.safe_load(match[1]) or {}, match[2]


def valid_date(value: object) -> bool:
    try:
        dt.date.fromisoformat(str(value))
        return True
    except (TypeError, ValueError):
        return False


def check_article(folder: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    missing = REQUIRED - {p.name for p in folder.iterdir() if p.is_file()}
    if missing:
        return {}, [f"Missing files: {', '.join(sorted(missing))}"]
    meta = json.loads((folder / "paper.json").read_text(encoding="utf-8-sig"))
    review = json.loads((folder / "review.json").read_text(encoding="utf-8-sig"))
    if meta.get("schema_version") != 1:
        errors.append("Unsupported schema_version")
    if not re.fullmatch(r"\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*", folder.name) or meta.get("paper_id") != folder.name:
        errors.append("paper_id must match a YYYYMMDD-slug directory")
    if meta.get("type") not in KINDS:
        errors.append("Unknown article type")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(meta.get("version", ""))):
        errors.append("version must use major.minor.patch")
    if meta.get("status") != "ready":
        errors.append("Only ready packages belong in the public articles directory")
    if meta.get("original_language") not in {"zh-CN", "en"}:
        errors.append("Specify a single original_language")
    if not valid_date(meta.get("date")):
        errors.append("Missing or invalid article date")
    authors = meta.get("authors", [])
    if not isinstance(authors, list) or not authors or not all(isinstance(x, str) and x.strip() for x in authors):
        errors.append("Real confirmed author names are required")
    if not isinstance(meta.get("license"), str) or not meta["license"].strip():
        errors.append("A permissions/license statement is required")
    peer = meta.get("peer_review")
    if peer not in {"not-peer-reviewed", "internally-reviewed", "externally-peer-reviewed"}:
        errors.append("Specify truthful peer_review status")
    if peer == "externally-peer-reviewed" and not str(meta.get("peer_review_url", "")).startswith("https://"):
        errors.append("External peer review requires a supporting record URL")
    for key, value in fingerprints(folder).items():
        path = Path(key)
        if path.name.startswith(".env") or path.suffix.lower() in {".pem", ".key", ".pfx"} or "__pycache__" in path.parts:
            errors.append(f"Unexpected private/cache material: {key}")
    if PLACEHOLDER.search(json.dumps(meta, ensure_ascii=False)):
        errors.append("Metadata still contains placeholders")
    bib = (folder / "references.bib").read_text(encoding="utf-8-sig")
    bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
    structures = []
    citation_sets = []
    languages=json.loads((ROOT/'survey/languages.json').read_text(encoding='utf-8'))
    for entry in languages:
        language=entry['code'];filename=('zh' if language=='zh-CN' else language)+'.qmd';counterpart='en.qmd' if language=='zh-CN' else 'zh.qmd'
        front, body = frontmatter(folder / filename)
        if meta.get("language_status", {}).get(language) != "reviewed":
            errors.append(f"Full {language} manuscript has not been reviewed")
        expected = {"lang": language, "paper-id": folder.name, "paper-version": meta.get("version"), "article-type": meta.get("type"), "title": meta.get("title", {}).get(language)}
        for key, value in expected.items():
            if not value or front.get(key) != value:
                errors.append(f"{filename}: {key} does not match article metadata")
        if str(front.get("date")) != str(meta.get("date")) or front.get("author") != authors:
            errors.append(f"{filename}: date/authors do not match")
        if not front.get("abstract"):
            errors.append(f"{filename}: abstract is required")
        if PLACEHOLDER.search(body + json.dumps(front, default=str, ensure_ascii=False)):
            errors.append(f"{filename}: unresolved placeholders")
        if len(re.sub(r"\s", "", body)) < 300:
            errors.append(f"{filename}: too little text for a full manuscript; inspect completeness")
        if f"]({counterpart})" not in body:
            errors.append(f"{filename}: missing same-article language link")
        if f"]({Path(filename).stem}.pdf)" not in body:
            errors.append(f"{filename}: missing PDF link")
        anchors = re.findall(r"^##\s+.+?\{#([a-z0-9-]+)\}\s*$", body, re.M)
        if len(anchors) != len(set(anchors)):
            errors.append(f"{filename}: repeated section anchors")
        if not {"limitations", "availability", "ai-use"}.issubset(set(anchors)):
            errors.append(f"{filename}: limitations, materials and AI disclosure sections are required")
        structures.append(anchors)
        keys = {key for key in re.findall(r"(?<!\w)@([A-Za-z][\w:.-]*)", body) if not key.startswith(("fig-", "tbl-", "eq-", "sec-", "lst-"))}
        if keys - bib_keys:
            errors.append(f"{filename}: unknown bibliography keys: {sorted(keys - bib_keys)}")
        citation_sets.append(keys)
        if meta.get("type") == "playful":
            if not re.search("趣味|戏仿|虚构" if language == "zh-CN" else "playful|satire|fiction", str(front.get("subtitle", "")), re.I):
                errors.append(f"{filename}: playful identity must be visible in the subtitle")
    if any(s!=structures[0] for s in structures[1:]):
        errors.append("Localized semantic section anchors/order differ")
    if any(s!=citation_sets[0] for s in citation_sets[1:]):
        errors.append("Localized citation keys differ")
    for filename in ("CHANGELOG.md", "reproduce.md"):
        if PLACEHOLDER.search((folder / filename).read_text(encoding="utf-8-sig")):
            errors.append(f"{filename}: unresolved placeholders")
    with (folder / "evidence.csv").open(encoding="utf-8-sig", newline="") as stream:
        evidence = list(csv.DictReader(stream))
    if not evidence:
        errors.append("Evidence/source record is empty; document the article's actual evidence or creative status")
    if not review.get("reviewer") or PLACEHOLDER.search(str(review.get("reviewer"))):
        errors.append("A real reviewer/checker's name is required")
    if not valid_date(review.get("reviewed_on")):
        errors.append("Missing or invalid review date")
    if any(review.get("checks", {}).get(key) is not True for key in CHECKS):
        errors.append("Actual content, sources, bilingual, web, PDF and public-scope checks are required")
    if review.get("files_sha256") != fingerprints(folder):
        errors.append("Review fingerprints are incomplete or stale; recheck the changed materials")
    return meta, errors


def check_all(root: Path = ROOT, release: bool = False) -> tuple[list[dict], list[str]]:
    items, errors = [], []
    for folder in sorted((root / "protocol").iterdir()):
        if not folder.is_dir():
            continue
        try:
            if folder.is_symlink():
                raise ValueError("Article directories cannot be symbolic links")
            meta, article_errors = check_article(folder)
            errors.extend(f"{folder.name}: {e}" for e in article_errors)
            if not article_errors:
                items.append(meta)
        except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
            errors.append(f"{folder.name}: {exc}")
    if release:
        config = yaml.safe_load((root / "_quarto.yml").read_text(encoding="utf-8-sig"))
        website = config.get("website", {})
        if not re.fullmatch(r"https://[^\s]+", str(website.get("site-url", ""))):
            errors.append("Set the real website.site-url before deployment")
        if not re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+/?", str(website.get("repo-url", ""))):
            errors.append("Set the real website.repo-url before deployment")
    return items, errors


def write_catalogues(items: list[dict], root: Path = ROOT) -> None:
    for language, index, prefix in (("zh", 0, "protocol/"), ("en", 1, "../protocol/")):
        if not items:
            text = "尚无已验收并发布的文章。版式样张不计入文章目录。\n" if language == "zh" else "No reviewed articles have been released yet. Layout examples are not included in the article catalogue.\n"
        else:
            text = "| 日期 | 文章 | 类型 | 版本 |\n| --- | --- | --- | --- |\n" if language == "zh" else "| Date | Article | Type | Version |\n| --- | --- | --- | --- |\n"
            for item in sorted(items, key=lambda x: (x["date"], x["paper_id"]), reverse=True):
                title = item["title"]["zh-CN" if language == "zh" else "en"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
                text += f'| {item["date"]} | [{title}]({prefix}{item["paper_id"]}/{language}.qmd) | {LABELS[item["type"]][index]} | {item["version"]} |\n'
        (root / f"_catalog.{language}.md").write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--fingerprints", metavar="PAPER_ID")
    args = parser.parse_args()
    if args.fingerprints:
        folder = (ROOT / "protocol" / args.fingerprints).resolve()
        folder.relative_to((ROOT / "protocol").resolve())
        if not folder.is_dir() or folder == (ROOT / "protocol").resolve():
            parser.error("Specify one existing article directory")
        print(json.dumps(fingerprints(folder), ensure_ascii=False, indent=2))
        return 0
    items, errors = check_all(release=args.release)
    if errors:
        print("PUBLICATION CHECK FAILED\n" + "\n".join(f"- {e}" for e in errors))
        return 1
    print(f"Structural checks passed: {len(items)} article(s). Scientific and bilingual judgments require actual review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
