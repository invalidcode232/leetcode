class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        cur = "1"

        for n in range(2, n + 1):
            i = 0
            # log = []
            new_cur = ""

            while i < len(cur):
                focus = cur[i]
                count = 1

                while i + count < len(cur) and cur[i + count] == focus:
                    count += 1

                new_cur += str(count) + focus
                i = i + count

            cur = new_cur

        return cur


s = Solution()
print(s.countAndSay(4))
