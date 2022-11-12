class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums) - 1
        
        while l <= r: 
            mid = (l+r) // 2 #// if a list has 4 elements [0,1,2,3] 1 is mid
            
            if nums[mid] == target: 
                return mid
            
            # left partition
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # right partition
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        # target doesn't exist
        return -1
                