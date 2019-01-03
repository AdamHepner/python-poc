from solution.stairs import flattened


def all_solutions(solution): return True


def generated_solutions(tree): return len(list(flattened(tree, all_solutions)))


def test_empty_tree_flattened_is_empty():
    tree = {

    }
    assert generated_solutions(tree) == 0


def test_when_predicate_not_fullfilled_then_no_resuts():
    def no_solutions(solution): return False
    assert len(list(flattened({1: {}}, no_solutions))) == 0


def test_wide_tree_is_flattened_to_single_list():
    tree = {
        1: {},
        2: {}
    }
    assert generated_solutions(tree) == 2


def test_deep_tree_is_flattened_to_single_list():
    tree = {
        1: {
            2: {}
        }
    }
    assert generated_solutions(tree) == 1


def test_when_tree_is_deep_then_wide_it_is_flattened_to_single_list():
    tree = {
        1: {
            1: {},
            2: {}
        }
    }
    assert generated_solutions(tree) == 2
