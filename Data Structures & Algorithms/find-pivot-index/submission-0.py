class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        left = 0
        for a in nums:
            sum = sum + a
        for i in range(0, len(nums)):
            if i > 0:
                left += nums[i-1]
            right = sum - left - nums[i]
            if (left == right):
                return i
        return -1