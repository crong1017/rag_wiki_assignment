# S05｜NVIDIA 原始資料導讀

- 原文：What is Retrieval-Augmented Generation (RAG)?
- URL：https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/
- 檢查日期：2026-11-24
- 本次擷取重點：資料蒐集與清理、chunking、embedding、indexing、reranking、向量檢索

## 本次 Ingest 摘要（以自己的話整理）
檢索前需將內容擷取、分塊並建立索引；向量表徵能協助找出語意相近的內容，必要時以 reranking 調整排序。

## 匯入處理
已經將來源重點整理到 knowledge_base.json，對應 Wiki 條目可由 sources 欄位追溯。本專案只匯入經過摘要與整理的內容，並未宣稱對原始網頁全文建立向量索引。
