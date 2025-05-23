# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         max_area = 0

#         for h_i, h in enumerate(height):
#             dist = 1

#             for nh_i in range(h_i + 1, len(height)):
#                 cur_nh = height[nh_i]

#                 cur_area = min(h, cur_nh) * dist
#                 max_area = max(cur_area, max_area)

#                 dist += 1

#         return max_area


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            print(height[left], height[right])
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


s = Solution()
inp = [1, 20, 30, 2, 3, 4, 20, 6]
print(s.maxArea(inp))
