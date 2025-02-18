class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        result= 0
        stack = []
        for c in s :
            if c == "(":
                counter +=1
            elif c == ")":
                counter -=1
            result = max(counter,result)
            
        return result

# Test cases
solution = Solution()
print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))  # Expected output: 3 (max depth: ((8)/4))
print(solution.maxDepth("(1)+((2))+(((3)))"))   # Expected output: 3 (max depth: (((3))))
print(solution.maxDepth("1+(2*3)/(2-1)"))       # Expected output: 1 (only single-level parentheses)
print(solution.maxDepth("1"))                   # Expected output: 0 (no parentheses)
print(solution.maxDepth("(())"))                # Expected output: 2 (max depth: (()))
print(solution.maxDepth("(()(()))"))            # Expected output: 3 (max depth: (()(())))
