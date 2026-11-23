# Workflow / Graph 與 loop 規則

## 節點
A. 討論主題、決定章節 → B. 取得 5 篇權威文章 → C. ingest（整理各篇來源摘要與來源 ID） → D. 建立 Wiki 條目 → E. 檢查 Wiki 來源完整性 → F. 產生教學大綱 → G. 依 Wiki 知識卡製作 HTML 投影片 → H. 檢查每頁的 Wiki/來源對應與 HTML 操作 → I. 發布與存證。

## 分支與迴圈
- E 不通過（少了來源、資料敘述無足夠依據）：返回 B/C/D，補資料與改寫，再做 E。
- H 的來源對應不通過：返回 F/G，依原 Wiki 改寫簡報，重新驗證。
- H 的網頁互動不通過：返回 G 修正 JavaScript/CSS，再做 H。
- E 與 H 都通過：才能進入 I。

## 檢查前移
原本若僅在投影片完成時檢查，無法追蹤錯誤從何而來。現在在產生任何 HTML 前就先執行 E（來源至少五個、每個 Wiki 條目有合法 source ID），並在 G 前就確認大綱的 Wiki ID 存在。這能避免生成後回頭大改。

## 可重現的實際執行
執行 `python tests/validate.py`；檢查 knowledge_base.json 的 source/Wiki/slides 映射、Markdown 檔案與 HTML 標記。接著以 `python tests/browser_check.py` 進行實際 Chromium 操作測試。`TEST_LOG.md` 記錄實測輸出。


## 2026-11-24 補充迭代：簡報擴充後提早進行互動檢查
- 初版 9 頁；根據教學完整性需求擴充為 22 頁。
- 前端事件測試首次發現：點擊下一頁後焦點停留按鈕，ArrowRight 未執行。
- 故在「G 生成 HTML」後即加跑快速鍵盤導航冒煙測試；失敗直接退回 G 修改 JS，而不必等所有頁面製作完成。
- 修正後完整測試通過，保留原失敗紀錄與修改說明。
