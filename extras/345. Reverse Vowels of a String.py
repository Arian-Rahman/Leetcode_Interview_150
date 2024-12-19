class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        s=list(s)
        i,j=0,len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
            elif s[i] in vowels :
                j-=1
                continue
            elif s[j] in vowels :
                i+=1
                continue
            i+=1 
            j-=1
            
        result= "".join(s)    
        return result
    
   
    
if __name__=="__main__":
    st = "IceCreAm"
    
    s = Solution()
    result = s.reverseVowels(st)
    print(result)