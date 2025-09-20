#Question: Find the sum of all primes up to N.

'''
Input: 10
Output: 17   (2+3+5+7)
'''
def is_prime(n):
    st = True
    if n <= 1: 
        return False
    else:
        for i in range(2, n//2+1):
            if (n%i == 0):
                return False
    return True  
n = int(input())
s = 0
for i in range(2,n):
    if (is_prime(i)):
        s += i
        
print(s)

'''
⚠️ Improvements:

Range: Currently you go up to n-1. If the problem statement says "up to N", then loop should be range(2, n+1).

Efficiency: Checking up to n//2 is fine for small inputs, but we can speed it up using √n instead.
'''
def is_prime(n):
    st = True
    if n <= 1: 
        return False
    else:
        for i in range(2, n//2+1):
            if (n%i == 0):
                return False
    return True  
n = int(input())
s = 0
arr = []
for i in range(2,n):
    if(n%i == 0):
        if (is_prime(i)):
            arr.append(i)
print(arr[len(arr)-1])


#version 3 
def is_prime(n):
    st = True
    if n <= 1: 
        return False
    else:
        for i in range(2, n//2+1):
            if (n%i == 0):
                return False
    return True  
n = int(input())
s = 0
lar = 2
for i in range(2,n):
    if(n%i == 0) and (is_prime(i)):
        lar = i
print(lar)


#version 4 : If the number itself is prime, your loop won’t consider it
def is_prime(n):
    st = True
    if n <= 1: 
        return False
    else:
        for i in range(2, n//2+1):
            if (n%i == 0):
                return False
    return True  
n = int(input())
s = 0
lar = 0
for i in range(2,n+1):
    if(n%i == 0) and (is_prime(i)):
        lar = i
print(lar)



