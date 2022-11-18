class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = [] # store the mereged intervals
        # sort the intervals based on the start[i]
        intervals.sort(key=lambda x:x[0]) # 0 is start[i], first element in each interval
        
        for i in intervals:
            # empty list or not overlapping
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
            else: # overlapping
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged