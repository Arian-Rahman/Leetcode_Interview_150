class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                index=t.find(c)
                t=t[index+1:]
                print(t)
            else :
                return False
        return  True
        

        

def main ():
    s= "aaaaaa"
    t="bbaaaa"
    solution = Solution()
    s = solution.isSubsequence(s,t)
    print(s)


if __name__ == "__main__":
    main()