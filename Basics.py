'''Practice Chapter 2 and 3
Declare, assign and reassign value to a variable
'''
a=5
a=10
a=20
print(a)
b,c,d= 1,2,3
print(b,c,d)

'''Modify values using built in functions and methods'''

a=max(255,5)
print(a)

s="Hello there how are you"
print("Length of string",len(s))
print(s.upper())
print(s.lower())

'''Practice whitespace and style guidelines
'''
name="Marij Murtaza"
roll_num="123"
print(f"\tMy name is {name}\n \tMy roll number is: {roll_num}")

'''Write a function that accepts an integer n and a string s as parameters, 
and returns a string of s repeated exactly n times. Example 3, “Hello” —->>>> “HelloHelloHello”
'''
def repeat_string(n, s):
    repeated_string = s * n
    return repeated_string
repeat_string(3,'hello')

'''Given a random non-negative number, 
you have to return the digits of this number within an array in reverse
order. Example:35231 => [1,3,2,5,3]
'''
n=int(input("Enter how many numbers you want to enter:"))
arr=[]
for i in range(n):
    num= int(input("Enter a number:"))
    arr.append(num)
arr.reverse()
print('Reversed array',arr)

'''Write a function to convert a name into initials. 
This problem strictly takes two words with one space in between them
'''
def get_initials(fname,lname):
    name1=fname[0].upper()
    name2=lname[0].upper()
    return name1 + "."+ name2
print(get_initials("marij","murtaza"))

'''Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. 
You don't have to worry with strings with less than two characters. Eloquent —->>> loquen
'''
def remove_string(string):
    print(string[1:-1])
string="Eloquent"
remove_string(string)

''' You will be given an array a and a value x. All you need to do is check
whether the provided array contains the value. Return true if contains value
otherwise false.
'''
def contains_value(arr, x):
    # Check if x is in arr using the "in" operator
    if x in arr:
        return True
    else:
        return False

a = [1, 2, 3, 4, 5]
contains_value(a, 3)

'''We need a function that can transform a number (integer) into a string.
Example 100 ⇒ “100”, -100 ⇒ “-100”
'''
def transform_number(num):
    num=str(num)
    return num


print(transform_number(100))

'''Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).
'''

def ends_with(string1, string2):
    if string1.endswith(string2):
        return True
    else:
        return False
print(ends_with("100", "100"))

'''
Create a method to add, subtract, multiply, and divide. Take both number and
operator as an input from the user. Method will return the answer.
'''
def add_subtract_multiply_divide(num1, operator, num2):
     if operator == "+":
         return num1 + num2
     elif operator == "-":
         return num1 - num2
     elif operator == "*":
         return num1 * num2
     elif operator == "/":
         return num1 / num2
     

'''
Create a function that takes an integer as an argument and returns "Even" for
even numbers or "Odd" for odd numbers.
'''
def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even(100))

'''You probably know the "like" system from Facebook and other pages. People
can "like" blog posts, pictures or other items. We want to create the text that
should be displayed next to such an item. Implement the function which takes
an array containing the names of people that like an item. It must return the
display text as shown in the examples:
[] --> "no one likes this"
["Peter"] --> "Peter likes this"
["Jacob", "Alex"] --> "Jacob and Alex like this"
["Max", "John", "Mark"] --> "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"] --> "Alex, Jacob and 2 others like this"
'''
def like(array):
    if len(array) == 0:
        return "No likes this"
    elif len(array) == 1:
        return array[0] + " likes this"
    elif len(array) == 2:
        return array[0] + " and " + array[1] + " like this"
    elif len(array) == 3:
        return array[0] + " and " + array[2] + " like this"
    elif len(array) >= 4:
        return array[0] + " and " + array[3] + "like this"
print(like(["marij,sajjal,faizan"]))

    
'''Make a function that will return a greeting statement that uses an input; your
program should return, "Hello, <name> how are you doing today?".
'''
def greeting(name):
 return "Hello, " + name + " how are you doing today?"
print(greeting("marij"))

'''Write a function which returns the sum of each number squared. For example:
[1,2,3] —> 1^2 + 2^2 + 3^2 = 14'''

def square_sum(arr):
    sum=0
    for i in arr:
        sum=sum+i**2
    return sum

print(square_sum([1,2,3]))
