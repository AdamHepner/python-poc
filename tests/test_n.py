from solution import stairs
from nose.tools import raises 

def test_N_equal_0():
    """
    When there are no stairs to be climbed, then there are 0 steps to be made

    0 steps can be done in 1 unique way
    """
    assert 1 == stairs.count_combinations(stairs_count=0)

def test_invalid_N():
    @raises(ValueError)
    def check_invalid_argument_exception(invalid_number_of_steps):
        """
        when an invalid number of steps is given as a parameter, it should result in an exception
        """
        stairs.count_combinations(invalid_number_of_steps)

    for n in [None, -1, "1"]:
        yield check_invalid_argument_exception, n

