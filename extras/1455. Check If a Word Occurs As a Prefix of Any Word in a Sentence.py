class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i=1
        sentence = sentence.split()
        for word in sentence:
            if searchWord in word[:len(searchWord)]:
                return i
            i+=1
            
        return -1
        
        
if __name__ == "__main__":
    s_1 = "THIS IS A PEN"
    s_2 = "PE"

    
    solution = Solution()
    result = solution.isPrefixOfWord(s_1,s_2)

    print(result )  