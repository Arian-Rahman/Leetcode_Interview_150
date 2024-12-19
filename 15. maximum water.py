def min_subarray_length(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')
    length = len(nums)
    for right in range(length):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length,right-left+1)
            current_sum -=nums[left]
            left+=1
    return min_length if current_sum != float('inf') else 0


 


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_length(target, nums))  # Output: 2
