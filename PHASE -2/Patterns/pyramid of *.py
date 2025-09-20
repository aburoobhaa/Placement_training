# Question : Print a pyramid of *.

# Wrong 1
n = int(input())
for i in range(1, n+1): 
    print(" "*(i-1) + "*"*(2*i-1)) #-------------------->  i-1 on space 
'''
output
*
 ***
  *****
   *******
    *********
'''

# Wrong 2 
n = int(input())
for i in range(1, n+1):
    print(" "*(n-1) + "*"*(2*i-1)) #-------------------->  n-1 on space 

'''
output
    *
    ***
    *****
    *******
    *********
'''


#Finally 

n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

'''
output:
    *
   ***
  *****
 *******
*********
'''


# note: Space: 4,3,2,1,0 (n-i) i = 1,2,3,4...
# * : 1,3,5,7... (2i-1) 

