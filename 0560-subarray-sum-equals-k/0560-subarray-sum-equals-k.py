class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Hash map to store the frequency of prefix sums
        # Base case: a prefix sum of 0 has occurred 1 time (empty subarray)
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Check if there exists a previous prefix sum such that:
            # current_sum - prev_sum = k  =>  prev_sum = current_sum - k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
                
            # Record/update the frequency of the current prefix sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count