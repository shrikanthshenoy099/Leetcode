class Solution:
    """My 1D Array DP Solution"""
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up[i] = up[i-1] + 1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                down[i] = down[i+1] + 1

        res = 0
        for i in range(n):
            if up[i] > 1 and down[i] > 1:
               res = max(res, up[i] + down[i] - 1)
        return res