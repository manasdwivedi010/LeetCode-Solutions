# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        if head==None or head.next==None:
            return head
        dummyNode=ListNode(0)
        prev=dummyNode

        curr=head

        while curr!=None:

            prev=dummyNode

            while prev!=None and prev.next!=None and prev.next.val<curr.val:
                prev=prev.next

            temp=curr.next
            curr.next=prev.next
            prev.next=curr

            curr=temp

        return dummyNode.next

        