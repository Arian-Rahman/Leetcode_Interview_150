class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        while i  < len(word1) and j<len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        
        if i  < len(word1):
            result.append(word1[i:])
        elif j< len(word2):
            result.append(word2[j:])
        
        return "".join(result)

        
def main():
    # Example inputs
    word1 = "ab"
    word2 = "pqrs"
    
    # Create an instance of the Solution class
    solution_instance = Solution()
    
    # Call the mergeAlternately method and store the result
    result = solution_instance.mergeAlternately(word1, word2)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
