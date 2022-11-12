class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 # left and right pointers
        
        while l <= r: 
            mid = (l+r) // 2  # [4,5,6,7]  mid = 1, nums[mid] = 5
            
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
                    r = mid -1
        return -1
            
        
        
        
                
        