from typing import Optional


class Node:
    """
    A linked list is a data structure which has connected elements where each element
    has reference to its next element.

    A Node is a box which has data and reference to the next element. Series of nodes form
    the linked list.

    The advantage of linked list lies in updating and deleting in the middle or adding in
    the beginning when compared to arrays which takes O(N).

    Accessing in Linked list is a drawback compared to arrays as we have to traverse the
    previous elements to get to the exact element.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def traverse(curr):
        """
        This helper function helps us to traverse the linked list
        """
        while curr is not None:
            print(curr.data)
            curr = curr.next

    @staticmethod
    def insert_at_top(data, first_node):
        """
        This helper function helps us to insert an element at the front of the linked list
        """
        nn = Node(data)
        if first_node is None:
            first_node = nn
        else:
            nn.next = first_node
            first_node = nn
        return first_node


# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
#
# head = a
# a.next = b
# b.next = c
# c.next = d


head = None


def insert_at_top(data):
    global head
    nn = Node(data)
    if head is None:
        head = nn
    else:
        nn.next = head
        head = nn


def insert_at_end(data):
    """
    This helper function helps us to insert an element at the end of the linked list
    """
    global head
    nn = Node(data)
    if head is None:
        head = nn
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = nn


def insert_at_middle(data, pos):
    """
    Complexity : O(N)
    """
    global head
    nn = Node(data)
    if head is None:
        head = nn
    else:
        curr = head
        i = 0
        while i < pos - 1 and curr is not None and curr.next is not None:
            curr = curr.next
            i += 1
        nn.next = curr.next
        curr.next = nn


def traverse():
    """
    This helper function helps us to traverse the linked list
    """
    global head
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next


def delete_at_top():
    """
    Complexity : O(1)
    """
    global head
    if head is not None:
        head = head.next


def delete_at_end():
    global head
    if head is not None and head.next is None:
        head = None
    elif head is not None and head.next is not None:
        curr = head
        while curr is not None and curr.next is not None and curr.next.next is not None:
            curr = curr.next
        curr.next = None


# insert_at_top("A")
# insert_at_top("B")
# insert_at_top("C")
# insert_at_top("D")
# insert_at_end("A")
# insert_at_end("B")
# insert_at_end("C")
# insert_at_end("D")

# insert_at_middle("K", 2)
# insert_at_middle("J", 3)

# insert_at_top("Z")
# head = head.insert_at_top("E", head)
# head.traverse(head)

# delete_at_top()

# delete_at_end()
# traverse()

class LinkedListIntersection:
    """
    Two linked lists can be of same length or varying length.

    In case of same length, we can start comparing from the first element
    to get the exact intersection.

    In case of varying length, the intersection can only happen from the
    start of the smaller list.

    So we need to move the node of the bigger linked list of length(n) to
    the length of the smaller list (m) to start comparing and find the intersection point
    i.e. n-m if m is smaller.

    Two pointer solution.

    Complexity : O(M+N) Memory: O(1)
    """

    def getIntersectionNode(self, headA, headB):
        m = self.find_length(headA)
        n = self.find_length(headB)

        fp = headA
        sp = headB

        if m <= n:
            for i in range(n - m):
                sp = sp.next
        else:
            for i in range(m - n):
                fp = fp.next
        while fp is not None:
            if fp == sp:
                return fp
            fp = fp.next
            sp = sp.next

        return None

    def find_length(self, head):
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        return count


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeSortedLinkedList:
    """
        This problem is similar to merging two sorted lists.

        Complexity : O(m+n)
    """

    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        endNode = None
        head = None
        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                if p1.val <= p2.val:
                    data = p1.val
                    p1 = p1.next
                else:
                    data = p2.val
                    p2 = p2.next
            elif p1 is not None:
                data = p1.val
                p1 = p1.next
            else:
                data = p2.val
                p2 = p2.next
            if endNode is None:
                head = self.insert_at_end(endNode, data)
                endNode = head
            else:
                endNode = self.insert_at_end(endNode, data)
        return head

    def insert_at_end(self, endNode, data):
        nn = ListNode(data)
        if endNode is not None:
            endNode.next = nn
        return nn


class LinkedListCycle:
    """
    Hare and tortoise algorithm where one pointer moves faster than the other pointer.

    Create two pointers fp and sp.
    Initially both the pointers will point to the first node.

    Second pointer will move double the speed of the first pointer. If there is a cycle
    the second pointer will circle back. Eventually the fp and sp will meet.

    If there is a cycle, sp must meet fp before fp traverses all the nodes one at a time.

    If there is no cycle the second pointer will reach the end of the linked list before
    the first pointer.

    Complexity: O(N)

    """

    def hasCycle(self, head):
        if head is None or head.next is None:  # Edge case where the length is 0 or 1
            return False
        fp = head  # fp moves one node at a time
        sp = head.next.next  # sp moves two nodes at a time

        while fp is not None and sp is not None and sp.next is not None:
            if fp == sp:
                return True
            fp = fp.next
            sp = sp.next.next
        return False


class ReverseLinkedList:
    """
    Complexity: O(N)
    """

    def __init__(self):
        self.newHead = None

    def reverseListIteratorHashMapMethod(self, head):
        trace = {}
        curr = head
        while curr is not None and curr.next is not None:
            trace.update({curr.next: curr})
            curr = curr.next
        newHead = curr
        while curr is not None:
            curr.next = trace.get(curr)
            if curr == head:
                curr.next = None
                break
            curr = curr.next
        return newHead

    def reverseListIteratorStackMethod(self, head):
        trace = []
        curr = head
        while curr is not None and curr.next is not None:
            trace.append(curr)
            curr = curr.next
        newHead = curr
        while curr is not None:
            if curr == head:
                curr.next = None
                break
            curr.next = trace.pop()
            curr = curr.next
        return newHead

    def reverseList(self, head):
        if head is not None:
            lastNode = self.reverse(head)
            lastNode.next = None
        return self.newHead

    def reverse(self, current):
        if current.next is None:
            self.newHead = current
            return current
        else:
            lastNode = self.reverse(current.next)
            lastNode.next = current
            return current


# head = ReverseLinkedList().reverseList(head)

# head = ReverseLinkedList().reverseListIteratorHashMapMethod(head)
# head = ReverseLinkedList().reverseListIteratorStackMethod(head)
# traverse()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class AddTwoNumbersLinkedList:
#
#     def insert_at_end(self, node, data):
#         """
#         This helper function helps us to insert an element at the end of the linked list
#         """
#         nn = Node(data)
#         if node is None:
#             node = nn
#         else:
#             curr = node
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = nn
#         return node
#
#     def addTwoNumbers(self, l1, l2):
#         ans = None
#         q = 0
#         while l1 is not None or l2 is not None:
#             if l1 is not None and l2 is not None:
#                 val = l1.val + l2.val + q
#                 l1 = l1.next
#                 l2 = l2.next
#             elif l1 is not None:
#                 val = l1.val + q
#                 l1 = l1.next
#             elif l2 is not None:
#                 val = l2.val + q
#                 l2 = l2.next
#             q = val // 10
#             r = val % 10
#             ans = self.insert_at_end(ans, r)
#         if q:
#             ans = self.insert_at_end(ans, q)
#         return ans


