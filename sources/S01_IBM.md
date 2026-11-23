# S01｜IBM 原始資料導讀

- 原文：What is RAG (Retrieval Augmented Generation)?
- URL：https://www.ibm.com/think/topics/retrieval-augmented-generation
- 檢查日期：2026-11-24
- 本次擷取重點：RAG 核心概念、retriever / generator / integration layer、chunking 與 embedding、微調比較

## 本次 Ingest 摘要（以自己的話整理）
RAG 由外部知識庫擷取相關內容，將其加入提示，再由語言模型生成回應；知識庫、檢索器與生成器彼此分工。

## 匯入處理
已經將來源重點整理到 knowledge_base.json，對應 Wiki 條目可由 sources 欄位追溯。本專案只匯入經過摘要與整理的內容，並未宣稱對原始網頁全文建立向量索引。
