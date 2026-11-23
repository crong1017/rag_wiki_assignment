# S03｜Google Cloud 原始資料導讀

- 原文：What is Retrieval-Augmented Generation (RAG)?
- URL：https://cloud.google.com/use-cases/retrieval-augmented-generation
- 檢查日期：2026-11-24
- 本次擷取重點：外部知識接地（grounding）、應用場景、品質評估與改進

## 本次 Ingest 摘要（以自己的話整理）
RAG 用於讓生成式 AI 存取新、私有或專業領域資料；可透過 groundedness 與檢索品質等指標逐步評估及改善。

## 匯入處理
已經將來源重點整理到 knowledge_base.json，對應 Wiki 條目可由 sources 欄位追溯。本專案只匯入經過摘要與整理的內容，並未宣稱對原始網頁全文建立向量索引。
