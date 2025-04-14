class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        nums = sorted(nums)
        r = 1
        if(len(nums)==1):
            return nums[0]

        for i in range(1,len(nums)):

            if(nums[i-1] == nums[i]):
                r = r + 1
                print(nums[i],r)
                if(r>n):
                    return nums[i]
            else:
                if(r>n):
                    return nums[i]
                r = 1
        