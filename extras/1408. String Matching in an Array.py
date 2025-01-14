from typing import List

# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         concatenated = "".join(words) 
#         result = []

#         for word in words:
#             if concatenated.count(f"{word}") > 1:
#                 result.append(word)
#                 print(result)
#         return result

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:  
                    result.append(words[i])
                    break  

        return result       

# Main function
def main():
    # Example input
    words = ["uexk","aeuexkf","wgxih","yuexk","gxea","yuexkm","ypmfx","jjuexkmb","wqpri","aeuexkfpo","kqtnz","pkqtnza","nrbb","hmypmfx","krqs","jjuexkmbyt","zvru","ypmfxj"]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the stringMatching function
    result = solution.stringMatching(words)
    
    # Print the result
    print("Result:", result)

# Run the main function
if __name__ == "__main__":
    main()
