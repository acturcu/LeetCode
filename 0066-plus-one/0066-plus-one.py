class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits[-1]
        if last != 9:
            digits[-1] += 1
            return digits
        else:
            carry = 1
            index = len(digits) - 1
            while carry and index >= 0:
                last = digits[index]
                if last != 9:
                    digits[index] += 1
                    return digits
                else:
                    digits[index] = 0
                    carry = 1
                    index -= 1
            
            if index == -1 and carry == 1:
                digits.insert(0, 1)
            
            return digits