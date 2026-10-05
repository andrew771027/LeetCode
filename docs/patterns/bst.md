# 二元搜尋樹與分治

[回學習索引](../readme.md) · [測試方法](../testing.md)

BST 的中序結果有序，因此最小差值只需要比較相鄰值。若排序後有 a ≤ b ≤ c，c − a 不可能小於 b − a 和 c − b 兩者，所以 #530 與 #783 不必比較所有配對。最小差的兩個節點也不一定是父子，只比較樹上的連線會漏掉答案。

#108 從有序陣列的中點建立根，左右半段各自建立子樹。每層左右大小相近，才能保證高度平衡。

```text
[-10, -3, 0, 5, 9]
          0
        /         -3     9
      /     /
    -10    5
```

這是目前選取上中位數所得到的一種答案。合法的平衡 BST 不只有這一種；測試固定形狀可以檢查目前策略，但若要允許其他解法，應檢查中序結果和每個節點的高度差。

#501 雖然輸入是 BST，目前仍用一般 DFS 加頻率表，沒有利用中序的連續相同值。題目群組和目前使用的 Pattern 可以不同。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 108 · Convert Sorted Array To Binary Search Tree

[解法](../../src/tree/lc_108_convert_sorted_array_to_binary_search_tree.py) · [測試](../../tests/tree/test_lc_108_convert_sorted_array_to_binary_search_tree.py) · Group：`tree`

將有序陣列轉成高度平衡 BST。選中點當根，左右切片各自遞迴。

- **成本：** 目前切片版 O(n log n) 時間，額外空間峰值 O(n)，輸出 O(n)。
- **現有測試：** 固定層序形狀案例。
- **練習與邊界：** 可補中序等於原陣列、逐節點高度差不超過 1；索引版可省切片。

## 530 · Minimum Absolute Difference In Bst

[解法](../../src/tree/lc_530_minimum_absolute_difference_in_bst.py) · [測試](../../tests/tree/test_lc_530_minimum_absolute_difference_in_bst.py) · Group：`tree`

求 BST 任兩節點的最小絕對差。中序收集有序值，再比較相鄰差。

- **成本：** O(n) 時間、O(n) 空間。
- **現有測試：** 參數化 BST 案例。
- **練習與邊界：** 至少兩個節點；只保存 previous 值的做法見下方 [#783](#783--minimum-distance-between-bst-nodes)。


## 783 · Minimum Distance Between BST Nodes

[解法](../../src/tree/lc_783_minimum_distance_between_bst_nodes.py) · [測試](../../tests/tree/test_lc_783_minimum_distance_between_bst_nodes.py) · Group：`tree`

輸入為至少兩個節點、節點值非負的 BST，求任意兩個不同節點值的最小差。#783 與 #530 是相同問題，兩題都使用「BST 中序有序 → 比較相鄰值」的 Pattern，也可以互用解法。目前 #530 先收集完整陣列再掃描；#783 改成在走訪時直接比較，只保存上一個值 `previous` 與目前最小差 `min_difference`。

### 推理與步驟

中序按「左子樹 → 目前節點 → 右子樹」走訪，因此 `previous` 是有序序列中上一個值，不一定是目前節點的父節點。處理目前節點前，`min_difference` 已記錄所有已走訪相鄰值的最小差；加入目前這一對即可維持此條件。

1. 每次呼叫 `minDiffInBST`，將 `previous` 重設為 `None`，最小差重設為無限大。
2. 遞迴走訪左子樹。
3. 若 `previous is not None`，用 `node.val - previous` 更新最小差；有序性保證差值非負。
4. 將 `previous` 更新為目前值，再遞迴走訪右子樹。
5. 完成走訪後回傳最小差。第一個節點沒有前值，跳過比較；前值可能是 `0`，因此不能用真假值判斷。

以 `multiple-levels` 測資為例：

```text
        10
       /  \
      5    20
     / \   / \
    2   8 15 30

中序值：2 → 5 → 8 → 10 → 15 → 20 → 30
相鄰差：  3   3   2    5    5    10
```

走訪到 `10` 時，`previous` 是 `8`，得到最小差 `2`；這兩個節點不是直接父子。

### 成本與測試

- **成本：** O(n) 時間；兩個狀態變數佔 O(1)，遞迴堆疊佔 O(h)，所以總額外空間為 O(h)。平衡樹為 O(log n)，退化成鏈時為 O(n)。#530 的陣列版額外空間為 O(n)。
- **現有測試：** pytest 參數化五筆層序資料，用 `list_to_binary_tree` 建樹，再比較回傳值。涵蓋一般例子、含 `0` 與右側最小差、兩個節點、多層樹，以及 `[10, 5, None, None, 9]` 中非父子的 `9`、`10` 差值為 `1`。最後一筆也能抓出漏比較最後一組相鄰值的錯誤。
- **測試方法：** `poetry run pytest tests/tree/test_lc_783_minimum_distance_between_bst_nodes.py -q`。
- **延伸建議：** 可補同一個 `Solution` 連續呼叫以驗證狀態重設，以及較長的偏斜樹。空樹與單節點不在題目前提內，目前實作會回傳無限大。
