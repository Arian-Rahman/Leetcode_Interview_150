class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range (0,len(s)-2):
            temp_sub = s[i:i+3]
            if len(set(temp_sub)) == len(temp_sub):
                count+= 1
                
        return count

def main():
    # Example input
    s = "xyzzaz"

    # Create an instance of the Solution class
    solution = Solution()

    # Call the countGoodSubstrings method and print the result
    result = solution.countGoodSubstrings(s)
    print("Result:", result)

if __name__ == "__main__":
    main()
