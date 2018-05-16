class Solution(object):
    def minWindow(self, s,t):
        need = {}
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1
        freq = {}

        satisfied = 0
        l = 0
        window = ""
        for r in range(len(s)):
            c = s[r]
            if c in need:
                freq[c] = freq[c] + 1 if c in freq else 1
                if freq[c] ==need[c]:
                    satisfied += 1
            while l <= r and satisfied == len(need):
                if window == '' or len(window) > r-l +1:
                    windows = s[l:r+1]
                if s[l] in need:
                    freq[s[l]] -= 1
                    if freq[s[l]] < need[s[l]]:
                        satisfied -= 1
                l += 1
        return windows
