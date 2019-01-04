#Kadane algorithm for largest subarray sum O(n)
def kadane(a,n):
    max_so_far = -100000
    max_ending_here = 0
    
    for i in range(0,n): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here
            
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far
  

#main
print(kadane([1,8,-2,-9,4,13,-2,1],8))
