# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print()


class Solution:
    def build(self):
        head = ListNode(0, None)
        current = head
        for i in range(10):
            current.next = ListNode(i+1, None) 
            current = current.next
        return head

    def reverseList0(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre 
                    
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        while head.next:
            tmp = head.next.next
            next = head.next
            head.next = tmp
            next.next = dummy.next
            dummy.next = next
        return dummy.next
        

solution = Solution()
head = solution.build()
print_ll(head)
head2 = solution.reverseList(head)
print_ll(head2)
            