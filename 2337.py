import re


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if re.sub("_", "", start) != re.sub("_", "", target):
            return False

        i_l = 0
        i_r = 0

        l_count = start.count("L")
        r_count = start.count("R")

        for i in range(len(target)):
            moved = False

            if target[i] == "R" and start[0 : i + 1].find("R") == -1:
                return False
            elif target[i] == "L" and start[i : len(start)].find("L") == -1:
                i_l += 1
                return False

        return True


s = Solution()
s.canChange("_L__R__R_")
