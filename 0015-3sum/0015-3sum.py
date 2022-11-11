class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        # sort the array 
        nums.sort()
        
        
        #loop through the elements
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: #dont count the duplicates
                continue
            
            l,r = i+1, len(nums) - 1 # pointers for the 2 sum part
            
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0: 
                    r -=1 
                elif threeSum < 0:
                    l +=1
                else: # threesum == 0
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result