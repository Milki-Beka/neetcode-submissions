class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_x = 0
        x = 0
        for i in nums:
            if i == 1:
                x += 1
                if x > max_x:
                    max_x = x
            else:
                x = 0
        return max_x