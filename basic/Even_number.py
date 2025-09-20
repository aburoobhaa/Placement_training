# Questions:  Print only the even numbers from 1 to N.
n = int(input())
for i in range(0, n,2):
    print(i+2, end=" ")
#Output: 2 4 6 8 10


n = int(input())
for i in range(1,n+1):
    if(i%2==0):
        print(i, end=" ")
#Output: 2 4 6 8 10


n = int(input())
for i in range(2, n+1,2):
    print(i, end=" ")
#Output: 2 4 6 8 10

'''
Note:
if n+1 is removed, n(if even) will not be included, check y? (😉 play with the code to learn) 
and also why range is differen t in each code? check it also 
