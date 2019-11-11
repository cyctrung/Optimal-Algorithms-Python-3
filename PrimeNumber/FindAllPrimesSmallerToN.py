"""
    Problem: Given a number n, print all primes smaller than or equal to n
            Example:
                -Input: 20
                -Ouput: 2 3 5 7 11 13 17 19
    Idea:   Using Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
            Summary:
            1.  Create a list of consecutive intergers from 2 thround n: (2,3,4,...,n)
            2.  Initially, let p equal 2, the smallest prime number
            3.  Enumerate the multiples of p by counting in increments of p from 2p to n,
                and mark them in the list (these wil be 2p, 3p, 4p...; the p itself should 
                not be marked)
            4.  Find the first number greater than p in the list that is not marked.
                If there was no such number, stop. Otherwise, let p now equal this new number
                (which is the next prime), and repeat from step 3
            5.  When the algorithm terminates, the numbers remainning not marked in the list
                are all the primes below n
    -------------------------------------------------------------------------------------------            
    ***OH NO!!! THAT'S NOT GREAT. WHY?
    WITH A HUGE NUMBER. HOW MUCH MEMORY DO WE NEED TO PROVIDE?
    LET'S TRY: N = 1 BILLION, CORRESPONDING TO 1 * 8 MILLION BYTES
    SO WE NEED ABOUT 8GB MEMORY....
    TOO WASTE!!!***
    ------------------------------------------------------------------------------------------
            Using Segmented Sive (It is introduced in the Sieve of Eratosthenes document above)
            (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
            Summary:
            1.  Divide the range 2 through n into segments of some size Δ ≤ √n.
            2.  Find the primes in the first (i.e. the lowest) segment, using the regular sieve.
            3.  For each of the following segments, in increasing order, with m being 
                the segment's topmost value, find the primes in it as follows:
                3.1. Set up a Boolean array of size Δ
                3.2. Eliminate from it the multiples of each prime p ≤ √m found so far,
                    by calculating the lowest multiple of p between m - Δ and m, 
                    and enumerating its multiples in steps of p as usual, 
                    marking the corresponding positions in the array as non-prime.
"""
### FUNCTION SIEVE OF ERATOSTHENES
def SieveOfEratosthenes(n: int):
    # Step 1: Create a list of consecutive intergers from 2 thround n: (2,3,4,...,n)
    isPrime = [True for i in range(n+1)]
    isPrime[0] = isPrime[1] = False
    # Step 2: Initially, let p equal 2, the smallest prime number
    p = 2
    # Step 3,4: Starting from 2*p, count up in increments of p and mark
    while(p*p <= n):
        if(isPrime[p] is True):
            # Mark False all multiples of p
            for i in range(2*p, n+1, p):
                isPrime[i] = False
        # Increase p to find the next Prime number
        p += 1
    # Step 5:
    # If you wanna print all Primes from [x,n]
    # Let's change "range(n+1)" to "range(x,n+1)"
    prime=[]
    for i in range(n+1):
        if isPrime[i] is True:
            prime.append(i)
            #print(i)
    return prime

### FUNCTION SEGMENT SIVE
import math
# Prime store Prime numbers from [0,√n], next_prime store Prime numbers from [√n,n]
prime = []
next_prime=[]
# Function RegularSieve is also SieveOfEratosthenes
def RegularSieve(n):
    global prime
    isPrime = [True for i in range(n+1)]
    isPrime[0] = isPrime[1] = False
    p = 2
    while(p*p <= n):
        if(isPrime[p] is True):
            for i in range(2*p, n+1, p):
                isPrime[i] = False
        p += 1
    for i in range(n+1):
        if isPrime[i] is True:
            # Store them in prime
            prime.append(i)

def SegmentSive(n):
    global prime
    global next_prime
    # Calculator Δ ≤ √n
    limit = int(math.floor(math.sqrt(n)) + 1)
    # Step 1: Divide the range 2 through n into segments of some size Δ 
    low = limit
    hight = limit*2
    # Step 2: Find the primes in the first segment, using the regular sieve
    RegularSieve(limit)
    # Step 3: Process one segment at a time  
    while(low < n):
        if hight > n:
            hight = n
        #Step 3.1: Set up a Boolean array of size Δ
        isPrime = [True for i in range(limit+1)]
        #Step 3.2:
        for i in range(len(prime)):
            # Find the minium number in [low..hight] that is a multiple of prime[i]
            low_limit = int(math.floor(low / prime[i]) * prime[i])
            if low_limit < low:
                low_limit += prime[i]
            # Mark multiples of prime[i] in [low..high]:
            for j in range(low_limit,hight,prime[i]):
                isPrime[j-low]=False
        # Numbers which are not marked as False are prime
        # Store them to next_prime       
        for i in range(low,hight):
            if isPrime[i-low] is True:
               next_prime.append(i)
        # Update low and high for next segment      
        low=low + limit
        hight = hight + limit
    #Merge prime and next_prime into 1
    prime+=next_prime
    next_prime.clear()
    # #Print Primes number
    # for each in prime: 
    #     print(each)
    return prime
###--------------CycTrung-------------###
###--------All Code is Garbage--------###
###-----------bit.ly/YTBcyc-----------###
