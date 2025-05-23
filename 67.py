# pyright: strict
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s: list[str] = []

        i = len(a)
        j = len(b)
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                i -= 1
                carry += int(a[i])

            if j >= 0:
                j -= 1
                carry += int(b[i])

            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))


s = Solution()
print(s.addBinary("111", "111"))
