class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        last_col = len(triangle) - 1

        bottoms = triangle[last_col]
        res = None

        for i in range(0, len(bottoms)):
            bot = bottoms[i]

            path_val = bot

            c = 1
            for j in range(last_col - 1, 0, -1):
                best_val = -1

                print(j, i - c)
                if i == 0:
                    best_val = triangle[j][0]
                elif i == len(bottoms) - 1:
                    best_val = triangle[j][len(triangle[j]) - 1]
                else:
                    best_val = min(triangle[j][i - c], triangle[j][i - c + 1])

                path_val += best_val

                c += 1

            path_val += triangle[0][0]

            if res == None:
                res = path_val
            else:
                res = min(res, path_val)

        return res


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
