class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr_size = len(nums)
        index = 0
        k = arr_size
        end = arr_size - 1
        while index < arr_size and index <= end:
            if nums[index] == val:
                nums[index] = nums[end]
                nums[end] = val
                end -= 1
                k -= 1
            else:
                index +=1
        return k