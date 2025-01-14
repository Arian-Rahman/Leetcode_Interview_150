from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"  
        n = len(words)

        prefix_sum = [0] * (n + 1)  
        
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]

        results = []
        for start, end in queries:
            results.append(prefix_sum[end + 1] - prefix_sum[start])
        
        return results

def main():
    # Example input
    words = ["apple", "banana", "orange", "umbrella", "ice"]
    queries = [[0, 2], [1, 4], [0, 4]]

    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the vowelStrings method and print the result
    result = solution.vowelStrings(words, queries)
    print("Results:", result)

if __name__ == "__main__":
    main()
