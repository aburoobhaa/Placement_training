'''
QUESTION: Print the multiplication table of a given number N.

Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

'''
n = int(input())
for i in range(1, 11):
    print(n,"x",i,"=",n*i)


'''
I learned new thing here : f string 
 way to embed expressions inside string literals using curly braces {}


how to use 
Put an f or F in front of the string.
Inside {}, you can put variables, math, or function calls.
 
'''
#EXAMPLE USAGE:
name = "Alice"
age = 25
# Basic usage
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.


n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

