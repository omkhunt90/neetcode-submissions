class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0; r = len(nums) - 1; k = len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            right = nums[r]*nums[r]
            left = nums[l]*nums[l]
            if left < right:
                res[k] = right
                k -= 1; r -= 1
            else:
                res[k] = left
                k -= 1; l += 1
        return res