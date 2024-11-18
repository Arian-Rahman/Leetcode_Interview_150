def min_subarray_length(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        # Expand the window by adding the current number to the sum
        current_sum += nums[right]

        # Contract the window from the left side until the sum is less than the target
        while current_sum >= target:
            # Update the minimum length
            min_length = min(min_length, right - left + 1)
            # Subtract the leftmost element and move the left pointer to the right
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_length(target, nums))  # Output: 2
