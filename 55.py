class Solution:
    def canJump(self, nums: list[int]) -> bool:
        def dfs(pos: int):
            if pos >= len(nums) - 1:
                return True

            if nums[pos] == 0:
                return False

            for i in range(pos + 1, pos + nums[pos] + 1):
                if pos >= len(nums) - 1:
                    return True

                if dfs(i) == True:
                    return True

            return False

        return dfs(0)


s = Solution()
print(
    s.canJump(
        [
            2,
            0,
            6,
            9,
            8,
            4,
            5,
            0,
            8,
            9,
            1,
            2,
            9,
            6,
            8,
            8,
            0,
            6,
            3,
            1,
            2,
            2,
            1,
            2,
            6,
            5,
            3,
            1,
            2,
            2,
            6,
            4,
            2,
            4,
            3,
            0,
            0,
            0,
            3,
            8,
            2,
            4,
            0,
            1,
            2,
            0,
            1,
            4,
            6,
            5,
            8,
            0,
            7,
            9,
            3,
            4,
            6,
            6,
            5,
            8,
            9,
            3,
            4,
            3,
            7,
            0,
            4,
            9,
            0,
            9,
            8,
            4,
            3,
            0,
            7,
            7,
            1,
            9,
            1,
            9,
            4,
            9,
            0,
            1,
            9,
        ]
    )
)
