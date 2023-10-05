#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and divisible by 2.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a divisible by 2.
xx is only a perfect square.
xx is only divisible by 2.

Example:
Enter a number: 8
8 is only divisible by 2.

Enter a number: 64
64 is both a perfect square and divisible by 2.
"""
n = int(input("Give me a number"))
if n%2==0:
    d=1 # n is disviable by two
else: 
    d=0 # n is not  disviable by two
    
import math
def perfsqr(num):
    if num < 0:
        return False
    s = math.isqrt(num)
    return s * s  

z = perfsqr(n)
if n == z:
    p=1 # n is a perfect square
else:
    p=0 #n is not a perfect square
    
if d==1 and p==1:
    print (f"{n} is both a perfect square and divisible by 2")
elif d==1 and p==0:
    print (f"{n} is only divisible by 2")
elif d== 0 and p==1: 
    print (f"{n} is only a perfect square ")
else: print(print (f"{n} is not a perfect square and not divisible by 2"))

    
