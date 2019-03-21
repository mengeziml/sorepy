def sum_array(array):
    """Return the sum of all items in an array.

        Args:
            array: list or array-like object containing numerical values.

        Returns:
            array: sorted in ascending order.

        Examples:
            >>> sum_array([1,2,3,4,5,6,7])
            28
    """
    if len(array)== 0:
        return 0
    else:
        return array[0]+sum_array(array[1:])



def fibonacci(n):
    """Return nth term in fibonacci sequence.

        Args:
            n (int): nth term in fibonacci sequence to calculate

        Returns:
            int: nth term of fibonacci sequence,
             equal to sum of previous two terms

        Examples:
            >>> fibonacci(5)
            3
      """

    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    """Return product of all positive integers less than or equal to n.

        Args:
            n (int): calculate the factorial of n

        Returns:
            Returns a product of all positive integers
            less than or equal to n!

        Examples:
            >>> factorial(8)
            40320
    """
    if n<1:
        return 1
    else:
        f = n * factorial(n-1)
        return f

def reverse(word):
    """Return string in reveresed order.

        Args:
            word (str): string to be reveresed

        Returns:
            str: string/word in reverse order

        Examples:
            >>> reverse("Hello")
            olleH
    """
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
