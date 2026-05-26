class Solution:
    def sahi(self,have: str, needed: str) -> bool:
        for i in range(0,256):
            if have[i] < needed[i]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        low = 0; high = 0; res = len(s) + 1; start = 0
        have = [0] * 256
        needed = [0] * 256
        for ch in t:
            needed[ord(ch)] += 1
        for high in range(len(s)):
            have[ord(s[high])] += 1
            while self.sahi(have,needed):
                size = high - low + 1
                if res > size:
                    res = size
                    start = low
                have[ord(s[low])] -= 1
                low += 1
        if res == len(s)+1:
            return ""
        return s[start:start+res]
