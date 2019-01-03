# Problem statement

 There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X. 

Problem found here: https://www.dailycodingproblem.com/ , apparently was asked by Amazon.

# Solution proposition

I attempt to solve the generalized case.

Rough idea here is: in order to climb the staircase with N steps, I have to take some steps and climb the rest of the staircase. Classic CS :)

So, in order to achieve the result, I have to traverse a spanning tree of possible ways to climb the staircase. There are most possible ways to do it without generating the whole thing in memory, but a) none came to my mind and b) I got bit sidetracked with the presentation of possible solutions, so I implemented it as well.

The spanning tree for example given in problem description is as following:

- (no steps taken)
  - 1 step taken
    - 1 step taken
      - 2 steps taken
      - 1 step taken
        - 1 step taken
    - 2 steps taken
      - 1 steps taken
  - 2 steps taken
    - 2 steps taken
    - 1 step taken
      - 1 step taken


If I drop the initial "no steps taken" level, the tree becomes a forest, and is somewhat easily representable as a built-in dict, where each key represents the step taken, and each value represents a spanning subtree, ie. all the ways in which I can traverse remaining stairs.

When traversing the spanning tree in depth, you get a sample possible solution to the stated problem, however there is no guarantee that it is an actual solution, because while spanning the tree it had not been taken care of to remove invalid solutions.

The way to circumvent it is as following: traverse the tree, but return only the possible solutions that conform to given predicate.

The most complex part for me had been to traverse the tree and return a flat list of solutions, but in the end the (almost) correct solution had been to use recursive generators.

# Techniques used

I wanted to showcase some of the Python features that I am familiar with:

- list, generator and dictionary comprehension
- generator usage
- currying (returning funtion from a function)
- lambdas
- logging and argument parsing, ie what is provided by Python
- testing using Nosetest library
- virtualenv

And additionally - familiarity with CS problems and problem solving techniques.

# Known issues

Apparently, when trying to obtain a flat list of possible solutions, if there is only a single solution, the '''flattened''' funtion will return invalidly contrued data structure, ie ```[1]``` instead of ```[[1]]```

# Prerequisites

- Python 2.17
- PIP

# Installation

Instal Virtualenv

```bash
pip install virtualenv
```

Create and activate virtual environment

```bash
virtualenv venv
. venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```