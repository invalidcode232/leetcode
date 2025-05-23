class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        r = list()
        for h in range(1, len(height)):
            if height[h - 1] > threshold:
                r.append(h)

        return r
