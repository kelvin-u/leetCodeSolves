class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Map = {}
        
        for i, val in enumerate(nums):
            complement = target - val
            
            if complement in Map:
                return[Map[complement], i]
            Map[val] = i
        return