from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        hash_map = Counter(nums1)
        print(hash_map)
        return []


# s = Solution()
# print(s.intersect([4, 9, 9, 5], [9, 4, 9, 8, 4]))

c1 = Counter("hello world").most_common()
for k, v in enumerate(c1):
    print(k, v)
