class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rec = {}

        l, ans = 0, 0

        for r in range(len(s)):
            if s[r] in rec:
                l = max(rec[s[r]] + 1, l)
            rec[s[r]] = r
            ans = max(ans, r - l + 1)

        return ans