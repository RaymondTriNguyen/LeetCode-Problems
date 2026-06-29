# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode()
        current1 = list1
        current2 = list2
        mergeStore = merge

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                mergeStore.next = current1
                current1 = current1.next
                mergeStore = mergeStore.next
            else:
                mergeStore.next = current2
                current2 = current2.next
                mergeStore = mergeStore.next
        
        if current1 is not None:
            mergeStore.next = current1

        if current2 is not None:
            mergeStore.next = current2

        return merge.next
