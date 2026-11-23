# S02｜AWS 原始資料導讀

- 原文：What is RAG (Retrieval-Augmented Generation)?
- URL：https://aws.amazon.com/what-is/retrieval-augmented-generation/
- 檢查日期：2026-11-24
- 本次擷取重點：一般 LLM 限制、RAG 目的、企業知識庫、semantic search

## 本次 Ingest 摘要（以自己的話整理）
RAG 不必重新訓練原模型，就能在生成回答前引用權威資料；可緩解過時、缺乏領域知識等問題，但不保證零錯誤。

## 匯入處理
已經將來源重點整理到 knowledge_base.json，對應 Wiki 條目可由 sources 欄位追溯。本專案只匯入經過摘要與整理的內容，並未宣稱對原始網頁全文建立向量索引。
