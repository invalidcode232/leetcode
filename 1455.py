# pyright: strict


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")

        for i, word in enumerate(words):
            f = word.find(searchWord)

            if f == 0:
                return i + 1

        return -1


s = Solution()
print(s.isPrefixOfWord("this aproblem is an easy sproblem", "pro"))
