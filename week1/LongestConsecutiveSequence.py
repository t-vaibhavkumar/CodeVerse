class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0

        for i in nums:
            if i-1 not in nums:
                n = 1
                currentnum = i
                while currentnum+1 in nums:
                    currentnum += 1
                    n += 1
                l = max(l,n)
        return l