"""
Idea:
    -Case 1: Number <=1 are not Prime
    -Case 2: Number <=3 (except Case 1) are Prime (This is 2 and 3)
    -Case 3: Numbers <25 if It % 2 or 3 !=0 are Prime
             This is 5,7,11,13,17,19,23)
    Notice that 5, 7, 11, 13, 17, 19, 23 can analyzed
    5, 5+2, 5+6 = 11, 11+2, 11+6 = 17, 17+2, 17+6 = 23
    So if Numbers from 25 to 121 %5 or 7 !=0 are Prime
    And Continue Number from 121 to 17^2 %11 or 13 !=0 are Prime
    .....
"""
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        print(i)
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i+=6
    return True
###--------------CycTrung-------------###
###--------All Code is Garbage--------###
###-----------bit.ly/YTBcyc-----------###
