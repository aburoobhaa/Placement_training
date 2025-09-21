n = int(input())
le = len(str(n))
#print(le)
s = 0
temp = n 
while (n >0):
    l = n % 10
    r = n//10
    s += (l**le)
    #print(s)
    n = r 
if (temp == s):
    print(True) 
else:
    print(False)

'''
NOTE: I HAVE LEARNED:

1. I learned to format the decimal using ------> f{value:.2f}"
2. Find no of digits in a num using -----------> len(str(num))
3. Get the last digit -------------------------> l = n%10
4. Get the remaining digits from the last -----> r = n//10 

    
