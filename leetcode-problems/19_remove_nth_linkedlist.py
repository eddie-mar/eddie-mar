# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        holder = head
        ith = 1

        while itr.next:
            itr = itr.next
            ith += 1
            if ith > n + 1: holder = holder.next
        
        if ith == n:
            head = holder.next
            return head
            
        holder.next = holder.next.next
        return head