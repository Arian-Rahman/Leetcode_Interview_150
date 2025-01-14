from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)  
        answer = [0] * n  
        
        # Left-to-right pass
        moves = 0  # Total moves needed so far
        count = 0  # Number of balls collected so far
        
        for i in range(n):
            # Accumulate moves from left to right
            answer[i] += moves
            # If current box has a ball, increment the count
            count += int(boxes[i])
            # Update the moves for the next index
            moves += count

        # Right-to-left pass
        moves = 0 
        count = 0  
        
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            # If current box has a ball, increment the count
            count += int(boxes[i])
            # Update the moves for the next index
            moves += count

        return answer


if __name__ == "__main__":
    solution = Solution()
    boxes = "110"
    print(solution.minOperations(boxes))  # Output: [1, 1, 3]
