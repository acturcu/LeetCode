class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_index = 0 
        count = 1
        for index in range(len(nums)):
            if(nums[maj_index] == nums[index]):
                count +=1 
            else: 
                count -= 1
            if count == 0: 
                maj_index = index
                count = 1
        return nums[maj_index]

