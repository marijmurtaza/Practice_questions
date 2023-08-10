#Declare, assign and reassign value to a variable
a=10
b=a
print(b)

'''Modify values using built in functions and methods'''
a=255
b=45
print(max(a,b))

str="Hello my name is Marij"
print(len(str))
print(str.upper())

'''Practice whitespace and style guidelines'''
name="Marij Murtaza"
roll_num="1234"
print(f"\tMy name is {name}\n \tMy roll number is: {roll_num}")

'''Write a function that accepts an integer n and a string s as parameters, 
and returns a string of s repeated exactly n times. Example 3, “Hello” —->>>> “HelloHelloHello”
'''
def repeat_string(n,s):
    n=int(input("Enter a number"))
    repeated_string=s*n
    return repeated_string
repeat_string("n","Hello")
    

'''Given a random non-negative number, 
you have to return the digits of this number within an array in reverse
order. Example:35231 => [1,3,2,5,3]'''

def return_array(a,b,c,d,e):
    arr=[a,b,c,d,e]
    arr.reverse()
    return arr
result=return_array(3,5,2,3,1)
print(result)

'''Write a function to convert a name into initials. 
This problem strictly takes two words with one space in between them'''

def initials(fname,lname):
   name1=fname[0]
   name2=lname[0]
   return name1 + "."+ name2
names=initials("Marij","Murtaza")
print(names)

'''Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. 
You don't have to worry with strings with less than two characters. Eloquent —->>> loquen
'''
def remove(str):
    return str[1:-1]
remove_str=remove("Eloquent")
print(remove_str)
   
''' You will be given an array a and a value x. All you need to do is check
whether the provided array contains the value. Return true if contains value
otherwise false.'''

def check_array(x):
    arr=[1,2,3,4,5,6]
    if x in arr:
        return True
    else:
        return False

print(check_array(5))

'''We need a function that can transform a number (integer) into a string.
Example 100 ⇒ “100”, -100 ⇒ “-100”
'''
def transform_number(num):
    num_str = str(num)
    return num_str

print(transform_number(100))
print(transform_number(-100))

'''Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).
'''
def check(str1,str2):
    if str1.endswith(str2):
        return True
    else:
        return False
    
print(check("100","100"))

'''Create a method to add, subtract, multiply, and divide. Take both number and
operator as an input from the user. Method will return the answer.'''
def calculator(number1,number2,operator):
 if operator =="+":
     return number1+number2
 elif operator == "-":
     return number1-number2
 elif operator == "*":
     return number1*number2
 elif operator == "/":
     return number2/number1
 else:
     print("Invalid operator")

"""Create a function that takes an integer as an argument and returns "Even" for
even numbers or "Odd" for odd numbers."""

def even_odd(num):
    if num%2==0:
        return "Is even"
    else: 
        return "Is odd"
   
print(even_odd(4))

"""You probably know the "like" system from Facebook and other pages. People
can "like" blog posts, pictures or other items. We want to create the text that
should be displayed next to such an item. Implement the function which takes
an array containing the names of people that like an item."""

def like(array):
    if len(array) == 0:
        return "No likes this"
    elif len(array) == 1:
        return array[0] + " likes this"
    elif len(array) == 2:
        return array[0] + " and " + array[1] + " like this"
    elif len(array) == 3:
        return array[0] + "," +array[1] + " and " + array[3] + " like this"
    else:
        return array[0] +  " and " + array[1]  +  "and 2 others like this"
print(like(["marij","sajjal","faizan","Ali"]))


'''Make a function that will return a greeting statement that uses an input; your
program should return, "Hello, <name> how are you doing today?".
'''
def greeting(name):
    return  "Hello, "+ name+" how are you doing today?"

print(greeting(input("Enter your name :")))
                    
"""Write a function which returns the sum of each number squared. For example:
[1,2,3] —> 1^2 + 2^2 + 3^2 = 14"""

def sum_square(arr):
    sum=0
    for x in arr:
        sum= sum + x**2

    return sum


print(sum_square([1,2,3]))
