class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        # print(nums)

        r: list[list[int]] = []
        for i in range(len(nums)):
            if i == len(nums) - 3:
                break

            first = nums[i]

            for j in range(i + 1, len(nums) - 2):
                second = nums[j]
                sum = first + second

                third_i = i + 2
                fourth_i = len(nums) - 1

                while third_i < fourth_i:
                    third = nums[third_i]
                    fourth = nums[fourth_i]
                    # print(first, second, third, fourth)
                    check = sum + third + fourth

                    if check == target:
                        r.append([first, second, third, fourth])
                        # third_i += 1
                        fourth_i -= 1

                        continue

                    if check > target:
                        fourth_i -= 1
                    else:
                        third_i += 1

        # removing duplicateZ
        new_r = []
        for l in r:
            l.sort()
            if l not in new_r:
                new_r.append(l)

        return new_r


s = Solution()
print(s.fourSum([], 0))
