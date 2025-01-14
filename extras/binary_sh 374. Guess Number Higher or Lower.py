# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

    
def main():
    # Define a mock guess function for testing
    picked_number = 6  # Replace this with the number you want to test

    def guess(num: int) -> int:
        if num < picked_number:
            return 1
        elif num > picked_number:
            return -1
        else:
            return 0

    class Solution:
        def guessNumber(self, n: int) -> int:
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                result = guess(mid)
                if result == 0:
                    return mid
                elif result == 1:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            

    solution = Solution()
    print(solution.guessNumber(10))  # Replace 10 with the range limit for testing

if __name__ == "__main__":
    main()
