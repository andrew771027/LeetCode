# 雙指標與原地寫入

[回學習索引](../readme.md) · [測試方法](../testing.md)

雙指標不是固定模板。先定義兩個位置各自代表什麼，再決定誰要移動。

#26、#27 使用讀取位置和寫入位置。每輪處理完成後，`nums[:k]` 都是已保留的有效答案；後面的內容不屬於輸出契約。#283 同樣維護讀寫位置，但以交換把零留在已掃描區間的後方，最後整個陣列都是答案。#88 則從尾端寫入，因為前方仍有尚未讀取的資料。

```text
#27：移除 3
輸入         [3, 2, 2, 3]
讀到第一個 2  [2, 2, 2, 3]  k = 1
讀到第二個 2  [2, 2, 2, 3]  k = 2
有效結果      [2, 2]         只讀 nums[:k]
```

#125 和 #234 從兩端向中間比較。每次相等就排除一對；不相等可以立刻結束。注意目前兩題都有建立新資料，不能把雙指標直接等同於 O(1) 空間。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 026 · Remove Duplicates From Sorted Array

[解法](../../src/array/lc_026_remove_duplicates_from_sorted_array.py) · [測試](../../tests/array/test_lc_026_remove_duplicates_from_sorted_array.py) · Group：`array`

有序陣列去重，回傳有效長度。讀到不同值才把寫入位置往前推。

- **成本：** O(n) 時間、O(1) 額外空間。
- **現有測試：** 原有長度案例，另補有效前綴檢查。
- **練習與邊界：** 尾端不必清空；保留原本排序。

## 027 · Remove Element

[解法](../../src/array/lc_027_remove_element.py) · [測試](../../tests/array/test_lc_027_remove_element.py) · Group：`array`

給定整數陣列 `nums` 與目標值 `val`，原地保留所有不等於 `val` 的元素，回傳有效長度；不要求輸入有序。答案只看有效前綴，尾端不必清空。

`i` 掃描每個元素，`index` 指向下一個寫入位置。遇到 `nums[i] != val` 時，寫入 `nums[index]` 並增加 `index`；遇到目標值則跳過。因為 `index <= i`，寫入不會破壞尚未讀取的資料。每輪結束後，`nums[:index]` 就是目前已讀元素中要保留的值，最後回傳 `index`。

- **成本：** O(n) 時間、O(1) 額外空間，沒有建立切片或暫存陣列。
- **現有測試：** 兩組一般案例檢查長度；`test_retained_prefix` 涵蓋空陣列、混合值、全部刪除與完全不刪除，驗證長度及排序後的有效前綴。此比較不要求保留順序，雖然目前實作會保留順序。
- **測試方法：** `poetry run pytest tests/array/test_lc_027_remove_element.py -q`。

## 088 · Merge Sorted Array

[解法](../../src/array/lc_088_merge_sorted_array.py) · [測試](../../tests/array/test_lc_088_merge_sorted_array.py) · Group：`array`

合併兩個有序陣列到 nums1。比較兩側尾端，把較大者寫到空間尾端，避免覆蓋尚未讀取的值。

- **成本：** O(m+n) 時間、O(1) 額外空間。
- **現有測試：** 原有回傳值案例，另補原地修改檢查。
- **練習與邊界：** 目前也回傳 nums1；題目主要要求修改輸入。

## 125 · Valid Palindrome

[解法](../../src/string/lc_125_valid_palindrome.py) · [測試](../../tests/string/test_lc_125_valid_palindrome.py) · Group：`string`

忽略非英數與大小寫後判斷回文。先用正規表示式清理，再比較兩端。

- **成本：** O(n) 時間、O(n) 清理空間。
- **現有測試：** 回文、非回文、空白。
- **練習與邊界：** 清理後為空字串應回傳 True。

## 234 · Palindrome Linked List

[解法](../../src/linkedlist/lc_234_palindrome_linked_list.py) · [測試](../../tests/linkedlist/test_lc_234_palindrome_linked_list.py) · Group：`linkedlist`

判斷串列值是否為回文。目前先複製到 list 再比較兩端，沒有啟用反轉後半段的註解版本。

- **成本：** O(n) 時間、O(n) 空間。
- **現有測試：** 參數化的回文與非回文案例。
- **練習與邊界：** 可延伸快慢指標加反轉；若改動連線，思考是否要還原。

## 283 · Move Zeroes

[解法](../../src/array/lc_283_move_zeroes.py) · [測試](../../tests/array/test_lc_283_move_zeroes.py) · 難度：Easy · Group：`array`

給定未排序的整數陣列，把所有零移到尾端，並保留非零元素的相對順序。必須修改原本的 list，回傳 `None`。題目輸入至少有一個元素；目前實作與測試也支援空陣列。

### 為什麼使用雙指標

與 #27 一樣，可以讓一個位置掃描輸入，另一個位置記住下一個非零元素要放在哪裡。差別是 #283 要保留陣列長度並讓尾端全為零，因此目前解法使用交換，把前方的零換到已掃描區間的後方。

每輪開始時，`nums[:left]` 是已讀到的非零元素，順序與輸入一致；`nums[left:right]` 全為零，`right` 之後仍待處理。這裡的切片只是描述區間，程式沒有建立切片。

1. 將 `left` 設為 0，讓 `right` 依序掃描每個位置。
2. 若 `nums[right] == 0`，只讓掃描繼續，零區間因而擴大。
3. 遇到非零值時，交換 `nums[right]` 與 `nums[left]`，再將 `left` 加一。當兩個位置相同時，只是與自己交換；否則會把 `left` 上的零換到 `right`。
4. 掃描結束後，所有非零元素依讀取順序排在前面，其餘位置都是零，不需要另外補零。

```text
輸入 [0, 1, 0, 3, 12]，left = 0
right  讀到的值  處理後 nums          處理後 left
0      0         [0, 1, 0, 3, 12]    0
1      1         [1, 0, 0, 3, 12]    1
2      0         [1, 0, 0, 3, 12]    1
3      3         [1, 3, 0, 0, 12]    2
4      12        [1, 3, 12, 0, 0]    3
```

- **成本：** O(n) 時間，每個位置掃描一次；O(1) 額外空間，交換只需要固定大小的暫存資料。
- **現有測試：** 8 組參數化案例涵蓋題目範例、單一零、無零、全零、前端連續零、尾端連續零、空陣列，以及含負數的混合資料。每組都檢查回傳值為 `None`、完整結果與順序，以及呼叫前後 list 的 `id` 相同。這些檢查不量測額外空間，O(1) 仍需由實作分析。
- **測試方法：** `poetry run pytest tests/array/test_lc_283_move_zeroes.py -q`。
