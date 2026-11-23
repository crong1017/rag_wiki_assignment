<div align="center">

# ✦ RAG Learning Lab

### 讓 AI 先查找資料，再產生有根據的回答

從 **5 篇技術資料** 出發，建立 **7 個主題知識條目**，
再將知識整理成 **22 頁互動式 HTML 教學簡報**。

**LLM Wiki × RAG 基礎教學 × 可追溯的內容生成流程**

</div>

---

## 🌱 專案介紹

當我們向大型語言模型提問時，回答不一定附有可靠的依據。這個專案以 **RAG（Retrieval-Augmented Generation，檢索增強生成）** 為主題，帶領初學者了解：如何先從知識庫找到相關資訊，再讓 AI 根據資料組織回答。

我把蒐集到的公開技術文章整理為 LLM Wiki，並以 Wiki 作為教學簡報的內容依據。除了介紹技術概念，也設計了來源檢查、內容修正與互動測試的流程，讓整個作品不只是「生成完成」，而是能夠被追溯、檢查與改善。

## 📚 你可以學到什麼？

- **RAG 為什麼重要**：了解 LLM 的知識限制，以及檢索能解決哪些問題。
- **資料如何變成知識庫**：認識 Ingest、Chunking、Embedding 與索引。
- **AI 如何找到相關資訊**：理解語意檢索、混合檢索與參考資料的使用。
- **從檢索到生成**：看懂 RAG 的完整處理流程與常見錯誤。
- **如何評估結果**：透過案例與互動題目，練習判斷回答是否有足夠證據。

## ✨ 作品內容

| 教學資源 | 內容亮點 |
| --- | --- |
| 📖 **LLM Wiki** | 7 個主題知識條目、關鍵字查詢、對應資料來源 |
| 🖥️ **HTML 教學簡報** | 22 頁循序教學、圖像化流程、情境練習、3 題小測驗 |
| 🔁 **Workflow / Graph** | 呈現資料取得、知識整理、來源檢查、生成與重試的關係 |
| 🧪 **驗證紀錄** | 資料來源對應檢查、操作測試、發現問題後的調整與反思 |

### 專案頁面

- [網站首頁（HTML 原始檔）](index.html)
- [RAG 知識 Wiki（HTML 原始檔）](wiki.html)
- [22 頁教學簡報（HTML 原始檔）](slides.html)
- [Loop / Graph 流程說明（HTML 原始檔）](workflow.html)

> **瀏覽提醒：** GitHub 的檔案頁面是程式碼預覽，不等於可操作的網站。需要把完整專案（含 `assets/`、`data/` 等資料夾）部署至 GitHub Pages，才能透過網址正常瀏覽。

## 🧩 Wiki 與簡報如何連結？

這份教學內容不是憑空寫成：每個 Wiki 條目都有參考來源編號，簡報也標示對應的 Wiki 主題，方便回頭查證。

**5 篇參考資料（S01–S05） → 7 個 Wiki 條目（W01–W07） → 22 頁教學簡報（P01–P22）**

主要參考：[IBM](https://www.ibm.com/think/topics/retrieval-augmented-generation) · [AWS](https://aws.amazon.com/what-is/retrieval-augmented-generation/) · [Google Cloud](https://cloud.google.com/use-cases/retrieval-augmented-generation) · [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation) · [NVIDIA](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/)。

## 🔄 Workflow：從知識到教學內容

**資料蒐集 → 整理與匯入 → 建立 Wiki → 驗證來源 → 規劃教學大綱 → 生成 HTML → 測試與發布**

流程中有兩個重要的回饋迴圈：

1. **知識檢查 Loop**：若 Wiki 缺少依據或來源編號不一致，就返回資料整理步驟補充或修正。
2. **簡報檢查 Loop**：若投影片敘述與 Wiki 不符，便重新整理該頁；若操作按鈕或鍵盤導覽失效，則回到 HTML／JavaScript 修正並再次測試。

這樣可以在錯誤進入後續生成階段之前先攔截問題，減少整份簡報反覆重做的成本。

## 🛠️ 實作與檢查

技術使用 **HTML、CSS、JavaScript、Markdown 與 JSON**，並以自動化資料對應檢查及瀏覽器互動測試驗證作品。

在擴充教學簡報時，曾發現「點擊換頁按鈕後，方向鍵無法繼續換頁」的問題。修正鍵盤事件處理後重新執行測試，並把「換頁後立即測試鍵盤」加入後續檢查流程。詳細過程見 [測試紀錄](TEST_LOG.md) 與 [Workflow 設計](WORKFLOW.md)。

<details>
<summary><strong>查看專案文件與技術細節</strong></summary>

- [設計決策](DESIGN_DECISIONS.md)：記錄主題、範圍與「先討論、後生成」的設計思路。
- [Workflow 規則](WORKFLOW.md)：說明各節點與條件分支。
- [檢查與修正紀錄](TEST_LOG.md)：保留測試結果、錯誤與處理方式。
- [AI 協作規範](AGENTS.md)：定義資料引用、產出與驗證原則。

</details>

