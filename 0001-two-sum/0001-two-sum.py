class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # if the array was ordered
        # left = 0
        # right = len(nums) - 1
        
        # while left < len(nums) and right>= 0 and nums[left] + nums[right] != target:
        #     if nums[left] + nums[right] < target:
        #         left += 1
        #     else:
        #         right -= 1
        
        dictionary = {}
        for index, el in enumerate(nums):
            dictionary[el] = index
        
        for index, el in enumerate(nums):
            remaining = target - el

            if remaining in dictionary and dictionary[remaining] != index:
                return [index, dictionary[remaining]] 

        return []