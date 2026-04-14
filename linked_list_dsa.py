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


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

head = a
a.next = b
b.next = c
c.next = d


# head = None


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
#
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
            data = None
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
        self.newHead = None
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
