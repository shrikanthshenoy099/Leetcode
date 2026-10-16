class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        second_max = -1
        max_index = -1
        
        for i, num in enumerate(nums):
            if num > max_val:
                second_max = max_val
                max_val = num
                max_index = i
            elif num > second_max:
                second_max = num
                
        # Check if the largest element is at least twice as much as the second largest
        if max_val >= 2 * second_max:
            return max_index
        
        return -1