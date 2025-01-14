from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Binary search to count the number of soldiers in a row
        def countSoldiers(row):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left  # Number of 1s
        
        soldier_count = [(countSoldiers(row), i) for i, row in enumerate(mat)]
        
        soldier_count.sort()
        
        return [index for _, index in soldier_count[:k]]

        
    # without binary search 
    def kWeakestRows_2(self, mat: List[List[int]], k: int) -> List[int]:
       # Step 1: Calculate soldier count for each row using sum
       soldier_counts = [(sum(row), i) for i, row in enumerate(mat)]
       # Step 2: Sort by (soldier_count, row_index)
       soldier_counts.sort()
       # Step 3: Extract the indices of the k weakest rows
       return [index for _, index in soldier_counts[:k]]
