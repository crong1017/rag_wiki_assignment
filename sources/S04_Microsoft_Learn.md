# S04｜Microsoft Learn 原始資料導讀

- 原文：Retrieval augmented generation (RAG) and indexes in Microsoft Foundry
- URL：https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation
- 檢查日期：2026-11-24
- 本次擷取重點：Retrieve → Augment → Generate、索引、keyword / vector / hybrid 檢索、引用

## 本次 Ingest 摘要（以自己的話整理）
典型 RAG 包含檢索、增補、生成三步；索引可使用關鍵字、向量或混合式檢索，並保存文件標題與來源網址協助引用。

## 匯入處理
已經將來源重點整理到 knowledge_base.json，對應 Wiki 條目可由 sources 欄位追溯。本專案只匯入經過摘要與整理的內容，並未宣稱對原始網頁全文建立向量索引。
