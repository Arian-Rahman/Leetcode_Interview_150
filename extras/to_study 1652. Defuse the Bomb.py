from typing import List

## Using Sliding Window 

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        result = [0] * n
        
        # Step 1: Calculate the initial window sum (forward or backward)
        window_sum = 0
        
        if k > 0:
            # Sum the first k elements (forward direction)
            for j in range(1, k + 1):
                window_sum += code[j % n]
        else:
            # Sum the first |k| elements (backward direction)
            for j in range(1, abs(k) + 1):
                window_sum += code[(n - j) % n]
        
        # Step 2: Use sliding window to calculate sum for each index
        for i in range(n):
            result[i] = window_sum
            
            # Slide the window
            # Remove the element that's leaving the window
            window_sum -= code[(i + 1) % n] if k > 0 else code[(i - abs(k) + 1) % n]
            
            # Add the element that's entering the window
            window_sum += code[(i + k) % n] if k > 0 else code[(i - abs(k) - 1) % n]
        
        return result


# # without Sliding window
# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n=len(code)

#         if k == 0:
#             return [0] * n
#         result = [0]*n
#         for i in range (n):
#             current_sum=0
#             if k>0:
#                 for j in range(1,k+1):
#                     current_sum+= code[(i+j)%n]  
                    
#             else : 
#                 for j in range (1,abs(k)+1):
#                     current_sum += code[(i-j+n)%n]
                             
#             result[i]=current_sum
#         return result
    

if __name__ == "__main__":

    solution = Solution()
    #decrypted_code = solution.decrypt(code=[5,7,1,4], k = 3)
    decrypted_code = solution.decrypt(code = [2,4,9,3], k = -2)

    print("Decrypted code:", decrypted_code)