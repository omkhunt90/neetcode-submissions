class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        maxx = arr[-1]
        res[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            res[i] = maxx
            maxx = max(maxx, arr[i])
        return res