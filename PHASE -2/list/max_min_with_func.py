'''
Write a Python function that finds the maximum and minimum element in a list without using max() or min().

👉 Example:
Input: [4, 1, 9, 2, 7]
Output: min = 1, max = 9
'''
l = list(input().strip().split())
#print(l)
l.sort()
print(f" min = {l[0]}, max = {l[len(l)-1]}")

'''
learned the use of .split()

when i used list(input()) -> took the spaces too 
            list(input().strip()) -> make the gap as a element
            list(input().strip().split()) -> correct as list 

'''
