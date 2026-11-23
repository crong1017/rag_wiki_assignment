# 作業需求摘要與可驗收成果

| 必要要求 | 對應成果 | 驗收方式 |
|---|---|---|
| 先討論後生成 | DESIGN_DECISIONS.md | 有決策與教學規格，不是一次生成 |
| 建立自訂 LLM Wiki | wiki.html、wiki/、data/knowledge_base.json | 7 張可查詢知識卡 |
| 至少 ingest 5 篇 | sources/S01–S05、data/knowledge_base.json | 5 筆有 URL 的來源記錄 |
| HTML 教學簡報 | slides.html | 22 張、可操作、互動案例與三題測驗 |
| 根據 Wiki 製作 | slides.html 每頁的 data-wiki、data-sources | 可追溯到 Wxx / Sxx |
| loop / graph | workflow.html、assets/workflow.png | A/B 兩個有退回路徑的 loop |
| 實際執行與檢查 | TEST_LOG.md、tests/test_report.json | 結構測試與 Chromium 互動測試 |
| 反思及改進 | TEST_LOG.md、Word 第 5 頁 | 有真實限制、故障注入與檢查前移 |
| Word 繳交 | 另附 RAG_LLM_Wiki_課堂作業報告.docx | 六頁完整報告 |
| 公開 Wiki 與 HTML 連結 | 尚待 GitHub Pages 部署 | 部署後填入 Word；不得以假網址替代 |
