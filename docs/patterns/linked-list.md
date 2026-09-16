# 鏈結串列：快慢指標與重新接線

[回學習索引](../readme.md) · [測試方法](../testing.md)

鏈結串列沒有隨機索引。移動指標前，先想清楚要保留哪一條連線。

#206 反轉串列時，先暫存 next，才能在改寫 current.next 後繼續前進。#203 使用 dummy node，讓刪除首節點也能寫成 `previous.next = current.next`。刪除時 previous 留在原處，才能處理連續刪除。

```text
反轉前：None ← previous    current → next → ...
暫存：  temp = current.next
接線：  previous ← current    temp → ...
前進：  previous = current；current = temp
```

#876 的 fast 每次走兩步、slow 走一步，fast 到尾端時 slow 在中點。偶數長度會回傳第二個中點。#141 使用相同速度差：進入環後，fast 每輪相對 slow 多走一步，最後會相遇。必須比較節點身分 `is`；兩個節點值相同並不代表有環。

#160 讓兩個指標走完各自串列後換到另一條，抵消前段長度差；相交時會抵達同一個節點，無交集時會一起到 None。

## 題目筆記

本篇依題號排列，#19、#61 標為 Medium，其餘為 Easy。可先練 #203 的 dummy node 與 #206 的接線，再閱讀這兩題。

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 019 · Remove Nth Node From End of List · Medium

[解法](../../src/linkedlist/lc_019_remove_nth_node_from_end_of_list.py) · [測試](../../tests/linkedlist/test_lc_019_remove_nth_node_from_end_of_list.py)

刪除倒數第 n 個節點。從 dummy 出發，fast 先走 n+1 步，再讓 fast 和 slow 同速移動。fast 到 None 時，slow 正好停在要刪除節點的前面，因此可用 `slow.next = slow.next.next`。

時間 O(L)、額外空間 O(1)。現有測試以參數化資料建串列，轉回 list 比較結果。閱讀時特別檢查 n 等於串列長度的情況：此時要刪的是 head，dummy 可以統一處理。輸入前提是 1 ≤ n ≤ L。

## 021 · Merge Two Sorted Lists

[解法](../../src/linkedlist/lc_021_merge_two_sorted_lists.py) · [測試](../../tests/linkedlist/test_lc_021_merge_two_sorted_lists.py) · Group：`linkedlist`

合併兩條有序串列。dummy 後面每次接較小的節點，最後接上剩下整段。

- **成本：** O(m+n) 時間、O(1) 額外空間。
- **現有測試：** 轉換 list 建串列，結果轉回 list 比較。
- **練習與邊界：** 會重用並改接原節點，不能假設輸入仍獨立。

## 061 · Rotate List · Medium

[解法](../../src/linkedlist/lc_061_rotate_list.py) · [測試](../../tests/linkedlist/test_lc_061_rotate_list.py)

將串列向右旋轉 k 格。先求長度 L，把 k 化為 k % L，再暫時把尾端接回 head。從舊尾端前進 L−k 步會抵達新尾端，記住下一個節點後斷開環。

```text
1 → 2 → 3 → 4 → 5，k = 2
新尾端是 3；新頭是 4
4 → 5 → 1 → 2 → 3 → None
```

時間 O(L)、額外空間 O(1)。現有參數化測試涵蓋一般旋轉與邊界，最後轉回 list 比較。斷環是必要步驟；遺漏時轉換器不會走到 None。空串列在取餘數前就回傳，避免除以零。

## 083 · Remove Duplicates From Sorted List

[解法](../../src/linkedlist/lc_083_remove_duplicates_from_sorted_list.py) · [測試](../../tests/linkedlist/test_lc_083_remove_duplicates_from_sorted_list.py) · Group：`linkedlist`

刪除有序串列重複值。相鄰值相同就跳過下一節點；刪除後 current 不前進。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 參數化案例，轉回 list 比較。
- **練習與邊界：** 補三個以上連續相同值，檢查沒有漏刪。

## 141 · Linked List Cycle

[解法](../../src/linkedlist/lc_141_linked_list_cycle.py) · [測試](../../tests/linkedlist/test_lc_141_linked_list_cycle.py) · Group：`linkedlist`

判斷有無環。fast 走兩步、slow 走一步，兩者指向同一節點便代表有環。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** helper 依 pos 建立真實的環。
- **練習與邊界：** 不要把循環串列轉成一般 list；可補自環。

## 160 · Intersection Of Two Linked Lists

[解法](../../src/linkedlist/lc_160_intersection_of_two_linked_lists.py) · [測試](../../tests/linkedlist/test_lc_160_intersection_of_two_linked_lists.py) · Group：`linkedlist`

找兩條串列共用的起始節點。走完自己的串列就切換到另一條，使總路程一致。

- **成本：** O(m+n) 時間、O(1) 空間。
- **現有測試：** helper 建立共享尾端，使用 is 驗證答案。
- **練習與邊界：** 相同值但不同物件不算交集。

## 203 · Remove Linked List Elements

[解法](../../src/linkedlist/lc_203_remove_linked_list_elements.py) · [測試](../../tests/linkedlist/test_lc_203_remove_linked_list_elements.py) · Group：`linkedlist`

移除所有等於 val 的節點。dummy 統一頭部刪除，刪除時 previous 留在原地。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 參數化案例，轉回 list 比較。
- **練習與邊界：** 連續頭部刪除與全部刪除。

## 206 · Reverse Linked List

[解法](../../src/linkedlist/lc_206_reverse_linked_list.py) · [測試](../../tests/linkedlist/test_lc_206_reverse_linked_list.py) · Group：`linkedlist`

反轉每一條 next 連線。先保存下一節點，再接回 previous，最後回傳 previous。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 參數化案例，檢查反轉後值。
- **練習與邊界：** 可補反轉兩次回到原串列的性質。

## 876 · Middle Of Linked List

[解法](../../src/linkedlist/lc_876_middle_of_linked_list.py) · [測試](../../tests/linkedlist/test_lc_876_middle_of_linked_list.py) · Group：`linkedlist`

回傳中間節點。fast 到尾端時 slow 在中間，偶數長度選第二個中點。

- **成本：** O(n) 時間、O(1) 空間。
- **現有測試：** 參數化案例檢查中點後的串列。
- **練習與邊界：** 同時檢查奇數與偶數長度。
