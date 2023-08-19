# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # size = 0
        # mid = 0
        # cpy = head
        # while head:
        #     size +=1 
        #     head = head.next
        
        # if size % 2 == 0:
        #     mid = size / 2 + 1
        # else:
        #     mid = size / 2
        
        # while mid > 1:
        #     cpy = cpy.next
        #     mid -=1

        # return cpy

        # better runtime
        once = head
        twice = head

        while twice and twice.next:
            once = once.next
            twice = twice.next.next
        
        return once