from bisect import bisect_right
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect_right(letters, target) # find the index of immediately bigger one than the target
        
        if index < len(letters):
            return letters[index]

        else:
            return letters[0]
