class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers, one at the beginning and one at the end of the array
        i, j = 0, len(height) - 1
        max_area = 0
        
        # Iterate until the two pointers meet
        while i < j:
            # Calculate the area formed between the lines at i and j
            width = j - i
            h = min(height[i], height[j])  # height is limited by the shorter line
            area = width * h
            
            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)
            
            # Move the pointer of the shorter line inward to try and find a larger area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_area


        

def main ():
    solution = Solution()
    s = solution.maxArea([1,8,6,2,5,4,8,3,7])
    print(s)


if __name__ == "__main__":
    main()