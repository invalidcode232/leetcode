class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        if len(words) == 1:
            return sentence[0] == sentence[-1]

        for i in range(len(words) - 1):
            w = words[i]
            nw = words[i + 1]

            if w[-1] != nw[0]:
                return False

        if words[-1][-1] != words[0][0]:
            return False

        return True


s = Solution()
print(s.isCircularSentence("eetcode"))
