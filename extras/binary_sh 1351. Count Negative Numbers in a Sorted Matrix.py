from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total_negatives = 0
        for row in grid :
            left,right = 0, len(row)-1
            while left<=right:
                mid = (left+right) //2
                if row[mid]<0:
                    total_negatives += right-mid+1
                    right = mid-1
                else :
                    left = mid+1
        
        return total_negatives


def main():
    # Test case 1: A grid with some negative numbers
    grid1 = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]

    solution = Solution()
    
    #Running the test cases
    print("Test Case 1:", solution.countNegatives(grid1))  # Expected output: count of negative numbers


if __name__ == "__main__":
    main()
