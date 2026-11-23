# AGENTS.md｜RAG Wiki × 教學 HTML 簡報

## 代理任務
將五份可信的公開資料整理為可回查的教學知識庫，並在此基礎上維護 HTML 簡報。讀者是從未接觸過 RAG 的大學生。

## 使用資料的優先順序
1. 以 `data/knowledge_base.json` 內的 `entries` 為教學內容的唯一正式知識來源。
2. 每個條目必須保留其 `sources` 所連結的來源 ID（S01–S05）。
3. 需要擴充內容時，先更新 `sources/Sxx_*.md` 的摘要與對應知識卡；不得直接從模型記憶填進 HTML。
4. 外部原始文章放在 `knowledge_base.json` 的 `sources`；文字採自己的整理與改寫，避免複製整篇文章。

## 生成與維護規則
- 先提教學大綱，再產生頁面；遵守「動機 → 核心概念 → 技術 → 流程 → 案例 → 限制 → 測驗」。
- 每張投影片都必須有正確的 `data-wiki` 與 `data-sources`，以及可供使用者點擊的對應來源。
- 必須明確區分「教學範例」和真實規範，不得杜撰學校、醫院或企業的實際規定。
- 保留 22 頁簡報上下頁、方向鍵、快速跳頁、頁碼、情境互動與三題測驗回饋；不得為美觀而移除必要功能。
- 禁止聲稱已部署 RAG LLM 問答 API、向量資料庫或 GitHub Pages；只有經查證的實際成果才可聲稱完成。

## 驗證規則 / Loop
- Gate A（生成 HTML 前）：執行 `python tests/validate.py`，確認來源數至少五個、Wiki 與來源 ID 合法。
- Gate B（生成 HTML 後）：確認簡報頁面 ID 映射合法，執行 `python tests/browser_check.py`，確認按鈕、方向鍵（特別是按鈕焦點後）、快速跳頁、互動情境、三題測驗與手機版正常。
- Gate A 未過：回到 source ingest 與 Wiki 條目整理。
- Gate B 內容來源未過：回到大綱與投影片生成；介面未過：回到 HTML/CSS/JS 修正。
- 修正後重新執行所有相關測試，更新 `TEST_LOG.md`，保留錯誤與修正紀錄。

## 專案架構
- `index.html`：入口
- `wiki.html`：Wiki 瀏覽頁
- `slides.html`：教學 HTML 簡報
- `workflow.html`：流程圖與迴圈解釋
- `wiki/`、`sources/`、`data/`：知識內容與來源
- `assets/`：CSS、JS、流程圖
- `tests/`：實際驗證工具與測試輸出

## 发布前核對
必須實際取得 GitHub Pages 網址，並用網站公開網址檢查圖片、樣式、腳本及 Wiki 連結，才能將「已部署」標示為完成。
