""" Write a Python function to find the maximum of three numbers."""
def maximum(a,b,c):
    maximum=max(a,b,c)
    return maximum

print(maximum(1,2,3))

"""Write a Python function to sum all the numbers in a list."""
def sum(numbers):
    total=0
    for num in numbers:
        total = num+total
    return total

print(sum([8, 2, 3, 0, 7])) 

"""Write a Python function to multiply all the numbers in a list."""
def multiply(numbers):
    mul=1
    for num in numbers:
        mul=mul*num
    return mul

print(multiply([8, 2, 3, -1, 7]))

"""Write a Python program to reverse a string."""
def rev(string):
    return string[::-1]

print(rev("Hello"))

"""Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument."""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

"""Write a Python function that accepts a string and counts the number of upper and lower case letters."""
def count(string):
    up=0
    low=0
    for char in string:
        if char.isupper():
            up=up+1
        elif char.islower():
            low=low+1
    return up,low

print(count("Hello"))






        

