class Solution:
    def get_all_num(self, l: list[int], t: int) -> list[int]:
        r = []
        for n in l:
            if n == t:
                r.append(n)

        return r

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        h = []
        r = []

        for n in nums1:
            if n in h:
                continue

            if n in nums1 and n in nums2:
                r1 = self.get_all_num(nums1, n)
                r2 = self.get_all_num(nums2, n)

                br = min(r1, r2)

                for d in br:
                    r.append(d)

            h.append(n)

        return r


s = Solution()
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
