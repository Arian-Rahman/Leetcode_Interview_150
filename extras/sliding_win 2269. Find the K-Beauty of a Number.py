from typing import List

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        counter = 0
        num_str = str(num)  
        for i in range(len(num_str) - k + 1):  
            sub_value = int(num_str[i:i + k])  
            if sub_value != 0 and num % sub_value == 0: 
                counter += 1
        return counter

def main():
    # Example input
    num = 120
    k = 2

    # Create an instance of the Solution class
    solution = Solution()

    # Call the divisorSubstrings method and print the result
    result = solution.divisorSubstrings(num, k)
    print("Result:", result)

if __name__ == "__main__":
    main()
