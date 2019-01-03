from solution.stairs import solution_traverses_staircase_fully


def test_a_funtion_is_returned():
    assert callable(solution_traverses_staircase_fully(0))


def test_exact_solution_matches_expectation():
    predicate = solution_traverses_staircase_fully(staircase_length=1)
    assert predicate([1]) == True


def test_too_many_steps_do_not_match_staircase():
    predicate = solution_traverses_staircase_fully(staircase_length=1)
    assert predicate([2]) == False


def test_too_few_steps_do_not_match_staircase():
    predicate = solution_traverses_staircase_fully(staircase_length=2)
    assert predicate([1]) == False
