class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r:
            width = r - l
            ht = min(height[l], height[r])
            area = width * ht
            res = max(res, area)   # <-- Correct way
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res