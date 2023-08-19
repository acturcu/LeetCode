class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_index = 1 
        curr = nums[0]
        # end = len(nums) - 1
        # k = len(nums)

        # while start < len(nums):
            # if nums[start] == nums[start - 1]:
            #     nums.pop(start)    
            #     k -= 1
            # else:
            #     start += 1
        for index in range(1, len(nums)):
            if curr != nums[index]:
                nums[uniq_index] = nums[index]
                curr = nums[index]
                uniq_index += 1
                
        return uniq_index 
