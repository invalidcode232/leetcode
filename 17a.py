MAPPING = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        def combine(l1: list[str], l2: str):
            r: list[str] = []

            for i in l1:
                for j in l2:
                    r.append(i + j)

            return r

        l1 = [c for c in MAPPING[digits[0]]]

        for i in range(1, len(digits)):
            l1 = combine(l1, MAPPING[digits[i]])

        return l1


s = Solution()
print(s.letterCombinations("234"))
