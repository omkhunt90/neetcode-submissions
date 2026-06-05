class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            h[nums[i]] = h.get(nums[i], 0) + 1
        return False