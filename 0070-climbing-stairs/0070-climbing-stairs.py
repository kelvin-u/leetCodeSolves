class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        
        for i in range(n-1):
            temp = one #
            one = one + two # the new one is basically the old (one + two)
            two = temp # two is now shifted to the one position
        return one
            
            