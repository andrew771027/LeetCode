# 二元搜尋樹與分治

[回學習索引](../readme.md) · [測試方法](../testing.md)

BST 的中序結果有序，因此最小差值只需要比較相鄰值。若排序後有 a ≤ b ≤ c，c − a 不可能小於 b − a 和 c − b 兩者，所以 #530 不必比較所有配對。

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
- **練習與邊界：** 至少兩個節點；可延伸只保存 previous 值。
