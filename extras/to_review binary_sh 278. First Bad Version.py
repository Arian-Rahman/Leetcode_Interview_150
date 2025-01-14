# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    # Example of a mock for testing purposes
    bad_version = 4  # Let's assume version 4 is the first bad version
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0,n
        while l<r:
            mid=(l+r)//2
            if isBadVersion(mid):
               r= mid
            else :
               l= mid+1
        return l
    
def main():
    # Test cases
    solution = Solution()

    # Example 1:
    n1 = 5
    # Assume the first bad version is 4
    print(solution.firstBadVersion(n1))  # Expected output: 4

    # Example 2:
    n2 = 1
    # Assume the first bad version is 1
    print(solution.firstBadVersion(n2))  # Expected output: 1

    # Example 3:
    n3 = 10
    # Assume the first bad version is 7
    print(solution.firstBadVersion(n3))  # Expected output: 7

if __name__ == "__main__":
    main()
