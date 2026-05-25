class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i + 1; right = len(nums) - 1
            sum = -1 * nums[i]
            while left < right:
                s = nums[left] + nums[right]
                if s == sum:
                    result.append((nums[i],nums[left],nums[right]))
                    left += 1; right -= 1
                    while left < len(nums) and nums[left]==nums[left-1]:
                        left += 1
                    while right >=0 and nums[right]==nums[right+1]:
                        right -= 1
                elif s < sum:
                    left += 1
                else:
                    right -= 1
        return result
