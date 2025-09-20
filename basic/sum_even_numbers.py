#Question: Can you try printing the sum of only even numbers from 1 to N?
n = int(input())
tot = 0
for i in range(2,n+1,2):
    tot +=i
print(tot)

'''
TRICK : 
The sum of first  k even numbers is:
               
               Sum=k×(k+1)
               
(Where k=n//2).

How :
First k even numbers: 2, 4, 6, ..., 2k

Sum:
= 2 + 4 + 6 + .... 2k
= 2(1 + 2 + ... + k)  
= 2 * [k(k+1)/2]  
= k(k+1)

Formula: Sum = k × (k+1) 
(where k = n // 2)
'''


n = int(input())
k = n // 2
print(k * (k + 1))
