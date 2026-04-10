from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        pop_value: int = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return pop_value

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_value: int = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.push(top_value)
        return top_value

    def empty(self) -> bool:
        return len(self.q1) == 0
