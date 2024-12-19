class Solution:
    def reverseWords(self, s: str) -> str:
        "This is done utilizing python functions "
        words=s.split()
        for i in range (len(words)):
            words[i] = words[i][::-1]
        return " ".join(words )
        " This is done using two pointers "
        # result_string = []
        # words = s.split()
        # for word in words :
        #     char_list= list(word)
        #     i,j = 0,len(word)-1
        #     while i<j:
        #         char_list[i],char_list[j] = char_list[j],char_list[i]
        #         i+=1
        #         j-=1
        #     result_string.append("".join(char_list))
            
        # return " ".join(result_string)
                            
            

        
def main():
    s =Solution()
    reversed = s.reverseWords("This Is a Pen")
    print(reversed)
    
if __name__ == "__main__":
    main()