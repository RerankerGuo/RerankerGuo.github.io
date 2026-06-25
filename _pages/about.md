---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

郭子扬，东南大学（SEU）软件工程专业硕士研究生一年级，导师为[金嘉晖](https://jujuhoo.github.io/)。本科毕业于河海大学（2025年），曾于百度担任大模型算法实习生。 

# 🔍Topics
- ChatBot 
- Agent-Memory     
- Healthcare Intelligence
- AI-Assisted Software Engineering

# 🔥 News
- 2026/5-[主讲东南大学黑客松workshop2](https://www.xiaohongshu.com/discovery/item/69fd7b3b00000000350335fe?source=webshare&xhsshare=pc_web&xsec_token=AB1lJekvt7r-6ERoXNSriwyhGzwulPVNI-xqenuwiI8ME=&xsec_source=pc_share):为大家讲解如何和ai同频共振，以便更好地AI Coding、AI Working
- 2026/4-[东南大学校花校草](https://mp.weixin.qq.com/s/VC-TzLqVNIvsVyMB-r2biw):愚人节看个开心～
- 2026/3-[成为真正的AI Native Coder](https://mp.weixin.qq.com/s/xLgonEJ9cCH0LaLpw76_3g):基于个人开发经历，沉淀AI Codind方法论，阅读2万转发3千
- 2025/12-[优化大模型应用的三个阶段：prompt->sft->rl](https://www.zhihu.com/question/498271491/answer/1978925310432010693):如何判断是自己prompt写的不够好 OR 基座模型的能力不够，才让大模型应用达不到预期效果？这个问题直接决定了后续的技术路径——是继续调prompt、引入RAG还是投入大量成本去做SFT、RL。
- 2025/10-[关于AI Agent设计理念的深度思考](https://mp.weixin.qq.com/s/3DGLUjQ_KP5heVbf3PTTZA):基于ChatBot、DeepResearch相关业务实习经历，总结Agent设计理念，阅读2万转发3千，获字节DeerFlow团队致敬认可
- 2025/9-[25年大模型应用方向：Text2SQL](https://zhuanlan.zhihu.com/p/1915001536171476928):随着模型底座能力与企业数据治理的持续进化，Text2SQL 不再只是问数据库，而是成为驱动业务流程的核心入口，让用户在一次对话中完成检索、决策与执行的全链路操作。我们有望从移动互联网迈向对话互联网


# 🚀 Projects

<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">GitHub</div>
<img src='../images/deepmemo-editor.png' alt="DeepMemo screenshot" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[DeepMemo](https://github.com/YeyezhizzZ/deepmemo)

![GitHub stars](https://img.shields.io/github/stars/YeyezhizzZ/deepmemo?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/YeyezhizzZ/deepmemo?style=flat-square)

- 本地优先的 Markdown 知识库创作与问答工作台，旨在构建可编辑、可检索、可追溯的个人知识系统，适合长期沉淀学习记录、工程经验和科研进度。

</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">GitHub</div>
<img src='../images/awesome-ai-memory.png' alt="Awesome-AI-Memory cover" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)

![GitHub stars](https://img.shields.io/github/stars/IAAR-Shanghai/Awesome-AI-Memory?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/IAAR-Shanghai/Awesome-AI-Memory?style=flat-square)

- 面向Agent Memory的持续更新知识库，系统整理记忆系统设计、研究论文、开源框架、基准与实践，当前已积累了 400+ 论文和 100+ 开源项目。个人认为memory是agent时代的数字基建，十分欢迎同行交流～

</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">GitHub</div>
<img src='../images/tencentdb-agent-memory.png' alt="TencentDB Agent Memory logo" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

![GitHub stars](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/TencentCloud/TencentDB-Agent-Memory?style=flat-square)

- 腾讯云开源的 Agent 记忆引擎，主打"符号化短期记忆 + 分层长期记忆"：将冗长的工具日志压缩为 Mermaid 符号图腾，长期记忆按 L0 Conversation → L1 Atom → L2 Scenario → L3 Persona 分层沉淀。集成 OpenClaw / Hermes 后，token 用量最多下降 61.38%，SWE-bench pass rate 相对提升 9.93%。 **Contributor (PR merged)** — 参与了核心代码贡献。

</div>
</div>

---

# 🏆 Competitions
- 2024, 中国大学生计算机设计大赛全国二等奖
- 2024, 中国大学生服务外包创新创业大赛三等奖

# 🎖 Honors and Awards
- 2024.11, 河海大学十佳班长（24年全校唯十）
- 2024.10, 河海大学严恺奖学金（24年全学院唯一）
- 2024.05, 江苏省先进班集体
- 2023.10, 本科生国家奖学金 
- 2021-2025, 河海大学优秀学生奖学金
