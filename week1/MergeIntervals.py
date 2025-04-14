class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        i = 0
        while i < len(intervals) - 1:
            a = intervals[i]
            b = intervals[i + 1]
            if b[0] <= a[1]:
                merged = [a[0], max(a[1], b[1])]
                intervals[i] = merged
                intervals.pop(i + 1)  
            else:
                i += 1

        return intervals
