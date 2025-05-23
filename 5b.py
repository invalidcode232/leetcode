class Solution:
    def is_palindrome(self, s: str):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def longest_palindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        max_ss, max_ss_l = "", 0

        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                ss = s[i:j]

                if self.is_palindrome(ss) and len(ss) > max_ss_l:
                    max_ss = ss
                    max_ss_l = len(ss)

        return max_ss


s = Solution()
print(
    s.longest_palindrome("nvkdsnvuijaerveoussuoevrecjkdslndsjkfndslfknerveoussuoevren")
)
