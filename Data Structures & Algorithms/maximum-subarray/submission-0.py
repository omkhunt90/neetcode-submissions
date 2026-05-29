class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestend = nums[0]; res = nums[0]
        for i in range(1,len(nums)):
            c1 = bestend + nums[i]
            c2 = nums[i]
            bestend = max(c1, c2)
            res = max(res, bestend)
        return res