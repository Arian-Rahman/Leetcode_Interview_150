class Solution:
    def checker(self, s: set, c: chr): 
        """
        Checks if the character's opposite case exists in the supplied set
        """
        return (c.isupper() and c.lower() in s) or (c.islower() and c.upper() in s)

    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        character_set = set(s)

        # Loop through the string to find the first invalid character
        for i, c in enumerate(s):
            if not self.checker(character_set, c):  
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right

        # If no invalid character is found, the whole string is nice
        return s


def main():
    # Example input
    s = "aAabcAbB"
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the longestNiceSubstring method and print the result
    result = solution.longestNiceSubstring(s)
    print("Result:", result)

if __name__ == "__main__":
    main()
