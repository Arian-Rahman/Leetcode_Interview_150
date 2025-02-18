class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Helper function: find the index of the character `ch`
        index = -1
        stack = list()
        for c in word:
            stack.append(c)
            if c == ch:
                index= word.find(ch)
                break 
        
        if index != -1:
            word = ''.join(stack[:index+1][::-1]) + ''.join(word[index+1:])
        
        return word

# Test cases for the main function
solution = Solution()
print(solution.reversePrefix("abcdef", "c"))  # Expected result after implementing the solution
print(solution.reversePrefix("abcdef", "z"))  # Expected result after implementing the solution
