'''
Write a function to check if a string is a palindrome (same forward and backward).
Example:
    "madam" → True
    "hello" → False
'''
st = input()
print(st[::-1])
#output: madAM  ------> Input MAdam

s = []
for i in st:
    print(i)
    s.append(i)
print(s)
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")


'''
What I have learned :
list : 0, 1, 2 , 3... n ==> the loop stops at n-1 
if reversed: n -1, n-2,......... 2, 1, 0, -1

so if the reverse loop will start at len(string)-1, ends at -1, by -1 step 
'''
