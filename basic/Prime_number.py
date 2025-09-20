# Question: Check if a number N is prime.
'''i know it is wrong '''

n = int(input())
for i in range(2,n//2):
    if(n%i==0):
        print("Prime")
    else:
        print("Not Prime") 

'''
What went wrong in your code:
You’re printing inside the loop — so it prints "Prime"/"Not Prime" many times.

Your logic is flipped:

If n % i == 0, that means the number is not prime.

If no divisor is found at all, only then it’s prime.

Your loop range should go up to n//2 + 1 (or better, up to √n) — since any factor of n must be ≤ n//2.
'''

n = int(input())
st = True
if n <= 1: 
  return False
else:
  for i in range(2, n):
      if (n%i == 0):
          return False
return True 
if (st):
  print("Prime")
else:
  print("Not")

