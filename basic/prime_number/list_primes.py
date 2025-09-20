#question: Instead of checking just one number, can you print all prime numbers up to N?
'''
Input: 10
Output: 2 3 5 7
'''

def is_prime(n):
    st = True
    if n <= 1: 
        return 0
    else:
        for i in range(2, n):
            if (n%i == 0):
                return 0
    return n  
n = int(input())
for i in range(2,n):
    if (is_prime(i)):
        print(i, end =" ")


'''
What can be improved:

Return value: Right now, you return n for primes and 0 for non-primes.

Better: return True or False (clearer, more Pythonic).

Efficiency: Loop in is_prime(n) goes up to n.

We can check only up to √n.
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):  
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n+1):  
    if is_prime(i):
        print(i, end=" ")




