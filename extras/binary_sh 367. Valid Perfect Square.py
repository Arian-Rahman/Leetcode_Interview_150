class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0: 
         return False  # Negative numbers can't be perfect squares
    
       # Edge cases for 0 and 1
        if num == 0 or num == 1: 
         return True
     
        l,r = 0, num>>1
        
        while l<=r:
            mid = (l+r)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid-1
            else:
                l= mid+1

        return False
    
def main():
    solution = Solution()
    print(f" 64 is Perfect square ? {solution.isPerfectSquare(64)}")
    print(f" 16 is Perfect square ? {solution.isPerfectSquare(16)}")
    print(f" 12 is Perfect square ? {solution.isPerfectSquare(12)}")
    print(f" 9 is Perfect square ? {solution.isPerfectSquare(9)}")
    print(f" 4 is Perfect square ? {solution.isPerfectSquare(4)}")



if __name__ == "__main__":
    main()
