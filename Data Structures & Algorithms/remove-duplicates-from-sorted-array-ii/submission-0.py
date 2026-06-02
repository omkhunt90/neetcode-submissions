class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        of = 0; uni = 1; cm = 1; get_in = 0
        while cm < len(nums):
            if nums[cm] == nums[cm-1]:
                if get_in == 0:
                    of = of + 1; uni = uni + 1
                    nums[of] = nums[cm]
                    get_in = 1; cm = cm + 1
                else:
                    cm = cm + 1
            else:
                of = of + 1; uni = uni + 1
                nums[of] = nums[cm]
                get_in = 0; cm = cm + 1
        return uni