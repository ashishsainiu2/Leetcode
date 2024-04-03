class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = sorted(nums)
        t = l[-1]

        for i in range(len(nums)) :
            if nums[i] == t:
                return i
            
        return -1
        