class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty hashamp to store pairs
        
        Map = {}
        
        for i, val in enumerate(nums):
            complement = target - val
            
            if complement in Map:
                return[Map[complement], i]
            # add to map
            Map[val] = i
            
        return