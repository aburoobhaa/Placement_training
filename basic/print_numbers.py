## QUESTION: can you write a Python program that prints all numbers from 1 to 10? (Just simple loop — no tricks.)

#Prints numbers 1 to 9, each on a new line.
for i in range(1, 10):
    print(i)


#Prints numbers 1 to 9 in the same line, separated by spaces.
for i in range(1, 10):
    print(i, end=" ")

#Can you try writing a program that prints numbers from 1 to N, where N is given by the user?
n = int(input())
for i in range(1, n+1):
    print(i, end=" ")

#Print the numbers from N down to 1 (reverse order).
n = int(input())
for i in range(0, n):
    i = n-i
    print(i, end=" ")

#DIFFERENT VERSION I 'VE TRIED 
n = int(input())
#FOR LOOP WORKS  AS -> range(start, end, step(like how many move))
for i in range(n, 0, -1):
    print(i, end=" ")
