s = input().strip().lower()
a = 'aeiou'
print(s)
l1 = 0
l2 = len(s)
for i in s:
    if i in a:
        l1 +=1
print(f"vowels = {l1}")
print(f"consonants = {l2-l1}")
        
