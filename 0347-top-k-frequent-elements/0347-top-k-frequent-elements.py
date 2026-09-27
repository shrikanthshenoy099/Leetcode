class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for num in nums:
            if num in val:
                val[num] += 1
            else:
                val[num] = 1
        sorted_nums = sorted(val, key=val.get, reverse=True)
        return sorted_nums[:k]

               