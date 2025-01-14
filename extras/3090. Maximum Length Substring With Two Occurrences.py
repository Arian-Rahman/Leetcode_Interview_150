from collections import Counter

class Solution:
    def longestSubstringWithTwoOccurrences(self, s: str) -> int:
        left = 0
        max_len = 0
        counter = Counter()
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            counter[s[right]] += 1
            
            # Shrink the window from the left if any character has more than 2 occurrences
            while any(count > 2 for count in counter.values()):
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]  # Remove the character if its count drops to 0
                left += 1  # Move the left pointer to shrink the window
            
            # Calculate the max length of valid substring
            max_len = max(max_len, right - left + 1)
        
        return max_len

def main():
    # Example input
    s = "bcbbbcba"
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the method and print the result
    result = solution.longestSubstringWithTwoOccurrences(s)
    print("Result:", result)

if __name__ == "__main__":
    main()
