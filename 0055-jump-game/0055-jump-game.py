class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        # start at the last index, keep moving right to left
        for i in range(len(nums) - 1, -1, -1): 
            if i + nums[i] >= goal: #nums[i] is the jump length the num itself in nums
                goal = i
        
        # return True if goal == 0 else False
        return goal == 0