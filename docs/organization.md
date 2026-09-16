# Problem Group 分類規則

[回學習索引](readme.md)

每題只保留一份解法與一份測試，兩邊使用相同 Group。先依題目主要操作的結構分類；若是實作容器，依對外介面分類。Pattern 教學另外提供跨 Group 的閱讀路徑。

| Group | 收錄範圍 | 題數 |
| --- | --- | --- |
| array | 陣列搜尋、修改、數值序列 | 8 |
| string | 字串比較、解析、編碼轉換 | 10 |
| linkedlist | 串列節點與連線操作 | 10 |
| stack | 括號配對、實作 Stack | 2 |
| queue | 實作 Queue | 1 |
| tree | 二元樹、BST、N 元樹 | 13 |

## 這次調整

| 題目 | 原 Group → 新 Group | 原因 |
| --- | --- | --- |
| #14 Longest Common Prefix | array → string | 主要問題是字串共同前綴 |
| #20 Valid Parentheses | string → stack | 核心工作是巢狀配對 |
| #94、#144、#145、#589、#590 | stack → tree | 輸入與結果描述的都是樹走訪 |
| #108 Sorted Array to BST | array → tree | 目標是建構平衡 BST |
| #225 Implement Stack using Queues | queue → stack | 對外提供 Stack 行為 |
| #232 Implement Queue using Stacks | stack → queue | 對外提供 Queue 行為 |

#28 檔名的 `occurance` 改為 `occurrence`；#160 的 `interection` 改為 `intersection`。import 同步更新。原本 stack 的樹測資改用 `tests/tree/utils/helper.py`，移除重複 helper。

## 新增題目

1. 在 `src/<group>/` 新增 `lc_<三位題號>_<題名>.py`。
2. 在 `tests/<group>/` 新增 `test_` 加上相同檔名，從對應 source 匯入。
3. 補上題意、解法成立的理由、成本及測試邊界，連到適合的 Pattern 文件。
4. 更新[題目總表](problem-index.md)，執行該題測試與完整測試。

不要因為嘗試另一種演算法就搬動題目；例如 Two Sum 改成 hash map 後仍放在 array，Pattern 筆記則可以更新。
