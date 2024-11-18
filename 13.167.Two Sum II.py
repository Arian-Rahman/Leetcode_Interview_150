class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]  
            elif current_sum < target:
                i += 1  
            else:
                j -= 1  

        return []  
