# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = head
        preGroup = head
        isFirst = True
        while root != None:
            saved = []
            for i in range(k):
                saved.append(root)
                root = root.next
                if root == None:
                    break
            pre = None
            prePreGroup = preGroup
            if len(saved) != k:
                prePreGroup.next = saved[0]
            else:
                for i in range(k):
                    if pre == None:
                        preGroup = saved[i]
                        preGroup.next = None
                    if pre != None:
                        saved[i].next = pre
                    pre = saved[i]
                    if i == (k - 1):
                        if isFirst:
                            head = saved[i]
                        else:
                            prePreGroup.next = saved[i]
            isFirst = False
        return head

a = ListNode(0)
head = a
a.next = ListNode(1)
a = a.next
a.next = ListNode(2)
a = a.next
a.next = ListNode(3)
a = a.next
a.next = ListNode(4)
a = a.next
a.next = ListNode(5)
a = a.next

res = Solution().reverseKGroup(head, 4)

while res != None:
    print(res.val)
    res = res.next
