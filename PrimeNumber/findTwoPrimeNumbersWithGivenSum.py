"""
    Problem: 
        -Input: Given a Even Sum: S (S > 2, S is Integer)
        -Output: Two Prime Numbers with sum they equal S
        -Example 1:     Input: 5
                        Ouput: 2 3
        -Example 2:     Input: 74
                        Output:  3 71
        (Print only first such pair)
    Idea:
        -The first, please read Goldbach's conjecture
        (https://en.wikipedia.org/wiki/Goldbach's_conjecture)
        Summary: Every even integer greater than 2 can be expressed as the sum of two primes
        -Continue, we can find all prime numbers less than or equal to S using Sieve of Eratosthenes
        or Segment Sieve (if S is huge number)
        -Finaly, we can traverse through this array to find pair with given S
        ***Sieve of Eratosthenes and Segment Sieve, please see at "FindAllPrimeNumbersSmallerToN.py"
"""
from FindAllPrimesSmallerToN import *
# FUNCTION FIND Two Prime Numbers WITH SUM THEY EQUAL TO S
def Find2Prime(n):
    # Generating primes using Sieve Of Eratosthenes
    prime = SieveOfEratosthenes(n)
    # Generating primes using Segment Sieve
    # prime = SegmentSive(n)
    # Traversing all numbers to find first pair
    for i in range(len(prime)):
        diff = n - prime[i]
        if (diff in prime):
            print(prime[i], diff)
            return
#Test program
Find2Prime(17454544)

###--------------CycTrung-------------###
###--------All Code is Garbage--------###
###-----------bit.ly/YTBcyc-----------###
