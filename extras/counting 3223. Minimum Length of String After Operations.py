from typing import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        char_count = Counter(s)
        result_length = 0
        for count in char_count.values():
            if count % 2 == 0:  
                result_length += 2
            else:  
                result_length += 1
        
        return result_length