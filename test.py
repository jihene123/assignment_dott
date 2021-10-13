import numpy as np
from main import solve


def test_example1():
    exp = np.array([[1]])
    result = solve(exp, exp.shape[0], exp.shape[1])
    assert np.array_equal(result, np.array([[0]]))


def test_example2():
    exp = np.array([[0, 0, 0, 1],
                    [0, 0, 1, 1],
                    [0, 1, 1, 0]])
    result = solve(exp, exp.shape[0], exp.shape[1])
    assert np.array_equal(result, np.array([[3, 2, 1, 0],
                                            [2, 1, 0, 0],
                                            [1, 0, 0, 1]]))


def test_example3():
    exp = np.array([[1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])
    result = solve(exp, exp.shape[0], exp.shape[1])
    assert np.array_equal(result, np.array([[0, 0, 0, 0],
                                            [1, 1, 1, 1],
                                            [2, 2, 2, 2],
                                            [3, 3, 3, 3],
                                            [4, 4, 4, 4]]))


def test_example4():
    exp = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])
    result = solve(exp, exp.shape[0], exp.shape[1])
    assert np.array_equal(result, np.array([[5, 4, 3, 2, 1],
                                            [4, 3, 2, 1, 0],
                                            [5, 4, 3, 2, 1],
                                            [6, 5, 4, 3, 2],
                                            [7, 6, 5, 4, 3]]))

