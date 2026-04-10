# Used Extension
- [x] gitignore
- [x] pre-commit
- [x] poetry

# Used Package / Function

- [x] Pytest
    - [x] pytest.mark.parametrize
    - [ ] pytest-benchmark
    - [ ] pytest-randomly (隨機測試)
    - [ ] pytest-xdist (平行測試)
    - [ ] pytest-cov（測試覆蓋率）
- [x] Hypothesis
    - [x] given
    - [x] strategies
    - [x] settings
- [ ] faker
- [ ] golden test
- [ ] monkeypatch

# TODO
- [ ] Leetcode Test Framework
   - [ ] registry
   - [ ] fuzz testing
   - [ ] benchmark
   - [ ] multi-solution comparison
   - [ ] model-based testing
   - [ ] property-based testing

---
## 一、這個 Framework 的核心價值（先講本質）

你不是在做：

❌ 一堆題目的集合

你是在做：

✅ 一個可以驗證演算法正確性 / 穩定性 / 效能的測試系統

## 二、整體架構（推薦設計）
```bash
leetcode-practice/
├── src/                     # 解法
│   ├── array/
│   │   └── lc_001_two_sum.py
│
├── tests/                   # pytest 測試
│   ├── test_two_sum.py
│
├── framework/               # 🔥 核心框架
│   ├── runner.py
│   ├── registry.py
│   ├── comparator.py
│   ├── generators.py
│   ├── benchmark.py
│   └── report.py
│
├── configs/
│   └── problems.yaml        # 題目定義
│
└── scripts/
    └── run_all.py
```

## 三、核心元件設計（重點）
### 1️⃣ registry（題目註冊系統）

👉 讓你的 framework 知道「有哪些題目」
```python
# framework/registry.py

REGISTRY = {}

def register(problem_id):
    def wrapper(func):
        REGISTRY[problem_id] = func
        return func
    return wrapper
```

使用方式
```python
# src/array/lc_001_two_sum.py

from framework.registry import register

@register("1")
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```
👉 好處：

- 可以自動跑全部題目
- 支援多解法比較（超強）
### 2️⃣ runner（執行核心）
```python
# framework/runner.py

from framework.registry import REGISTRY

def run(problem_id, cases):
    func = REGISTRY[problem_id]

    results = []
    for case in cases:
        output = func(**case["input"])
        results.append((output, case["expected"]))

    return results
```
### 3️⃣ comparator（比對邏輯）

👉 很多題目不能用 ==（例如順序不重要）
```python
# framework/comparator.py

def compare(actual, expected, unordered=False):
    if unordered:
        return sorted(actual) == sorted(expected)
    return actual == expected
```
👉 進階：

- tolerance（float）
- linked list compare
- tree compare
### 4️⃣ generators（測資生成器🔥）

👉 這是你比別人強的地方
```python
# framework/generators.py

import random

def gen_two_sum_case(size=10):
    nums = [random.randint(-100, 100) for _ in range(size)]
    i, j = random.sample(range(size), 2)
    target = nums[i] + nums[j]

    return {
        "input": {"nums": nums, "target": target},
        "expected": [i, j]
    }
```
👉 這就是：
```bash
property-based testing + fuzz testing 的核心
```
### 5️⃣ benchmark（效能測試）
```python
# framework/benchmark.py

import time

def benchmark(func, case, repeat=100):
    start = time.time()

    for _ in range(repeat):
        func(**case["input"])

    return time.time() - start
```
👉 進階：

- 比較多解法（O(n²) vs O(n)）
- 自動輸出排名
### 6️⃣ report（報告系統）
```python
# framework/report.py

def print_report(results):
    for i, (actual, expected) in enumerate(results):
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] Case {i}")
```
👉 進階可以做：

- JSON report
- HTML report
- coverage 整合
## 四、進階功能（你做到這會很猛）
### 🔥 1. 多解法比較（超加分）
```python
@register("1_v1")
def two_sum_bruteforce(...)

@register("1_v2")
def two_sum_hashmap(...)
```
👉 framework 自動：

- 跑同一組測資
- 比較正確性
- 比 benchmark
### 🔥 2. 自動 fuzz 測試
```python
for _ in range(1000):
    case = gen_two_sum_case()
    run("1", [case])
```
👉 你會抓到：

- edge case bug
- hidden bug
🔥 3. Property 驗證整合
```python
def validate_two_sum(nums, target, result):
    i, j = result
    return nums[i] + nums[j] == target
```
👉 比 expected 更強

### 🔥 4. CLI 工具
```bash
python scripts/run_all.py --problem 1 --benchmark
```
## 五、你可以怎麼「實際開始」

我建議你這樣做👇

### Step 1（今天就能做）
- 建 framework/registry.py
- 改 3 題用 register
### Step 2（這週）
- 加 generator（random case）
- 寫 runner
### Step 3（下週）
- 加 benchmark
- 加多解法比較
## 六、這個專案的「職涯價值」

如果你做到這種程度，你已經不是：

