class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2
        for index in range (2, len(nums)):
            if nums[index] != nums[k - 2]:
                nums[k] = nums[index]
                k += 1
            
        return k