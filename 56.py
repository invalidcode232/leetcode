class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        # print(intervals)

        i = 0
        res: list[list[int]] = []

        while i < len(intervals):
            bot, top = intervals[i][0], intervals[i][1]
            merged = 0

            j = i + 1

            while j < len(intervals):
                bot2, top2 = intervals[j][0], intervals[j][1]

                if bot2 <= top:
                    top = max(top, top2)
                    merged += 1

                j += 1

            res.append([bot, top])

            i += 1 + merged

        return res


s = Solution()
print(s.merge([[1, 4], [2, 3]]))
