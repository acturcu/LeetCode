# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # number1 = 0
        # while l1:
        #     number1 *= 10
        #     number1 += l1.val
        #     l1 = l1.next
        # number2 = 0
        # while l2:
        #     number2 *= 10
        #     number2 += l2.val
        #     l2 = l2.next
        
        # res = number1 + number2 
        # ret = ListNode()
        # curr = ret

        # while res != 0:
        #     val = res % 10
        #     res = res // 10
        #     print(val)
        #     curr.next = ListNode(val)
        #     curr = curr.next
        # return ret.next
        
        returnList = ListNode()
        carry = 0
        current = returnList
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            
            new_val = val1 + val2 + carry
            carry = new_val // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            current.next = ListNode(new_val % 10)
            current = current.next


        return returnList.next