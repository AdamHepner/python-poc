from solution.stairs import get_solutions


def test_no_solutions_for_no_stairs():
    assert [] == get_solutions(0, [1])


def test_no_solutions_for_no_steps():
    assert [] == get_solutions(1, [])


def test_solutions_for_problem_example():
    solutions = get_solutions(4, [1, 2])
    expected_solutions = [
        [1, 1, 1, 1],
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
        [2, 2]
    ]
    assert len(expected_solutions) == len(solutions)
    for solution in expected_solutions:
        assert solution in solutions
