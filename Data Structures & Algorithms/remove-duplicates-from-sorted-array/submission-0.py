class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        officer = 0; cm = 1; unique = 1
        while cm < len(nums):
            if nums[cm] == nums[cm-1]:
                cm = cm + 1
            else:
                officer = officer+1
                nums[officer] = nums[cm]
                cm = cm + 1; unique = unique + 1
        return unique