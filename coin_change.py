def count_ways(s,m,n):
  #s= list of denominations
  #m= no. of denominations
  #n= amount of money to be obtained
  '''Space Complexity of this function: O(n) 
  table[i] will be storing the number of solutions
  for value i. We need n+1 rows as the table is
  constructed in bottom up manner using the base
  case (n = 0)'''
  
  # Initialize all table values as 0 
  table=[0]*(n+1) #takes O(n)

  #Base case (If given value is 0)
  table[0]=1

  '''Pick all coins one by one and update the table[]
  values after the index greater than or equal to 
  the value of the picked coin'''

  for i in range(0,m):
    for j in range(s[i],n+1,1):
      table[j] += table[j-s[i]]
  return table[n]

#main
s=[1,5,10]
m=len(s)
n=12
print(count_ways(s,m,n))
