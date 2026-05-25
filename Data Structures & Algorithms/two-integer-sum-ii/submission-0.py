class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 ; j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                i=i+1;j=j+1
                return [i,j]
            if sum < target:
                i = i+1
            if sum > target:
                j = j-1
        return print("no pair found")