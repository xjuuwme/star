# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    if not head:
        print("Empty linked list!")
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

    def build_from(self, node_list: list[int]) -> ListNode:
        dummy = ListNode(-1, None)
        pre = dummy
        for node_val in node_list:
            pre.next = ListNode(node_val)
            pre = pre.next
        return dummy.next 

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
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1, None)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return dummy.next


solution = Solution()
head = solution.build()
print_ll(head)
head2 = solution.reverseList(head)
print_ll(head2)
# headb = solution.build_from([6, 6, 1, 2, 6, 3, 4, 6])
headb = solution.build_from([6, 6])
# headb = solution.build_from([1, 2])
print_ll(headb)
print_ll(solution.removeElements(headb, 6))
val = 61
print(val//2)
print(val/2)
print(val >> 1)
