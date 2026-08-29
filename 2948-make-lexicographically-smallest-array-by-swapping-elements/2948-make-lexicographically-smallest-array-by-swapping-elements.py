class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        
        
        
        n = len(nums)
        # Step 1: Pair each element with its original index and sort by value
        arr = sorted((num, i) for i, num in enumerate(nums))
        
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            # Step 2: Identify the range of the current group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
                
            # Step 3: Extract and sort the original indices for this group
            indices = sorted(k for _, k in arr[i:j])
            
            # Step 4: Assign the sorted values to the sorted indices
            for k, (val, _) in zip(indices, arr[i:j]):
                ans[k] = val
                
            i = j
            
        return ans
                

        
        