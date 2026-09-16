# 查表、計數與出現位置

[回學習索引](../readme.md) · [測試方法](../testing.md)

查表的目的，是把前面處理過的資訊留下來，避免重複搜尋。表格不一定是 dict：字元範圍固定時，陣列也可以當查表工具。

#242 用 26 個欄位累加 s、扣除 t 的字元數；全部歸零才表示頻率相同。#205 存的是「上次出現位置加一」，不是出現次數。加一讓 0 專門代表未出現。

```text
s = egg   t = add
位置 0：e / a 上次都是 0 → 記為 1
位置 1：g / d 上次都是 0 → 記為 2
位置 2：g / d 上次都是 2 → 記為 3
```

Two Sum 可以延伸成 hash map：先查 `target - value` 是否已出現，再存入目前索引，便能避免重用自己。這是後續練習；目前 #1 仍是逐一搜尋。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 205 · Isomorphic Strings

[解法](../../src/string/lc_205_isomorphic_strings.py) · [測試](../../tests/string/test_lc_205_isomorphic_strings.py) · Group：`string`

判斷兩字串能否一對一替換。兩側字元的上次出現位置必須相同，並更新為 i+1。

- **成本：** O(n) 時間、O(1) 固定表空間。
- **現有測試：** 固定同構與非同構案例。
- **練習與邊界：** 補 ab 對 aa，避免多對一；目前 200 格表不支援一般 Unicode。

## 242 · Valid Anagram

[解法](../../src/string/lc_242_valid_anagram.py) · [測試](../../tests/string/test_lc_242_valid_anagram.py) · Group：`string`

判斷是否為字母異位詞。對 s 加次數、t 減次數，26 格都為零才相同。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 正例、反例及長度不同。
- **練習與邊界：** 補相同字元集合但次數不同；目前限制小寫英文字母。

## 501 · Find Mode In Binary Search Tree

[解法](../../src/tree/lc_501_find_mode_in_binary_search_tree.py) · [測試](../../tests/tree/test_lc_501_find_mode_in_binary_search_tree.py) · Group：`tree`

找 BST 的所有眾數。DFS 累計頻率，再挑出等於最高頻率的值。

- **成本：** O(n) 時間、O(n) 空間。
- **現有測試：** 參數化案例，排序後比較眾數。
- **練習與邊界：** 輸出可能不只一個值，順序不重要。
