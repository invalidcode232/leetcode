class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slist = []

        for c in s:
            if c not in slist:
                slist.append(c)

        tlist = []
        for c in t:
            if c not in tlist:
                tlist.append(c)

        if len(slist) != len(tlist):
            return False

        mapping = {}
        for i, v in enumerate(tlist):
            mapping[v] = slist[i]

        res = ""
        for c in t:
            res += mapping[c]

        return s == res
