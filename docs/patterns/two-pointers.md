# 雙指標與原地寫入

[回學習索引](../readme.md) · [測試方法](../testing.md)

雙指標不是固定模板。先定義兩個位置各自代表什麼，再決定誰要移動。

#26、#27 使用讀取位置和寫入位置。每輪處理完成後，`nums[:k]` 都是已保留的有效答案；後面的內容不屬於輸出契約。#88 則從尾端寫入，因為前方仍有尚未讀取的資料。

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

原地移除 val，遇到要保留的值才寫入 nums[k] 並增加 k。

- **成本：** O(n) 時間、O(1) 額外空間。
- **現有測試：** 原有長度案例，另補有效前綴檢查。
- **練習與邊界：** 全部刪除與完全不刪除。

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
