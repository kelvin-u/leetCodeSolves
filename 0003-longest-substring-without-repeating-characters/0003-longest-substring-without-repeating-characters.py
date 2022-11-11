class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # hashset to store the uniqe values
        seenSet = set()
            
        j = 0 # pointer to remove the values
        result = 0
        
        for i in range(len(s)):
            # in seenSet
            while s[i] in seenSet:
                seenSet.remove(s[j])
                j +=1 
                
            # not in seenSet
            seenSet.add(s[i])
            result = max(result, i - j + 1)
            
        return result
            
            