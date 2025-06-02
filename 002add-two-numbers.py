# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def get_list_length(head):
            """
            计算链表的长度。
            """
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count
        len_l1 = get_list_length(l1)
        len_l2 = get_list_length(l2)
        larger = max(len_l1, len_l2)
        result = [0] * (larger + 1)
        is_carry_out = False
        for i in range(larger):
            sum = l1[i] + l2[i] + 1 if is_carry_out else 0
            is_carry_out = True if sum >= 10 else False
            result[i] = sum % 10
        result.reverse()
        return int(''.join(map(str,result)))


# copy from leetcode comment
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result