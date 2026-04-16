import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_one_element_in_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)

    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_stack_is_empty_on_creation():
    cut = CustomStack(5)

    assert cut.is_empty() == True
    assert cut.size() == 0


def test_pop_returns_last_pushed_element():
    cut = CustomStack(5)
    cut.push(10)
    cut.push(20)

    result = cut.pop()

    assert result == 20
    assert cut.size() == 1


def test_pop_raises_stack_empty_exception_when_empty():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_raises_stack_empty_exception_when_empty():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.top()


def test_push_raises_stack_full_exception_when_full():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)

    with pytest.raises(StackFullException):
        cut.push(3)
