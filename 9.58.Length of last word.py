class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

def main():
    s = Solution()
    x = s.lengthOfLastWord("   Zorro is lost again   ")
    print(x)


if __name__ == '__main__': 
    main()