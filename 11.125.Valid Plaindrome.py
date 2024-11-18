class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s=''.join(char for char in s if char.isalpha() or char.isdigit())
        return s == s[::-1]
        
def main ():
    strs = "race a car"
    solution = Solution()
    s = solution.isPalindrome(strs)
    print(s)


if __name__ == "__main__":
    main()