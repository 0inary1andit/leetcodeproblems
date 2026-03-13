def rotate_beginner(nums, k):
    n = len(nums)
    if n == 0:
      return nums 
    
    
    k = k % n 
    
    for _ in range(k):
     
        last_item = nums.pop() 
      
        nums.insert(0, last_item)
