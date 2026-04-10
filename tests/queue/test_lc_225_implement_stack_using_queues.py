from typing import List

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, precondition, rule

from src.queue.lc_225_implement_stack_using_queues import MyStack


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 2, 2, False],
        ),
    ],
)
def test_normal_case_1(ops, args, expected_result):

    obj = None
    actual_result = []

    for op, arg in zip(ops, args):
        if op == "MyStack":
            obj = MyStack()
            actual_result.append(None)
        elif op == "push":
            actual_result.append(obj.push(*arg))
        elif op == "top":
            actual_result.append(obj.top(*arg))
        elif op == "pop":
            actual_result.append(obj.pop(*arg))
        elif op == "empty":
            actual_result.append(obj.empty())

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 2, 2, False],
        ),
        (
            ["MyStack", "push", "pop", "empty"],
            [[], [5], [], []],
            [None, None, 5, True],
        ),
    ],
)
def test_normal_case_2(ops, args, expected_result):

    obj = None
    actual_result = []

    for op, arg in zip(ops, args):
        if op == "MyStack":
            obj = MyStack()
            actual_result.append(None)
        else:
            method = getattr(obj, op)
            actual_result.append(method(*arg) if arg else method())

    assert actual_result == expected_result


def run_ops(ops, args) -> List:
    obj = None
    result = []

    for op, arg in zip(ops, args):
        if op == "MyStack":
            obj = MyStack()
            result.append(None)
        else:
            method = getattr(obj, op)
            result.append(method(*arg) if arg else method())
    return result


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 2, 2, False],
        ),
        (
            ["MyStack", "push", "pop", "empty"],
            [[], [5], [], []],
            [None, None, 5, True],
        ),
    ],
)
def test_normal_case_3(ops, args, expected_result):
    assert run_ops(ops, args) == expected_result


@settings(max_examples=100)
@given(values=st.lists(st.integers(), max_size=20))
def test_normal_case_4(values):

    my_stack = MyStack()
    system_stack = []

    for v in values:
        my_stack.push(v)
        system_stack.append(v)

    while system_stack:
        assert my_stack.top() == system_stack[-1]
        assert my_stack.pop() == system_stack.pop()

    assert my_stack.empty() == (len(system_stack) == 0)


class StackStateMachine(RuleBasedStateMachine):

    def __init__(self):
        super().__init__()

        self.sut = MyStack()

        self.model: List = []

    # --- push ---
    @rule(x=st.integers())
    def push(self, x):
        self.sut.push(x)
        self.model.append(x)

    # --- pop ---
    @rule()
    @precondition(lambda self: len(self.model) > 0)
    def pop(self):
        assert self.sut.pop() == self.model.pop()

    # --- top ---
    @rule()
    @precondition(lambda self: len(self.model) > 0)
    def top(self):
        assert self.sut.top() == self.model[-1]

    # --- empty ---
    @rule()
    def empty(self):
        assert self.sut.empty() == (len(self.model) == 0)


TestStack = StackStateMachine.TestCase
