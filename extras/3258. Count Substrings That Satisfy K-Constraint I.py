class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            count_1 = 0
            count_0 = 0
            
            for j in range(i, n):
                if s[j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
                
                if count_1 <= k or count_0 <= k:
                    count += 1

        
        return count

    
if __name__ == '__main__':
    s = "1010101"
    k = 2

    solution = Solution()
    result = solution.countKConstraintSubstrings(s, k)

    print("Number of substrings satisfying the k-constraint:", result)