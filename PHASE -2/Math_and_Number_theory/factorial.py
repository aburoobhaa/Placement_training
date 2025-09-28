def fact(n):
    if n<=1:
        return 1
    else:
        return fact(n-1)*n
   
def f(n):
    r = 1
    while(n>=1):
        r = n * r
        n = n-1
    return r
n = 5 
print(fact(n))
print(f(n))

