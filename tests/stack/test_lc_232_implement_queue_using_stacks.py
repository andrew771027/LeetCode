from collections import deque
from typing import List

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from src.stack.lc_232_implement_queue_using_stacks import MyQueue


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 1, 1, False],
        ),
    ],
)
def test_normal_case_1(ops, args, expected_result):
    obj = None
    actual_result = []

    for op, arg in zip(ops, args):
        if op == "MyQueue":
            obj = MyQueue()
            actual_result.append(None)
        elif op == "push":
            actual_result.append(obj.push(*arg))
        elif op == "pop":
            actual_result.append(obj.pop())
        elif op == "peek":
            actual_result.append(obj.peek())
        elif op == "empty":
            actual_result.append(obj.empty())

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 1, 1, False],
        ),
        (
            ["MyQueue", "push", "pop", "empty"],
            [[], [5], [], []],
            [None, None, 5, True],
        ),
    ],
)
def test_normal_case_2(ops, args, expected_result):

    obj = None
    actual_result = []

    for op, arg in zip(ops, args):
        if op == "MyQueue":
            obj = MyQueue()
            actual_result.append(None)
        else:
            method = getattr(obj, op)
            actual_result.append(method(*arg) if arg else method())

    assert actual_result == expected_result


def run_ops(ops, args) -> List:
    obj = None
    result = []

    for op, arg in zip(ops, args):
        if op == "MyQueue":
            obj = MyQueue()
            result.append(None)
        else:
            method = getattr(obj, op)
            result.append(method(*arg) if arg else method())

    return result


@pytest.mark.parametrize(
    "ops, args, expected_result",
    [
        (
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 1, 1, False],
        ),
        (
            ["MyQueue", "push", "pop", "empty"],
            [[], [5], [], []],
            [None, None, 5, True],
        ),
    ],
)
def test_noraml_case_3(ops, args, expected_result):
    assert run_ops(ops, args) == expected_result


@settings(max_examples=100)  # 預設約 100，可調整
@given(values=st.lists(st.integers(), max_size=20))
def test_normal_case_4(values):
    my_queue = MyQueue()
    system_queue = deque()

    for v in values:
        my_queue.push(v)
        system_queue.append(v)

    while system_queue:
        assert my_queue.peek() == system_queue[0]
        assert my_queue.pop() == system_queue.popleft()

    assert my_queue.empty() == (len(system_queue) == 0)
