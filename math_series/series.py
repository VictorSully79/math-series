


def fibonacci(n):

    """ In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, the Fibonacci sequence, 
    in which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1.

    n represents an integer and will return the nth number in the sequence """

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def lucas(n):
    """ Lucas Numbers, much like the Fibonacci sequence only it starts with the values of 2 and 1."""

    if n < 0:
        return 0 
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, num1 = 0, num2 = 1):
    """ This function will produce Fibonacci or Lucas numbers depending on the starting values """

    if n < 0:
        return 0
    elif n == 0:
        return num1
    elif n == 1:
        return num2  
    else:
        return sum_series(n - 1, num1, num2) + sum_series(n - 2, num1, num2)