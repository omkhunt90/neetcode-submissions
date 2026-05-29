class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend = nums[0]; minend = nums[0]; res = nums[0]
        for i in range(1, len(nums)):
            c1 = maxend * nums[i]
            c2 = minend * nums[i]
            c3 = nums[i]
            maxend = max(c3, max(c1, c2))
            minend = min(c3, min(c1, c2))
            res = max(res, max(maxend, minend))
        return res