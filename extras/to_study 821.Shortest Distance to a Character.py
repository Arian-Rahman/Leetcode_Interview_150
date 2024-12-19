from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('inf')] * n  # Initialize all distances to infinity

        # Left to Right Pass
        prev = -float('inf')  # Track the most recent index of character c
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev  # Calculate distance from the previous 'c'

        # Right to Left Pass
        prev = float('inf')  # Reset to track the closest 'c' from the right
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)  # Take the minimum distance

        return result

# Main function to test the Solution class
def main():
    s = "loveleetcode"
    c = "e"
    
    # Create an instance of the Solution class
    solution_instance = Solution()
    
    # Call the method and store the result
    result = solution_instance.shortestToChar(s, c)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
