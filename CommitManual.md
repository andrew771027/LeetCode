# Commit 與文件更新指南

## 文件更新規則

更新前先閱讀本次 source、test 的變更與[分類規則](docs/organization.md)，再調整相關文件。

- **以實作為準：** 描述目前執行的解法與現有測試。註解中的替代解法、尚未加入的測試與優化想法，標為「延伸建議」。
- **每題內容：** 包含題意與輸入前提、推理過程、解法步驟、時間與空間複雜度、測試方法及邊界案例，並連結 source 與 test。需要追蹤指標、樹形或狀態變化時，補上 Mermaid 或文字圖解。
- **依 Pattern 編排：** 更新 `docs/patterns/` 對應主題，說明為何適用此方法。Problem Group 遵循分類規則，source 與 test 保持一致。
- **同步維護入口：** 更新[題目索引](docs/problem-index.md)、[學習索引](docs/readme.md)及 [README](README.md) 的相關連結、題數與說明。測試方法有變更時，也更新[測試教學](docs/testing.md)。
- **寫作方式：** 使用自然、簡潔的繁體中文，先講重點，再用具體例子解釋。避免口號、制式套話、重複摘要與無助理解的術語。
- **確認正確性：** 檢查文件連結與程式、測試是否一致；複雜度計入切片、暫存資料及遞迴堆疊。驗證結果只記錄實際執行的檢查，不沿用舊數字。

下次可直接使用：

> 請依照 CommitManual.md，根據本次 source 與 test 的變更更新 docs、相關索引與 README，並提供 commit 訊息。

## Commit 訊息

```text
<type>(<scope>): <修改摘要>

修改原因與主要變化；必要時附上實際驗證結果。
```

Type 使用 `feat`（新增）、`fix`（修正）、`refactor`（重構）、`test`（測試）、`docs`（文件）或 `chore`（設定）。Scope 使用 Group 或主題，例如 `tree`、`patterns`。

範例：`docs(patterns): 補上雙指標題目的推理與測試說明`。

## 提交前檢查

1. 檢查 `git diff`，只暫存本次要提交的檔案；搬移與 import 更新一起提交。
2. 程式或測試有變更時，執行 `poetry run pytest -q`；僅修改文件時，檢查內容與連結。
3. 執行 `git diff --cached --check` 並檢閱暫存差異，再用 `git commit` 提交。
