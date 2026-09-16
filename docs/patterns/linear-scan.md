# 線性掃描與字串處理

[回學習索引](../readme.md) · [測試方法](../testing.md)

先找出「檢查過的位置」能提供哪些資訊。若每一步只需要目前字元、相鄰字元或一段候選字串，直接掃描通常最容易說明，也容易測試。

#28 每次移動候選起點，重新比較整段 needle。雖然視窗長度固定，但沒有重用視窗的統計資訊，因此這裡將它歸為直接搜尋。它目前不是 KMP。

```text
haystack = s a d b u t s a d
起點 0     [s a d]             → 相符，回傳 0
起點 6                 [s a d] → 不必再找，題目要第一次出現
```

#14 的排序有另一個觀察：共同前綴只要在字典序最前與最後的字串比較即可。中間的字串若在此前綴內不同，就不可能仍排在兩者之間。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 001 · Two Sum

[解法](../../src/array/lc_001_two_sum.py) · [測試](../../tests/array/test_lc_001_two_sum.py) · Group：`array`

找兩個不同索引，使數值和等於 target。逐一取數值，再在後方切片搜尋補數；例如 [2,7,11,15]、9 回傳 [0,1]。

- **成本：** 時間 O(n²)，切片額外空間 O(n)。
- **現有測試：** 固定案例比較索引。
- **練習與邊界：** 加入重複值 [3,3]，檢查索引不同；延伸 dict 查補數。

## 013 · Roman To Integer

[解法](../../src/string/lc_013_roman_to_integer.py) · [測試](../../tests/string/test_lc_013_roman_to_integer.py) · Group：`string`

將羅馬數字轉整數。若目前數值小於下一個就扣除，否則加上；IV = -1 + 5 = 4。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 固定羅馬數字案例。
- **練習與邊界：** 補最後一字元與不同減法組合。

## 014 · Longest Common Prefix

[解法](../../src/string/lc_014_longest_common_prefix.py) · [測試](../../tests/string/test_lc_014_longest_common_prefix.py) · Group：`string`

找所有字串的共同前綴。排序後只比較首尾字串；flower、flow、flight 得到 fl。

- **成本：** n 個字串、最大長度 L，時間保守上界 O(L·n log n + L²)，包含字串逐次累加；空間 O(n+L)。
- **現有測試：** 共同前綴及無共同前綴。
- **練習與邊界：** 補單一字串、含空字串；輸入陣列需非空。

## 028 · Find The Index Of The First Occurrence In A String

[解法](../../src/string/lc_028_find_the_index_of_the_first_occurrence_in_a_string.py) · [測試](../../tests/string/test_lc_028_find_the_index_of_the_first_occurrence_in_a_string.py) · Group：`string`

回傳 needle 第一次出現的位置。逐起點切片比對，相符即回傳，找不到回傳 -1。

- **成本：** 最壞 O(nm) 時間、O(m) 切片空間。
- **現有測試：** 找到與找不到的固定案例。
- **練習與邊界：** 補匹配在尾端、needle 比 haystack 長。

## 058 · Length Of Last Word

[解法](../../src/string/lc_058_length_of_last_word.py) · [測試](../../tests/string/test_lc_058_length_of_last_word.py) · Group：`string`

回傳最後一個單字長度。目前先 strip，再以空白 split，取得最後一段。

- **成本：** O(n) 時間、O(n) 空間。
- **現有測試：** 一般字串與尾端空白。
- **練習與邊界：** 補單一字母；可練習從尾端掃描以省空間。
