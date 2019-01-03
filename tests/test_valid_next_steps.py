from solution.stairs import valid_next_steps
from nose.tools import eq_, raises


def test_when_no_steps_given_then_no_steps_valid():
    for steps_left in 0, 1, 17:
        yield eq_, valid_next_steps(steps_left, []),  []


def test_when_all_steps_are_valid_then_all_are_returned():
    assert valid_next_steps(4, [1, 2, 3, 4]) == [1, 2, 3, 4]


def test_when_some_steps_are_exceeding_staircase_they_are_not_returned():
    assert valid_next_steps(4, [1, 2, 4, 5]) == [1, 2, 4]


def test_duplicate_steps_are_dropped():
    assert valid_next_steps(2, [1, 1, 2]) == [1, 2]


def test_order_of_given_available_steps_is_not_important_when_getting_valid_next_steps():
    for expected_item in 1, 2:
        assert expected_item in valid_next_steps(2, [2, 1])
