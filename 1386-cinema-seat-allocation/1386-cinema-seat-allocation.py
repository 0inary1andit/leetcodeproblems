class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict
        
        # Dictionary to store the bitmask of reserved seats for each row
        # Only rows with AT LEAST ONE reservation will be in this dictionary
        reserved_map = defaultdict(int)
        
        for row, seat in reservedSeats:
            # Set the 'seat-th' bit to 1 for this row
            reserved_map[row] |= (1 << seat)
            
        # Start by assuming all rows are completely empty
        # Every empty row can fit exactly 2 families
        total_families = (n - len(reserved_map)) * 2
        
        # Now, evaluate the rows that actually have reservations
        for row, mask in reserved_map.items():
            
            # Can we fit 2 families? (Left and Right blocks are BOTH free)
            # 60 is left block, 960 is right block. 
            if (mask & 60) == 0 and (mask & 960) == 0:
                total_families += 2
                
            # If not 2, can we fit at least 1 family?
            # We can if Left OR Right OR Middle is free.
            elif (mask & 60) == 0 or (mask & 960) == 0 or (mask & 240) == 0:
                total_families += 1
                
            # Otherwise, 0 families fit in this row, so we add nothing.
            
        return total_families