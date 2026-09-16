# 進位、位元運算與逐列建構

[回學習索引](../readme.md) · [測試方法](../testing.md)

這組題目先把運算規則寫清楚，再逐位或逐列處理。它們不共享一個通用模板。

#66 從個位往前傳遞進位。#67 把兩個二進位位數和 carry 相加：`total % 2` 是本位，`total // 2` 是下一位進位。#168 的欄位編號從 1 起算，所以取餘數前要先減一。

```text
十進位加一： [9, 9] → [9, 0] → [0, 0] → [1, 0, 0]
Excel 欄位： 26 → Z；27 → AA（沒有代表 0 的字母）
Pascal：     [1, 2, 1] → [1, 1+2, 2+1, 1]
```

#136 使用 XOR 的交換律、結合律與 `x ^ x = 0`，讓成對數值抵消。這只適用於其他元素都出現兩次的前提。

#118 利用上一列求下一列，是動態規劃的狀態轉移；目前用遞迴取得前面所有列，再追加新的一列。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 066 · Plus One

[解法](../../src/array/lc_066_plus_one.py) · [測試](../../tests/array/test_lc_066_plus_one.py) · Group：`array`

以數字陣列表示整數加一。從尾端處理，遇非 9 就加一回傳；全部是 9 才新增最高位。

- **成本：** O(n) 時間，全 9 時配置 O(n) 新結果。
- **現有測試：** 一般進位、單個 9、連續 9。
- **練習與邊界：** 目前會修改傳入陣列；輸入需非空。

## 067 · Add Binary

[解法](../../src/string/lc_067_add_binary.py) · [測試](../../tests/string/test_lc_067_add_binary.py) · Group：`string`

兩個二進位字串相加。從右往左累加兩位與 carry，收集本位後反轉。

- **成本：** O(max(m,n)) 時間與空間。
- **現有測試：** 固定二進位加法案例。
- **練習與邊界：** 補長度不同與最後還有 carry。

## 118 · Pascals Triangle

[解法](../../src/array/lc_118_pascals_triangle.py) · [測試](../../tests/array/test_lc_118_pascals_triangle.py) · Group：`array`

產生 Pascal triangle。遞迴取得前面各列，新列兩端為 1，中間由上一列相鄰兩數相加。

- **成本：** r 列時間 O(r²)，輸出 O(r²)，遞迴堆疊 O(r)。
- **現有測試：** 0 列、1 列及 5 列完整結果。
- **練習與邊界：** 可補每列對稱、列和為 2^i，但性質不能取代所有精確值檢查。

## 136 · Single Number

[解法](../../src/array/lc_136_single_number.py) · [測試](../../tests/array/test_lc_136_single_number.py) · Group：`array`

找唯一只出現一次的數。由 0 起累積 XOR，成對值抵消，留下答案。

- **成本：** O(n) 時間、O(1) 空間（固定整數位寬）。
- **現有測試：** 固定單獨值案例。
- **練習與邊界：** 補負數與打亂順序；其他值必須恰好出現兩次。

## 168 · Excel Sheet Column Title

[解法](../../src/string/lc_168_excel_sheet_column_title.py) · [測試](../../tests/string/test_lc_168_excel_sheet_column_title.py) · Group：`string`

將正整數轉成 Excel 欄位名稱。每輪先減一，再除以 26 取得字母，最後反轉。

- **成本：** k 個輸出字元需 O(k) 輪、O(k) 空間。
- **現有測試：** A、AB、ZY 等固定案例。
- **練習與邊界：** 補 26/27 與 702/703 的位數交界。

## 171 · Excel Sheet Column Number

[解法](../../src/string/lc_171_excel_sheet_column_number.py) · [測試](../../tests/string/test_lc_171_excel_sheet_column_number.py) · Group：`string`

將欄位名稱轉成數字。從右至左以字母值乘上 26 的位置次方，再累加。

- **成本：** k 個字元需 O(k) 次累加；含 pow 的成本，不能視為任意大整數下嚴格線性。
- **現有測試：** 固定欄位名稱案例。
- **練習與邊界：** 可與 #168 做往返測試；逐字 result*26+value 可避免每輪求次方。
