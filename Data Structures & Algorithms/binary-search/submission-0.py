class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(target)
        return -1