class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()

        for left in range(len(nums)):
            
            mid = left + 1
            right = len(nums) - 1

            while mid< right:
                if nums[left] + nums[mid] + nums[right] < 0 :
                    mid += 1
                elif nums[left] + nums[mid] + nums[right] > 0:
                    right -= 1
                else :
                    ret.add((nums[left], nums[mid], nums[right]))
                    mid +=1 
                    right -=1
        return ret
