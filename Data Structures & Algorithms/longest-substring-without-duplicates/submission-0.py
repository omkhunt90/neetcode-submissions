class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0; high = 0; res = 0
        h = {}
        for high in range(len(s)):
            h[s[high]] = h.get(s[high], 0) + 1
            k = high - low + 1
            while len(h) < k:
                h[s[low]] = h.get(s[low], 0) - 1
                if h[s[low]] == 0:
                    del h[s[low]]
                low += 1
                k = high - low + 1
            if len(h) == k:
                res = max(k,res) 
        return res 