class AddTwoNumbersLinkedList:

    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # dummy head
        tail = dummy  # tail pointer
        carry = 0

        while l1 or l2 or carry:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            tail.next = ListNode(val % 10)
            tail = tail.next  # move tail forward

        return dummy.next

# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)
#
# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)
#
# AddTwoNumbersLinkedList().addTwoNumbers(l1, l2)


class PalindromeLinkedList:
    """
    For a palindrome, if the length is odd, then the first half must mirror the second half
    after the middle element. We have to skip the middle node.


    If it is even then there is no middle element, the first half must mirror the second half.

    Odd: Find reverse point (n//2) + 1 position -> Reverse 2nd half -> Compare with two pointers
    Even: Find reverse point (n//2) position -> Reverse 2nd half -> Compare with two pointers
    """

    def isPalindrome(self, head: [ListNode]) -> bool:
        n = self.findLength(head)
        if n == 1:
            return True
        reversePoint = n // 2
        if n % 2 == 1:
            reversePoint += 1

        head2 = self.findPos(head, reversePoint)
        prev = self.findPos(head, reversePoint - 1)

        self.reverse(head2, prev)

        fp = head
        sp = prev.next

        while fp is not None and sp is not None:
            if fp.val != sp.val:
                return False
            fp = fp.next
            sp = sp.next
        return True

    def findLength(self, node):
        length = 0
        curr = node
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def findPos(self, node, pos):
        count = 0
        curr = node
        while count < pos:
            count += 1
            curr = curr.next
        return curr

    def reverse(self, head, prev):
        a = head  # a = 5
        b = head.next  # b = 4
        while a is not None and b is not None:
            c = b.next  # c = 2  c = 1 c=None
            b.next = a  # b.next = 5 b.next = 4 b.next = 2
            a = b  # a = 4 a = 2 a = 1
            b = c  # b = 2 b = 1 b=None

        head.next = None
        prev.next = a

        # curr = a
        # while curr is not None:
        #     print(curr.val)
        #     curr = curr.next

# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l1.next.next.next = ListNode(5)
# l1.next.next.next.next = ListNode(3)
# l1.next.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next.next = ListNode(4)
# l1.next.next.next.next.next.next.next = ListNode(2)
# l1.next.next.next.next.next.next.next.next = ListNode(1)
#
# print(PalindromeLinkedList().isPalindrome(l1))


class LinkedListCycleII:
    """
    Fast and slow pointer theorem to find the intersection point.

    Once we found the intersection point, move the starting node and intersection node together.
    They will meet at the start of the cycle.
    """

    def detectCycle(self, head):
        slow = head
        fast = head

        while True:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                insPoint = slow
                break
        start = head
        while start != insPoint:
            start = start.next
            insPoint = insPoint.next
        return start


l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next


# print(LinkedListCycleII().detectCycle(l1))


class MiddleOfTheLinkedList:
    """
    We will use two pointer algorithm fast and slow pointers.
    Slow pointer moves one node a time. Fast pointer moves two nodes at a time.

    When fast pointer reaches the end, wherever the slow pointer is - that will be the middle element.

    Mathematically, fast pointer moves 2x finishes at n, 2x = n so x = n/2.
    """

    def middleNode(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


class RemoveNthNode:
    """
    We will use fast and slow pointer approach here where the fast pointer moves n+1 times.

    Then move both the fast and slow pointer one node at a time until fast is null.

    When the fast pointer moves to end, slow pointer will be at n - 1 node since we maintained
    n + 1 distance between them.

    Finally, s.next = s.next.next
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast is None:  # only one node
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


class RemoveDuplicatesFromSortedList:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)


# node = RemoveDuplicatesFromSortedList().deleteDuplicates(node)


class SwapNodesInPairs:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            temp = curr
            curr = curr.next
            curr.next = temp
        return head


node = SwapNodesInPairs().swapPairs(node)

while node is not None:
    print(node.val)
    node = node.next
