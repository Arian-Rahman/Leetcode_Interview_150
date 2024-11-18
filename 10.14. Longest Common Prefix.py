class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_element= min(strs, key=len)

        i=0
        while i< len(strs) :
            element = strs[i]
            if element.startswith(smallest_element) == False:
                smallest_element=smallest_element[:-1]
                i=0
            else:
                i+=1

        return smallest_element
               

               
        
def main ():
    strs = ["flower","flow","flight"]
    solution = Solution()
    s = solution.longestCommonPrefix(strs)
    print(s)


if __name__ == "__main__":
    main()