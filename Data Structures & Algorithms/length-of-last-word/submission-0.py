class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in reversed(s):
            if i == ' ':
                if res == 0:
                    continue
                else:
                    return res
            else:
                res += 1
        return res