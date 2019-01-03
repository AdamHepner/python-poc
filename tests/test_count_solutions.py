from solution.stairs import count_solutions
from nose.tools import raises, nottest

invalid_staircases = 0, -1, None, "abc"
invalid_step_sequences = [-1], None, "abc", [0]


def test_there_are_no_solutions_when_solution_list_is_empty():
    assert 0 == count_solutions(None, None, solutions_list=[])


@nottest
def is_invalid_staircase(staircase):
    try:
        assert count_solutions(staircase, [1])
    except ValueError:
        pass
    except TypeError:
        pass


@nottest
def is_invalid_step_sequence(step_sequence):
    try:
        assert count_solutions(1, step_sequence)
    except ValueError:
        pass
    except TypeError:
        pass


def test_invalid_staircase_are_not_allowed():
    for staircase in invalid_staircases:
        yield is_invalid_staircase, staircase


def test_invalid_step_sequences_are_not_allowed():
    for steps in invalid_step_sequences:
        yield is_invalid_step_sequence, steps


def test_if_solution_sequence_is_given_then_other_params_are_ignored():
    assert 0 == count_solutions(1, [1], [])


def test_example_from_problem_description():
    assert 5 == count_solutions(4, [1, 2])
