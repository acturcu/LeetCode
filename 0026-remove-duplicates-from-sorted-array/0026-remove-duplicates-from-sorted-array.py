class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1 
        # end = len(nums) - 1
        k = len(nums)

        while start < len(nums):
            if nums[start] == nums[start - 1]:
                nums.pop(start)
                # nums.append(nums[start - 1])
                k -= 1
            else:
                start += 1
        return k 
