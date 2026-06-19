class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            ind = nums2.index(nums1[i]) 
            while ind < len(nums2):
                if nums1[i] < nums2[ind]:
                    res.append(nums2[ind])
                    break
                if ind == len(nums2) - 1:
                    res.append(-1)
                ind += 1
        return res