class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        su = 0
        res=[]
        for i in range(len(nums)):
            res.append(su + nums[i])
            su=res[i]
        return res