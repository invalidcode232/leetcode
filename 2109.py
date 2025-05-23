class Solution:
    # def addSpaces(self, s: str, spaces: list[int]) -> str:
    #     spaces.sort()
    #
    #     sl = [c for c in s]
    #
    #     add = 0
    #     for space in spaces:
    #         sl.insert(space + add, " ")
    #         add += 1
    #
    #     return "".join(sl)
    #

    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = ""

        start = 0
        for space in spaces:
            res += s[start:space] + " "
            start = space

        res += s[start:]

        return res


s = Solution()
print(s.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
