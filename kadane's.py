#Kadane algorithm for largest subarray sum O(n)
def kadane(a,n):
    max_sum = a[0]
    temp_sum = a[0]
    
    for i in range(0,n): 
        temp_sum = max(a[i],temp_sum+a[i]) 
        max_sum=max(temp_sum,max_sum)
    return max_sum
  

#main
print(kadane([1,8,-2,-9,4,13,-2,1],8))
