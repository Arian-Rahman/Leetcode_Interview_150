class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        hash_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Traverse the string from right to left
        n = len(s)
        for i in range(n - 1, -1, -1):
            # If the current numeral is smaller than the previous one, subtract it
            if i < n - 1 and hash_table[s[i]] < hash_table[s[i + 1]]:
                total -= hash_table[s[i]]
            else:
                total += hash_table[s[i]]

        return total

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Input Roman numeral string from the user
    #roman = input("Enter a Roman numeral: ")

    roman = "XIX"
    
    # Call the romanToInt method and print the result
    result = solution.romanToInt(roman)
    print(f"The integer value of '{roman}' is: {result}")

if __name__ == "__main__":
    main()
