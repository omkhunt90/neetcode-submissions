class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0; high = 0; res = float('-inf')
        h = {}
        for high in range(len(s)):
            h[s[high]] = h.get(s[high], 0) + 1
            mx = max(h.values())
            size = high - low + 1
            diff = size - mx
            while diff > k:
                h[s[low]] = h.get(s[low], 0) - 1
                if h[s[low]] == 0:
                    del h[s[low]]
                low += 1
                size = high - low + 1
                mx = max(h.values())
                diff = size - mx
            size = high - low + 1
            res = max(res,size)
        return res
            
