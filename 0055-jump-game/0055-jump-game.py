class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        # the -1 in second range to 0, -1 step backwards
        for i in range(len(nums)-2, -1, -1): # goal is already at last posistion
            if i + nums[i] >= goal:
                goal = i # shift the goal to i
        
        return goal == 0
    