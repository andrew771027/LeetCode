# Stack、Queue 與操作序列

[回學習索引](../readme.md) · [測試方法](../testing.md)

Stack 是後進先出，Queue 是先進先出。分類依要實作的介面：#225 是 Stack，#232 是 Queue；內部使用哪種容器則寫在解法裡。

#20 遇到右括號時，只能配對最近尚未配對的左括號，因此需要 stack。數量相等不夠，例如 `([)]` 仍然錯誤。

#232 的 input 負責收新資料，output 負責取舊資料。只有 output 空了才倒入，否則會打亂先後順序。

```text
push(1), push(2)     input = [1, 2]   output = []
peek()，倒入         input = []       output = [2, 1] ← 頂端
push(3)              input = [3]      output = [2, 1]
pop() → 1            input = [3]      output = [2]
```

每個元素最多進 input 一次、搬到 output 一次、被取出一次，所以整串操作的平均成本為 O(1)；單次觸發搬移的 peek 或 pop 仍可能是 O(n)。測試需要交錯 push、peek、pop，才能檢查搬移時機。

## 題目筆記

以下「現有測試」描述目前測試；「練習與邊界」是閱讀提醒或後續可補項目。n 表示元素數、h 表示樹高、w 表示最大層寬；其他符號在各題說明。

## 020 · Valid Parentheses

[解法](../../src/stack/lc_020_valid_parentheses.py) · [測試](../../tests/stack/test_lc_020_valid_parentheses.py) · Group：`stack`

判斷括號是否正確巢狀配對。左括號入 stack，右括號必須匹配頂端，結束時 stack 要空。

- **成本：** O(n) 時間、O(n) 空間。
- **現有測試：** 固定合法與不合法括號案例。
- **練習與邊界：** 補 ([)]、只有左括號、第一個就是右括號。

## 225 · Implement Stack Using Queues

[解法](../../src/stack/lc_225_implement_stack_using_queues.py) · [測試](../../tests/stack/test_lc_225_implement_stack_using_queues.py) · Group：`stack`

用兩個 queue 做 stack。pop/top 把前面元素搬走，最後一個就是頂端；top 還要放回。

- **成本：** push/empty O(1)，pop/top O(n)；空間 O(n)。
- **現有測試：** 固定操作序列、Hypothesis 資料生成、StackStateMachine。
- **練習與邊界：** 連續 top 不應刪掉資料；空容器 pop 不在目前合法操作範圍。

## 232 · Implement Queue Using Stacks

[解法](../../src/queue/lc_232_implement_queue_using_stacks.py) · [測試](../../tests/queue/test_lc_232_implement_queue_using_stacks.py) · Group：`queue`

用兩個 stack 做 queue。output 空時才從 input 倒入，翻轉順序後最早加入的在頂端。

- **成本：** push/empty O(1)，pop/peek 攤銷 O(1)、單次最壞 O(n)；空間 O(n)。
- **現有測試：** 固定操作序列、deque 比對及 QueueStateMachine。
- **練習與邊界：** 交錯 push/pop 能驗證搬移時機。
