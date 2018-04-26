# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newL1 = l1[::-1]
        head = Node(newL1[0])
        node2 = Node(0)
        for num in newL1:
            node2 = Node(num)
            if num == newL1[0]:
                continue
            if not head.next:
                head.next = node2
            node2.next = node2
        print(head.next.val)

sol = Solution()

rel = sol.addTwoNumbers([1,2,3], [1,2,3])