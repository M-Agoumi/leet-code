from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp_sum = x + y + carry

            current.next = ListNode(tmp_sum % 10)
            current = current.next
            carry = tmp_sum // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next
    
def createList(numbers):
    if not numbers:
        return None

    head = ListNode(numbers[0])
    current = head

    for value in numbers[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


l1 = createList([0])
l2 = createList([0])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("\n\n")
while(result):
    print(result.val)
    result = result.next