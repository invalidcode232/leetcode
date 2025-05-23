class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        plist = []
        for p in pattern:
            if p not in plist:
                plist.append(p)

        log = {}
        patterns = 0
        res = ""

        for word in words:
            if word not in log:
                if patterns > len(plist) - 1:
                    return False

                log[word] = plist[patterns]
                res += log[word]
                patterns += 1
            else:
                res += log[word]

        return pattern == res


s = Solution()
print(s.wordPattern("deadbeef", "d e a d b e e f"))