QA ❌

而是：

✅ Test Infra Engineer / SDET（高階）

面試你可以直接講：

「我做了一個 LeetCode test framework，支援 registry、fuzz testing、benchmark、multi-solution comparison」

👉 這句話含金量非常高


---
# Testing Methods

---
## State Transition Testing

### State Transition Testing（狀態轉移測試）

#### 核心概念
系統會在不同「狀態（state）」之間切換
👉 測試重點是：狀態 + 事件 + 轉移是否正確

---
#### 📌 簡單例子：登入系統

狀態：

Logged out
Logged in
Locked

事件：

正確密碼
錯誤密碼（連續3次）

轉移：
| 當前狀態       | 事件   | 下一狀態       |
| ---------- | ---- | ---------- |
| Logged out | 正確登入 | Logged in  |
| Logged out | 錯誤3次 | Locked     |
| Locked     | 解鎖   | Logged out |

---
#### 🧠 測試重點
所有狀態都有被測到嗎？
每個轉移都正確嗎？
非法轉移有被擋住嗎？

👉 例如：
Locked 狀態還能登入嗎？（應該不能）

---
#### 🧪 適用場景
workflow（訂單流程）
UI flow（頁面切換）
狀態機系統（finite state machine）

---
## Model Based Testing
### Model-Based Testing（模型導向測試）

#### 核心概念

先建立「系統模型」，再從模型自動產生測試

👉 模型 = 系統行為的抽象表示
（可以是 state machine、流程圖、rule）

---
#### 📌 和 State Transition 的關係
👉 State Transition Testing 是一種「模型」
👉 Model-Based Testing 是更大的概念（包含它）

---
#### 📌 範例

你定義一個 model：

```python
state = LoggedOut

def login(password):
    if correct(password):
        state = LoggedIn
    else:
        fail_count += 1
```

然後工具會：

自動生成測試路徑
自動驗證實際系統 vs model 是否一致

---
#### 🧠 重點
不是手寫 test case
👉 而是寫「模型」，讓測試自己長出來

---
#### 🧪 常見工具
GraphWalker
Spec Explorer
Hypothesis stateful testing（Python）

---
#### 🧪 適用場景
複雜業務邏輯
API flow
狀態很多、路徑很多（人工測不完）

---
## Property-Based Testing

### Property-Based Testing（性質導向測試）

---
#### 核心概念

不是測「特定輸入 → 特定輸出」
👉 而是測「永遠成立的性質（property）」

---
#### 📌 範例：排序

你不用寫：

```python
assert sort([3,1,2]) == [1,2,3]
```

👉 而是寫「性質」：

```python
def test_sort(xs):
    ys = sort(xs)
    assert is_sorted(ys)
    assert same_elements(xs, ys)
```

然後工具會：
👉 自動生成一堆亂數測資

---
#### 🧠 重點

測的是「規則」，不是「案例」

---
#### 🧪 常見工具
Hypothesis（Python）
QuickCheck（Haskell）
ScalaCheck

---
#### 🔥 強大之處
自動找 edge cases
可以發現你想不到的 bug
shrinking（幫你縮小 failing case）


---
### 🧠 三者差異總結
| 類型               | 核心   | 測什麼           | 特點     |
| ---------------- | ---- | ------------- | ------ |
| State Transition | 狀態變化 | state + event | 明確流程   |
| Model-Based      | 抽象模型 | 系統 vs model   | 自動產測試  |
| Property-Based   | 性質   | invariant     | 自動生成資料 |

### 🔗 它們之間的關係（很重要）

👉 可以這樣理解：
```bash
Model-Based Testing
    ├── State Transition Testing（模型的一種）
    └── Property-Based Testing（驗證模型或系統）
```
甚至可以組合：

👉 用 Hypothesis 做「stateful model-based testing」

---

## Hypothesis

### 🧪 Hypothesis 快速總覽

Hypothesis
是一個 Property-Based Testing（性質導向測試） 工具，會自動產生測試資料來驗證你的「規則（properties）」是否成立。

👉 核心概念：

你不是寫「測試案例」
而是寫「這個程式應該永遠成立的性質」

---
#### 1️⃣ @given：輸入生成器

最核心 decorator，用來餵資料給測試

```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers())
def test_addition(x):
    assert x + x == 2 * x
```
👉 重點：

每次執行會用「不同的 x」
自動測 edge cases（0, 負數, 大數）

---
#### 2️⃣ strategies (st)：資料生成策略

Hypothesis 的資料來源

常用 strategies
```python
import hypothesis.strategies as st
```

##### 🔢 基本型別
```python
st.integers()
st.floats()
st.booleans()
st.text()
```

##### 📦 容器
```python
st.lists(st.integers())
st.tuples(st.integers(), st.text())
st.dictionaries(st.text(), st.integers())
```

##### 🎯 限制條件
```python
st.integers(min_value=0, max_value=100)
st.text(min_size=1, max_size=10)
```

