class Solution(object):
    def longestSubstring(self, s, k):
        n = len(s)
        count = {}
        total_max = 0

        
        if n < k:
            return 0

       
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for i in range(n):
            if count[s[i]] < k:
                chunks = s.split(s[i])
                
                for c in chunks:
                    curr_max = self.longestSubstring(c, k) 
                    total_max = max(curr_max, total_max)        
                
                return total_max
        
       
        return n