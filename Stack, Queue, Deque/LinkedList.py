from typing import Optional


class ListNode:
    def __init__(self, val, next):
        slots = ["val", "next"]
        self.val = val
        self.next = next


# https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=linked-list
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    head = dummy
    to_add = 0
    while l1 or l2 or to_add:
        if l1:
            to_add += l1.val
            l1 = l1.next
        if l2:
            to_add += l2.val
            l2 = l2.next
        dummy.next = ListNode(to_add % 10)
        dummy = dummy.next
        to_add //= 10
    
    return head.next


# https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=linked-list
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    dummy = head
    while list1 and list2:
        if list1.val < list2.val:
            dummy.next = ListNode(list1.val)
            dummy = dummy.next
            list1 = list1.next
        else:
            dummy.next = ListNode(list2.val)
            dummy = dummy.next
            list2 = list2.next
    
    dummy.next = list1 if list1 else list2
    
    return head.next


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=problem-list-v2&envId=linked-list
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    res = ListNode(0, head)
    dummy = res

    for _ in range(n):
        head = head.next
    
    while head:
        head = head.next
        dummy = dummy.next
    
    dummy.next = dummy.next.next
    
    return res.next


# https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=linked-list
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev, cur = dummy, head
    
    while cur and cur.next:
        s = cur.next
        t = cur.next.next
        
        s.next = cur
        cur.next = t
        prev.next = s
        
        prev = cur
        cur = t
    
    return dummy.next


# https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list
def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head
    
    length = 1
    dummy = head
    while dummy.next:
        length += 1
        dummy = dummy.next
    
    k %= length
    if not k:
        return head
    
    dummy1 = head
    for i in range(length - k - 1):
        dummy1 = dummy1.next
    
    res = dummy1.next
    dummy1.next = None
    dummy.next = head
    
    return res


# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=problem-list-v2&envId=linked-list
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1, head)
    left, right = dummy, head
    while right and right.next:
        if right.val == right.next.val:
            while right.next and right.val == right.next.val:
                right = right.next
            left.next = right.next
        else:
            left = left.next
        right = right.next
    
    return dummy.next


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=problem-list-v2&envId=linked-list
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    res = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    
    return res


# https://leetcode.com/problems/partition-list/description/?envType=problem-list-v2&envId=linked-list
def partition(head, x):
    leftNode, rightNode = ListNode(0), ListNode(0)
    left = leftNode
    right = rightNode
    
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    
    right.next = None
    left.next = rightNode.next
    
    return leftNode.next


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112506#1
def solution_112506():
    N, K = map(int, input().split())
    head = ListNode(1)
    tail = head
    for i in range(2, N + 1):
        tail.next = ListNode(i)
        tail = tail.next
    tail.next = head
    
    for _ in range(N):
        for i in range(K - 1):
            tail = tail.next
        print(tail.next.val, end=" ")
        tail.next = tail.next.next