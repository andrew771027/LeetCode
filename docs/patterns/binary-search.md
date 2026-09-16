# 二分搜尋

[回學習索引](../readme.md) · [測試方法](../testing.md)

前提是資料有序，而且每次判斷都能排除一整半的候選範圍。#35 使用閉區間 `[start, end]`；目標比中間值大，就讓 `start = mid + 1`，反之讓 `end = mid - 1`。

```text
nums = [1, 3, 5, 6], target = 2
[0, 3] → mid = 1，3 太大 → end = 0
[0, 0] → mid = 0，1 太小 → start = 1
[1, 0] → 區間為空，插入位置是 1
```

迴圈結束時，start 左邊都小於 target，end 右邊都大於 target。空區間仍有一個明確的插入位置，這就是回傳 start 的理由。不要混用閉區間和半開區間的更新規則。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 035 · Search Insert Position

[解法](../../src/array/lc_035_search_insert_position.py) · [測試](../../tests/array/test_lc_035_search_insert_position.py) · Group：`array`

回傳目標索引或插入位置。比較中間值後排除半邊，找不到時回傳 start。

- **成本：** O(log n) 時間、O(1) 空間。
- **現有測試：** 固定找到與插入案例。
- **練習與邊界：** 補插入開頭、尾端及單一元素。
