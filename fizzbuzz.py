"""
Problem:

    FizzBuzz is a counting game. Players take turns counting the next number
    in the sequence 1, 2, 3, 4 ...  However, if the number is:

    * A multiple of 3 -> Say 'Fizz' instead
    * A multiple of 5 -> Say 'Buzz' instead
    * A multiple of 3 and 5 -> Say 'FizzBuzz' instead
    
    The function fizzbuzz should take a number and print out what the player
    should say.

Tests:

    >>> fizzbuzz(7)
    7
    >>> fizzbuzz(10)
    Buzz
    >>> fizzbuzz(12)
    Fizz
    >>> fizzbuzz(30)
    FizzBuzz

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this function
def fizzbuzz(n):

    if n % 3 == 0 and n % 5 ==0:
        
     print ("FizzBuzz")

    elif n % 3 == 0:
        print("Fizz")

    elif n % 5 == 0:
        print("Buzz")

    else:
        print(n)
        
