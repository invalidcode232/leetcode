class Solution:
    def countSubstrings(self, s: str):
        dp = {}

        count = 0

        def is_palindrome(st: str) -> bool:
            i = 0
            j = len(st) - 1

            while i < j:
                if st[i] != st[j]:
                    return False

                i += 1
                j -= 1

            return True

        def p_iter(start_i: int, end_i: int, target: int) -> int:
            if start_i + 1 >= end_i:
                return 1 + p_iter(start_i, end_i + 1, target)

            ss = s[start_i:end_i]

            if end_i >= target:
                if ss in dp:
                    return dp[ss]

                if is_palindrome(ss):
                    return 1
                else:
                    return 0

            if ss in dp:
                return dp[ss] + p_iter(start_i, end_i + 1, target)

            if is_palindrome(ss):
                dp[ss] = 1
                return 1 + p_iter(start_i, end_i + 1, target)
            else:
                dp[ss] = 0
                return 0 + p_iter(start_i, end_i + 1, target)

        for i in range(len(s)):
            count += p_iter(i, i + 1, len(s))

        return count - 1


s = Solution()
print(s.countSubstrings("aaa"))
