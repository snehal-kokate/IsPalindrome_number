#leetcode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:

        dummy=ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next =l2
                l2 =l2.next
            tail =tail.next
        if l1:
            tail.next =l1
        elif l2 :
            tail.next =l2
        return dummy.next
    
#driver code
s = Solution()
l1 = [2,3,5,11]
l2 = [12,13,41,31,10]
print(s.mergeTwoLists(l1,l2))


"python way to solve this problem but not include linked list "

# merge two sorted list
l1 = [2,3,5,11]
l2 = [12,13,41,31,10]
#using sorted method
res = sorted (l1 + l2)
# printing sorted list
print(str(res)) #o/p=>[2, 3, 5, 10, 11, 12, 13, 31, 41]



