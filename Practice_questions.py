"""Problem 1
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters
A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers
and punctuation."""
import string

def is_pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

string = "The quick brown fox jumps over the lazy dog"
if is_pangram(string):
    print("Yes, it is a pangram.")
else:
    print("No, it is not a pangram.")

"""Problem 2
Make number negative
In this simple assignment you are given a number and have to make it negative. But maybe the
number is already negative?
Input: -100
Input2: 0
Input3: 3
Input4: 34 """
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

# User Input
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
input3 = int(input("Enter the third number: "))
input4 = int(input("Enter the fourth number: "))

# Convert the numbers to negative numbers
result1 = make_negative(input1)
result2 = make_negative(input2)
result3 = make_negative(input3)
result4 = make_negative(input4)

# Print the resulting negative values
print(result1, result2, result3, result4)

""" Problem 3
Two to one
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest
possible, containing distinct letters - each taken only once - coming from s1 or s2.
Example
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"""

def longest(s1,s2):
    combined= set(s1).union(set(s2))
    sorted_string= "".join(sorted(combined))
    return sorted_string
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
result= longest(a, b)
print(result)

a = "abcdefghijklmnopqrstuvwxyz"
result = longest(a, a)
print(result)


"""
Problem 4
Opposite number
Very simple, given an integer or a floating-point number, find its opposite.
"""
def opposite(number):
    return -number

print(opposite(1.4))
"""Problem 5
Keep Hydrated
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of
cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded
to the smallest value.
Example
time = 3 ----> litres = 1
time = 6.7---> litres = 3
time = 11.8--> litres = 5
"""

def water(time):
    drink =0
    save = time
    drink= save // 2
    return round(drink)

print(water(3))

"""
Problem 6
You will be given an array of numbers. You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""
def sort_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    odd_numbers.sort()

    j = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = odd_numbers[j]
            j += 1

    return arr

numbers = [5, 3, 2, 8, 1, 4]
result = sort_odd_numbers(numbers)
print(result)

"""Problem 7
Given two integers a and b, which can be positive or negative, find the sum of all the
integers between and including them and return it. If the two numbers are equal return a or b."""
def sum_between(a, b):
    if a == b:
        return a

    if a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))

print(sum_between(4, 7))

"""Problem 8
Can you find the needle in the haystack? Write a function findNeedle() that takes an array
full of junk but containing one "needle" After your function finds the needle it should return a
message (as a string) that says: "found the needle at position " plus the index it found the
needle,"""

def findneedle(array):
    for index , item in enumerate(array):
        if item == "needle":
            return "found the needle at position " + str(index)
        
haystack=["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
result = findneedle(haystack)
print(result)
"""
Problem #9
Write a program that finds the summation of every number from 1 to num. The number will
always be a positive integer greater than 0.
"""
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

num = 5
mynum = summation(num)
print(mynum)

""" Problem #10
Given the triangle of consecutive odd numbers:
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
"""
def sum_of_nth_row(n):
    return n**3


row_index = 5
row_sum = sum_of_nth_row(row_index)
print("The sum of the numbers in the", row_index, "row is:", row_sum)
