class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        l = sorted(nums)
        return l[len(nums)//2]
        