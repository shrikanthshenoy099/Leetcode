class Solution:
    def sortColors(self, nums: list[int]) -> None:
     
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
            
       
        idx = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[idx] = color
                idx += 1