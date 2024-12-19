from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        perm = []
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1
        perm.append(low)  
        return perm



if __name__ == "__main__":
    s_1 = "DDDD"
    s_2 = "IIII"
    s_3 = "IDID" # [0,4,1,3,2]
    s_4 = "DDI"  #  [3,2,0,1]
    
    solution = Solution()
    result = solution.diStringMatch(s_3)
    result_2 = solution.diStringMatch(s_4)

    print(result , result_2)  