# MBTI 与 AI 使用行为开放研究

[English](README.en.md) · [研究网站](https://lawyer112.github.io/mbti-ai-open-study/) · [填写问卷](https://lawyer112.github.io/mbti-ai-open-study/survey/index.html)

**类型：研究方案｜阶段：试填｜方案版本：0.3.0｜中文问卷：v0.2｜未经外部同行评审。** 本版本不报告真人样本结果，也不预定哪种人格最适合 AI。

研究问题：自报的 MBTI 类型或偏好标签，是否与 AI 使用中的提问、交互、核验、采用及体验有关？正式阶段以外部核验为主要探索指标，其余过程分别分析。客观工作绩效与 AI 增益需要后续统一任务研究。

## 参与

1. 选最近30天内最近一次已结束或暂停的真实 AI 任务；首轮面向18岁及以上、能够理解中文问卷的使用者。
2. 打开[问卷网页](https://lawyer112.github.io/mbti-ai-open-study/survey/index.html)，选择题版与文字版任选其一。也可下载[survey/index.html](survey/index.html)后在浏览器离线填写。
3. 检查后导出 JSON 与 Markdown，提交到[个人问卷回传 Issue](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=01-individual-report.yml)，或通过 PR 上传。

页面不自动上传答案。公开投稿关联 GitHub 账号，研究代号不等于匿名；请先移除私人和机密内容。参见[参与与贡献规则](CONTRIBUTING.md)。未核验、失败或未完成均可如实报告。两版补填同一次任务时沿用同一报告编号，不重复计人或计任务。

选择题版有28道过程与体验题、共49个题项；文字版有13道开放问题、共34个题项，含共同背景、可选与条件题。首轮20至30人用于改进问卷，不保证能够比较16类型。当前没有经过验证的英文问卷，英文全文是研究方案与参与说明。

## 阅读与协作

- [中文研究方案](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/zh.html) · [中文PDF](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/zh.pdf)
- [English protocol](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/en.html) · [English PDF](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/en.pdf)
- [选择题全文及目的](survey/choice-questionnaire.md) · [文字题全文及目的](survey/text-questionnaire.md)
- [操作与设计说明](QUESTIONNAIRE_DESIGN.md) · [数据规则](data/README.md)
- [提交独立调研](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=02-study-report.yml) · [讨论研究设计](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=03-research-discussion.yml)

项目署名为lawyer112。Codex辅助起草、翻译、实现和检查；未声称完成独立或外部同行评审。材料使用范围见[PERMISSIONS.md](PERMISSIONS.md)，不对参与者记录作整体再授权。

## 构建与验收

使用Python 3.12或更新版本、Quarto 1.10.19及中文字体，安装requirements.txt后运行 `python scripts/build_site.py`。网页与两个PDF从同一组中英源稿生成。详情见[复现说明](protocol/20261026-mbti-ai-use-protocol/reproduce.md)和[核验记录](VERIFICATION.md)。检查工作流不部署；Pages发布只通过手动工作流触发。
