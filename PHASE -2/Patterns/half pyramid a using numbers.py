#Question : Print number triangle of right


n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,end = ' ')
    print()

'''
output:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

''' 

'''
NOTE:🙅‍♀️
When making patterns with loops:
  Outer loop → controls the rows (how many lines you print).
  Inner loop(s) → control the columns (what happens inside each row).

So you can imagine the pattern like a grid:
      Outer loop moves down (row by row).
      Inner loop moves across (column by column).

