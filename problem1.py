#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""
n = int(input("Give me a number"))
if n%6==0:
    six=1
else: six=0

if n%8==0:
    eight=1
else: eight=0 

if six==1 and eight==0:
    print (f"{n} is frue")
else: (print (f"{n} is not frue"))