class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0; res = 0
        h = {}
        h[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            ques = (sum - k)
            freq = h.get(ques, 0)
            res += freq
            h[sum] = h.get(sum, 0) + 1
        return res