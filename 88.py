class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            check = m - 1

            for i in range(n):
                cur = nums2[i]

                swapped = False
                for j in range(check, -1, -1):
                    if nums1[j] > cur:
                        nums1[j + 1] = nums1[j]
                    else:
                        nums1[j + 1] = cur
                        swapped = True
                        break

                if not swapped:
                    nums1[0] = cur

                check += 1

        # return nums1


s = Solution()
print(s.merge([2, 0], 1, [1], 1))
