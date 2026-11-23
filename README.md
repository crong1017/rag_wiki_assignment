# RAG LLM Wiki × 教學 HTML 簡報

## 瀏覽方式
- `index.html`：專案首頁，連到 Wiki、簡報與 Workflow。
- `wiki.html`：可搜尋的 7 個知識條目，含 5 個來源 ID 與原文連結。
- `slides.html`：22 頁 HTML 教學簡報，包含循序課程、兩情境互動、三題測驗、快速跳頁及來源連結。
- `workflow.html`：Loop / Graph 設計與分支。
- `data/knowledge_base.json`：來源、條目、投影片關聯資料；`wiki/` 與 `sources/` 保留 Markdown 版本。
- `tests/`：資料驗證與瀏覽器測試紀錄。

## 課程要求對應
1. 先討論、後生成：參見 `DESIGN_DECISIONS.md`。
2. Ingest 至少五篇：5 份 `sources/` 導讀筆記；資料編號 S01–S05。
3. 以 Wiki 生成簡報：`knowledge_base.json` 裡每頁 slides 有 `wiki` 連結，可追溯到 W01–W07 條目。
4. Loop / Graph：`workflow.html`，以及 `WORKFLOW.md`。
5. 驗證與反思：`tests/test_report.json`、`TEST_LOG.md`。

## 注意
這份作業示範的是**經整理的 LLM Wiki 與以 Wiki 為依據的教學內容生成工作流**。站內搜尋為前端關鍵詞查詢，不是部署中的 LLM/RAG 回答服務，不應宣稱已建成向量資料庫。公開 GitHub Pages 連結需實際將專案上傳儲存庫並啟用 Pages 後填入 Word。
