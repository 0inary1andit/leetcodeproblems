class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict
        
        
        reserved_map = defaultdict(int)
        
        for row, seat in reservedSeats:
            
            reserved_map[row] |= (1 << seat)
            
     
        total_families = (n - len(reserved_map)) * 2
        
       
        for row, mask in reserved_map.items():
            
            
          
            if (mask & 60) == 0 and (mask & 960) == 0:
                total_families += 2
                
      
            elif (mask & 60) == 0 or (mask & 960) == 0 or (mask & 240) == 0:
                total_families += 1
                
           
        return total_families