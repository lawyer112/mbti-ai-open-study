# 复现与构建 / Reproduction and build

本方案尚无真人样本统计，没有可复算的经验结果或功效计算。49题、34题及所有题号来自scripts/questionnaire_items.py，使用构建脚本生成。TEST_ONLY材料是界面检查夹具，不是研究数据，不随首发包公开。

在仓库根目录使用Python 3.12或更新版本、Quarto 1.10.19、PyYAML 6.0.3和可用中文字体：

```text
python -m pip install -r requirements.txt
python scripts/build_questionnaires.py
python scripts/check_publication.py --release
python scripts/build_site.py
```

本地Quarto不在PATH时，设置QUARTO_BIN指向其入口。Linux构建使用Noto Sans CJK SC与Liberation Sans；Windows使用Noto Sans SC与Arial。输出为_site/中的双语网页、两个PDF和独立HTML问卷。--preview仅用于验收前排版检查，不允许据此发布；正式构建核验review.json和instrument-lock.json。

查看问卷后，使用明确标记的测试内容检查必答项、条件题、互斥选项、草稿恢复和两版导出。发布前还需检查桌面、手机、PDF逐页内容及公开范围。题库、引用、文稿或关键实现变化后重新核验，不能自动更新指纹掩盖变化。

This protocol has no human-participant statistics, empirical results to reproduce, or completed power calculation. The counts of 49 and 34 items and all item IDs come from scripts/questionnaire_items.py and its generator. TEST_ONLY materials are interface fixtures, not research data, and are excluded from the first public package.

Run the commands above from the repository root with Python 3.12 or later, Quarto 1.10.19, PyYAML 6.0.3, and Chinese fonts. Set QUARTO_BIN if Quarto is not on PATH. Linux uses Noto Sans CJK SC and Liberation Sans; Windows uses Noto Sans SC and Arial. The _site/ output contains bilingual HTML, both PDFs, and the standalone questionnaire. --preview is only for layout inspection before review; release builds require the review record and instrument lock.

Use explicitly marked test content to check required items, conditional questions, mutually exclusive answers, draft restoration, and both form exports. Review desktop/mobile pages, each PDF page, and public scope before release. Recheck after substantive source or implementation changes; do not automatically replace hashes to hide unreviewed changes.
