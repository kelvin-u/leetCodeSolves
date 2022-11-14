class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs is the input string
        
        # hashmap to store all the sorted word
        Map = {} 
        
        for i in strs:
            temp = ''.join(sorted(i))
            
            if temp in Map:
                Map[temp].append(i)
            else:
                Map[temp]=[i]
        
        return Map.values()