##### 範例：測排序
```python
@given(st.lists(st.integers()))
def test_sort(lst):
    result = sorted(lst)

    assert len(result) == len(lst)          # 長度不變
    assert sorted(result) == result         # 已排序
```
#### 3️⃣ assume()：過濾資料

用來跳過不符合條件的輸入

```python
from hypothesis import assume

@given(st.integers())
def test_division(x):
    assume(x != 0)
    assert (x / x) == 1
```
👉 類似：

precondition
filtering input

⚠️ 不要濫用（會降低測試效率）

---
#### 4️⃣ @settings：測試設定

控制 Hypothesis 行為

```python
from hypothesis import settings

@settings(max_examples=1000, deadline=None)
@given(st.integers())
def test_something(x):
    assert x + 1 > x
```

##### 常用參數
| 參數             | 說明            |
| -------------- | ------------- |
| `max_examples` | 測試次數          |
| `deadline`     | timeout（ms）   |
| `verbosity`    | debug 輸出      |
| `phases`       | 控制 shrink 等階段 |

---

#### 5️⃣ example()：手動補案例

```python
from hypothesis import example

@given(st.integers())
@example(0)
@example(1)
def test_add(x):
    assert x + x == 2 * x
```

👉 用途：

加入你已知的重要 case
regression testing

#### 6️⃣ draw()：進階資料生成

用在 @composite strategy

```python
from hypothesis.strategies import composite

@composite
def valid_list(draw):
    size = draw(st.integers(min_value=1, max_value=5))
    return draw(st.lists(st.integers(), min_size=size, max_size=size))
```

使用：
```python
@given(valid_list())
def test_list(lst):
    assert len(lst) > 0
```
👉 用於：

自訂複雜資料結構
dependent data（長度依賴）

#### 7️⃣ shrinking（自動縮小錯誤）

當測試失敗：

```python
@given(st.lists(st.integers()))
def test_fail(lst):
    assert sum(lst) < 100
```

Hypothesis 會幫你找：

👉 最小失敗案例（例如 [100]）

這是它最強大的功能之一。

---
### 🧠 Property-Based Testing（PBT）

#### 核心概念

👉 測「規則」而不是「例子」

##### 傳統測試
```python
def test_sort():
    assert sorted([3,1,2]) == [1,2,3]
```
##### PBT
```python
@given(st.lists(st.integers()))
def test_sort(lst):
    result = sorted(lst)

    assert result == sorted(result)
    assert len(result) == len(lst)
```

#### 常見 Property 類型
##### 1️⃣ 不變性（Invariant）
```python
assert len(result) == len(input)
```

##### 2️⃣ idempotent（冪等）
```python
sorted(sorted(x)) == sorted(x)
```

##### 3️⃣ reversible（可逆）
```python
reverse(reverse(x)) == x
```

##### 4️⃣ consistency（一致性）
```python
min(x) <= max(x)
```

---
### 🤖 Model-Based Testing（狀態機測試）

Hypothesis 支援「狀態機測試」

👉 用來測：

- stack
- queue
- DB
- API state

---
#### 範例：Stack 測試
```python
from hypothesis.stateful import RuleBasedStateMachine, rule
from hypothesis import strategies as st

class StackMachine(RuleBasedStateMachine):

    def __init__(self):
        super().__init__()
        self.sut = []      # system under test
        self.model = []    # 正確模型

    @rule(x=st.integers())
    def push(self, x):
        self.sut.append(x)
        self.model.append(x)

    @rule()
    def pop(self):
        if self.model:
            assert self.sut.pop() == self.model.pop()

TestStack = StackMachine.TestCase
```

#### 核心概念
| 概念        | 說明   |
| --------- | ---- |
| SUT       | 被測系統 |
| model     | 正確參考 |
| rule      | 操作   |
| invariant | 永遠成立 |

#### 加 invariant
```python
from hypothesis.stateful import invariant

@invariant()
def same_length(self):
    assert len(self.sut) == len(self.model)
```

#### 🔥 PBT vs Model-Based Testing
| 類型             | 重點             |
| -------------- | -------------- |
| Property-Based | 單次 function 規則 |
| Model-Based    | 多步驟 state 行為   |

#### 🧩 實務建議（SDET 視角）

你目前做的方向其實是對的（pytest + hypothesis 👍），可以再升級：

#### 1️⃣ 測「行為」而不是「結果」

❌
```python
assert func(2) == 4
```
✅
```python
assert func(x) >= x
```

#### 2️⃣ 建立 reusable strategies
```python
user_ids = st.integers(min_value=1, max_value=10_000)
```
#### 3️⃣ 結合 CI
每次 PR 自動跑 hypothesis
找 edge case bug
#### 4️⃣ 常見踩雷

⚠️ assume() 過多 → 測試變慢
⚠️ 測試不 deterministic
⚠️ 忘記測 invariant

### 🧾 總結一句話

👉 Hypothesis =
用數學性質 + 自動生成資料 → 找出你沒想到的 bug
