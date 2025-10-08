n = [1,2,3,4,5,6]
s = len(n)
add = 0
sub = 0
for i in range(s):
    if i % 2 == 0 :
        sub -=n[i]
    else:
        add +=n[i]
if sub < 0 :
    sub = - (sub)
print(add-sub)

'''

i did not understand the logic, i thought: add all (odd index) and subtract ( all even index), then print both
''''

# now i understood what they meant is if odd index, add it, if even substract it.
n = [1,2,3,4,5,6]
s = len(n)
res = 0
for i in range(s):
    if i % 2 == 0 :
        res -=n[i]
    else:
        res +=n[i]
print(res)
    print(sub)
print(add-sub)
