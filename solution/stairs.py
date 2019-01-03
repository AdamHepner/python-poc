#!/usr/bin/env python

import logging
from argparse import ArgumentParser, ArgumentTypeError


def valid_next_steps(stairs_left, allowed_steps):
    """
    return only those steps from given set that actually can be taken
    """

    return [step for step in set(allowed_steps) if step <= stairs_left]


def span_possible_tree(stairs_left, allowed_steps):
    """
    Create a spanning tree of all the ways that I can take allowed steps that result in taking a number of steps
    less or equal to the stairs in the staircase

    The resulting tree contains all the solutions with which I do *not* exit the staircase.
    Upon further analysis, the invalid solutions must be removed.
    Alternative solution would be to constantly check if a solution is achievable while spaning the solution tree
    """
    next_steps = valid_next_steps(stairs_left, allowed_steps)
    return {steps_taken: span_possible_tree(stairs_left - steps_taken, next_steps) for steps_taken in next_steps}


def flattened(spanning_tree, predicate, collected_results=[]):
    """
    traverse the given spanning tree in a way that allows me to get a list of all steps 
    """
    for element, subtree in spanning_tree.iteritems():
        if subtree:
            for flattened_subtree in flattened(subtree, predicate, collected_results + [element]):
                yield flattened_subtree
        else:
            solution = collected_results + [element]
            if predicate(solution):
                yield solution


def solution_traverses_staircase_fully(staircase_length):
    """
    A predicate that allows getting only valid solutions to the counting problem

    Alternatively, you could provide a predicate that allows e.g. only ways to climb the staircase using odd number of steps
    """
    return lambda solution: sum(solution) == staircase_length


def get_solutions(staircase, steps):
    possible_tree = span_possible_tree(staircase, steps)
    return list(flattened(
        possible_tree, solution_traverses_staircase_fully(staircase)))


def count_solutions(staircase, steps, solutions_list=None):
    if solutions_list != None:
        return len(solutions_list)
    if not isinstance(staircase, int):
        raise TypeError("staircase length must be an integer")
    if staircase <= 0:
        raise ValueError("staircase must have at least one step")
    for step in steps:
        if not isinstance(step, int):
            raise TypeError("list of allowed steps must contain only integers")
        if step <= 0:
            raise ValueError("All steps must be positive")
    all_solutions = flattened(span_possible_tree(
        staircase, steps), solution_traverses_staircase_fully(staircase))
    return sum(1 for solution in all_solutions)


def int_greater_than(lower_limit):
    def _int_greater_than(value):
        try:
            int_value = int(value)
        except ValueError:
            raise ArgumentTypeError("{} is not a proper integer".format(value))
        if int_value <= lower_limit:
            raise ArgumentTypeError(
                "{} is not allowed, should be greater than {}".format(value, lower_limit))
        return int_value
    return _int_greater_than


if __name__ == "__main__":
    logging.basicConfig(filename='stairs.log',
                        filemode='w', level=logging.DEBUG)

    logger = logging.getLogger("main")
    parser = ArgumentParser(description="Counts how many ways to climb stairs")
    parser.add_argument("stairs", metavar="N",
                        help="number of steps to climb", type=int_greater_than(0))
    parser.add_argument("steps", metavar="X",
                        help="allowed lengths of steps", type=int_greater_than(0), nargs="+")
    parser.add_argument("--show-solutions",  dest="show_solutions",
                        action="store_true", help="display calculated possible step combinations")
    parser.add_argument("--no-count-solutions",  dest="count_solutions",
                        action="store_false", default=True, help="skip counting possible solutions")
    arguments = parser.parse_args()

    logger.info("Parsed the following arguments: %s", arguments)
    possible_tree = span_possible_tree(
        arguments.stairs, arguments.steps)
    logger.debug("Calculated the following spanning tree: %s", possible_tree)

    precalulated_solutions = get_solutions(
        arguments.stairs, arguments.steps) if arguments.show_solutions else None
    if arguments.show_solutions:
        print "Possible solutions: \n%s" % (precalulated_solutions)
    if arguments.count_solutions:
        print "Number of ways to climb a staircase of {stairs_count} stairs using steps {allowed_steps} is: {}".format(
            count_solutions(arguments.stairs, arguments.steps, precalulated_solutions), stairs_count=arguments.stairs, allowed_steps=arguments.steps)
