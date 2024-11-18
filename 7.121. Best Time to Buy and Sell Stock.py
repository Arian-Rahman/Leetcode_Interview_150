from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        if len(prices) == 0: return 0

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit


def main():
    # Example input
    prices = [7,1,5,3,6,4]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the maxProfit method
    result = solution.maxProfit(prices)
    
    # Print the output
    print("Maximum profit:", result)

if __name__ == "__main__":
    main()
