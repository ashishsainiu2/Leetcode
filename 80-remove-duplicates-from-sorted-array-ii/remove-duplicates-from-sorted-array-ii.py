class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        n = len(nums)

        j = 1
        for i in range(1, n):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j