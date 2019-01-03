from solution import stairs
from nose.tools import eq_, istest


@istest
def duplicate_entries_in_available_next_steps_are_dropped():
    assert 2 == len(stairs.valid_next_steps(2, [1, 1, 2]))


@istest
def spanning_tree_is_empty_if_no_steps_available():
    assert {} == stairs.span_possible_tree(1, [])


@istest
def spanning_tree_has_single_element_if_one_step_available():
    assert {1: {}} == stairs.span_possible_tree(1, [1])


@istest
def spanning_tree_goes_deep_if_multiple_stairs_available_but_only_single_step_allowed():
    assert {1: {1: {}}} == stairs.span_possible_tree(2, [1])


@istest
def spanning_tree_goes_wide_if_multiple_ways_possible():
    assert {1: {1: {}}, 2: {}} == stairs.span_possible_tree(2, [1, 2])
