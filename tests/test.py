from sorepy import recursion

def test_sum_array(array):
    """
    make sure sum_array works correctly
    """

    assert recursion.sum_array([8,5,1,4,7,6]) == 31, 'incorrect'
    assert recursion.sum_array([6,5,2,1]) == 14, 'incorrect'

def test_fibonacci(n):
    """
    make sure fibonacci works correctly
    """

    assert recursion.fibonacci(8) == 13, 'incorrect'
    assert recursion.fibonacci(5) == 3, 'incorrect'

def test_factorial(n):
    """
    make sure factorial works correctly
    """

    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(8) == 40320, 'incorrect'

def test_reverse(array):
    """
    make sure reverse works correctly
    """

    assert recursion.reverse("Hello") == "olleH", 'incorrect'
    assert recursion.sum_array("Cell") == "lleC", 'incorrect'

from sorepy import sorting
