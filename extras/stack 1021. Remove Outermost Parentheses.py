class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        result = ""
        
        for c in s:
            if c == '(':
                if balance > 0:  # Exclude outermost '('
                    result += c
                balance += 1
            elif c == ')':
                balance -= 1
                if balance > 0:  # Exclude outermost ')'
                    result += c
        
        return result

                

# Test cases
solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))  # Expected output: "()()()"
print(solution.removeOuterParentheses("(()())(())(()())"))  # Expected output: "()()()()()"
print(solution.removeOuterParentheses("()()"))  # Expected output: ""
print(solution.removeOuterParentheses("(()())"))  # Expected output: "()"
print(solution.removeOuterParentheses("(())"))  # Expected output: ""
