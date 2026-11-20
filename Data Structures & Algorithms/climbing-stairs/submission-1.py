class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n <= 2:
            return n

        f1=1
        f2=2

        for i in range(3, n + 1):
            curr = f1 + f2
            f1=f2
            f2=curr
            

        return curr