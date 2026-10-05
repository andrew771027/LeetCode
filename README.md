# LeetCode Practice

用 Python 練習解題，並用 pytest 與 Hypothesis 驗證結果。目前收錄 45 題：43 題 Easy、2 題 Medium，每題都有對應測試。

## 開始練習

需要 Python 3.12 以上與 Poetry。在專案根目錄執行：

```bash
poetry install
poetry run pytest -q
```

只跑一組或一題：

```bash
poetry run pytest tests/tree -q
poetry run pytest tests/array/test_lc_026_remove_duplicates_from_sorted_array.py -q
```

VS Code 的偵錯設定放在 `.vscode/launch.json`。`args` 可指定測試檔案，或使用 `檔案路徑::測試函式名稱` 選擇案例。

## 專案結構

```text
src/                 解法，依題目主體分類
  array/
  string/
  linkedlist/
  stack/
  queue/
  tree/
tests/               與 src 使用相同 Group、題號及檔名
  tree/utils/        樹的測資建構工具
  linkedlist/utils/  串列、環與交集的測資建構工具
docs/
  patterns/          依解題思路編排的教學
  testing.md         測試案例、性質與狀態機
  problem-index.md   全部題目的 source、test、筆記連結
```

例如 `src/tree/lc_094_binary_tree_inorder_traversal.py` 對應 `tests/tree/test_lc_094_binary_tree_inorder_traversal.py`。樹的走訪即使用 stack 實作，仍放在 tree；詳見 [分類規則](docs/organization.md)。

## 閱讀筆記

- [學習索引與 Pattern 介紹](docs/readme.md)：從現有題目理解常見方法。
- [題目總表](docs/problem-index.md)：按題號找解法與測試。
- [測試方法](docs/testing.md)：了解原地修改、節點身分、Hypothesis 與操作序列。
- [BST Pattern](docs/patterns/bst.md)：#530 與 #783 的相鄰差比較，對照陣列與 `previous` 解法。
- [鏈結串列 Pattern](docs/patterns/linked-list.md)：節點接線、快慢指標，以及 Medium 題目 #19、#61。

筆記描述目前執行中的解法。註解中的替代版本與待補案例會另行說明；複雜度也計入 Python 切片、暫存陣列與遞迴堆疊。
