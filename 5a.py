class Solution:
    def getMirrorPalindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        l, l_len = s[0], 1
        for i in range(0, len(s)):
            odd = self.getMirrorPalindrome(s, i, i)
            even = self.getMirrorPalindrome(s, i, i + 1)

            if len(odd) > l_len:
                l = odd
                l_len = len(odd)

            if len(even) > l_len:
                l = even
                l_len = len(even)

        return l


s = Solution()
print(s.longestPalindrome("babad"))
