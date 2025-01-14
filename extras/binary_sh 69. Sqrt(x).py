class Solution:
    def mySqrt(self, x: int) -> int:
        l,h=0,x
        while l<=h:
            mid = (l+h)//2
            square = mid*mid 
            if square == x :
                 return mid
            elif square<x:
                l=mid+1
            else :
                h=mid-1
                
            return h
                
                
        
        
def main():
    solution = Solution()
    
    # Test cases
    print(solution.mySqrt(4))   # Expected output: 2
    print(solution.mySqrt(8))   # Expected output: 2
    print(solution.mySqrt(0))   # Expected output: 0
    print(solution.mySqrt(1))   # Expected output: 1
    print(solution.mySqrt(25))  # Expected output: 5

if __name__ == "__main__":
    main()
