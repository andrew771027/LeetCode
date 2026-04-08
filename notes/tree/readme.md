# Tree Traversal 樹的遍歷

樹的遍歷主要分為 深度優先搜尋 (DFS) 與 廣度優先搜尋 (BFS) 兩大類。
---
1. Preorder Traversal (前序遍歷)

    順序：中 $\rightarrow$ 左 $\rightarrow$ 右

    - 行為描述： 先拜訪根節點，再拜訪左子樹，最後拜訪右子樹。

    - Stack 實作邏輯：

        1. 將根節點放入 Stack。

        1. 當 Stack 不為空時：

            - 取出頂端節點（中）。

            - 先將右子節點推入 Stack，再將左子節點推入 Stack（因為 Stack 是後進先出，這樣左節點才會先被處理）。


---

1. Inorder Traversal (中序遍歷)

    順序：左 $\rightarrow$ 中 $\rightarrow$ 右

    - 行為描述： 先完整走完左子樹，再拜訪根節點，最後走右子樹。在 二元搜尋樹 (BST) 中，中序遍歷的結果會是由小到大的排序。

    - Stack 實作邏輯：
        1. 設定一指標指向根節點。

        1. 當指標不為空或 Stack 不為空時：

            - 持續將當前節點及其所有左子節點推入 Stack，直到指標為空。從 Stack 彈出節點（中），進行拜訪。

            - 將指標移向該節點的右子節點。

---

1. Postorder Traversal (後序遍歷)

    順序：左 $\rightarrow$ 右 $\rightarrow$ 中

    - 行為描述： 先走完左右子樹，最後才拜訪根節點。常用於「刪除整棵樹」或「計算目錄大小」。

    - Stack 實作邏輯（雙 Stack 法）：

        1. 此順序正好是「中 $\rightarrow$ 右 $\rightarrow$ 左」的反向。

        1. 利用第一個 Stack 依照「中右左」的順序壓入第二個 Stack

        1. 最後從第二個 Stack 依序彈出，即得到「左右中」。

---

1. Level-order Traversal (層序遍歷)

    順序：由上至下、從左至右 (Breadth-First Search, BFS)

    - 行為描述： 按照樹的深度，一層一層依序拜訪節點。

    - Queue 實作邏輯：

        1. 使用 Queue (隊列) 實作。

        1. 將根節點放入 Queue。

        1. 當 Queue 不為空時：

            - 從前端取出一個節點進行拜訪。

            - 若該節點有左子節點，放入 Queue。

            - 若該節點有右子節點，放入 Queue。

---
| 遍歷名稱        | 走訪順序      | 常用資料結構 | 應用場景        |
|-------------|-----------|--------|-------------|
| Preorder    | 中 → 左 → 右 | Stack  | 複製樹、表示前置表達式 |
| Inorder     | 左 → 中 → 右 | Stack  | BST 排序輸出    |
| Postorder   | 左 → 右 → 中 | Stack  | 刪除樹、計算後置表達式 |
| Level-order | 一層一層走     | Queue  | 尋找最短距離、層次分析 |



---

# LeetCode 的格式：

[1, null, 3, 2, 4, null, 5, 6]

👉 意思是 level order + null 分隔 children
