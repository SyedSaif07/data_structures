"""
LIFO - Last in First Out
Python lists can be used as stack but if there are many elements then finding
that chunk of contiguous memory will be tedious with lists.

Deque means double ended queue which gives pushing at the right and
popping at the right or pushing at the left and popping at the left.

We can use deque as stacks. Stack is ADT - Abstract Data type.

Deque solves the case for many elements because it does not require contiguous memory.

"""


# from collections import deque
# st = deque()

# st.append(10)
# st.append(15)
# st.append(20)
# st.append(30)
#
# print(st[-1])
#
# st.pop()
#
# print(st[-1])
#
# st.pop()

# print(st[-1])


def valid_parenthesis(s):
    """
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
    """

    def does_match(op, cl):
        return (op == "{" and cl == "}") or (op == "(" and cl == ")") or (op == "[" and cl == "]")

    st = []
    for i in s:
        if i in {'(', '{', '['}:
            st.append(i)
        else:
            if len(st) == 0:
                return False
            else:
                if does_match(st[-1], i):
                    st.pop()
                else:
                    return False
    if len(st) == 0:
        return True
    else:
        return False


# print(valid_parenthesis("([)]"))


def reverse_polish_notation(tokens):
    """
    Operators come after operands - this is called postfix notation to avoid the usage
    of brackets when writing mathematical expressions.

    Once an operator is seen, the two operands before it must be popped and
    calculation must be performed and appended in the stack.
    """
    st = []

    def is_operator(op):
        return op in {"+", "-", "*", "/"}

    def perform_operation(opr, value1, value2):
        if opr == "+":
            return value2 + value1
        elif opr == "-":
            return value2 - value1
        elif opr == "*":
            return value2 * value1
        elif opr == "/":
            return value2 / value1

    for token in tokens:
        if is_operator(token):
            fop = st.pop()
            sop = st.pop()
            result = perform_operation(token, fop, sop)
            st.append(int(result))
        else:
            st.append(int(token))
    return st.pop()


# print(reverse_polish_notation(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


class MinStack:
    """
    This will create all the standard methods like push pop top getMin of a stack.

    For getMin, we will do a tradeoff with space to reduce time complexity by using
    an auxiliary stack which is another stack whose purpose is to just store the
    minimum elements. This increases the space as we store additional auxiliary stack
    but reduces time complexity.

    """

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, val: int) -> None:
        self.a.append(val)
        if len(self.b) == 0 or val <= self.b[-1]:
            self.b.append(val)

    def pop(self) -> None:
        if len(self.a) > 0:
            if self.a[-1] == self.b[-1]:
                self.b.pop()
            self.a.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]


def nextGreaterElementOne(nums1, nums2):
    # h_table = {}
    # ans = [-1] * len(nums1)
    # for i in range(len(nums2)):
    #     h_table[nums2[i]] = i
    #
    # for k in range(len(nums1)):
    #     idx = h_table[nums1[k]]
    #     while idx < len(nums2):
    #         if nums2[idx] > nums1[k]:
    #             ans[k] = nums2[idx]
    #             break
    #         idx += 1
    # return ans
    """
    Better approach to use monotonic decreasing stack.
    """
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    for num in stack:
        next_greater[num] = -1

    return [next_greater[num] for num in nums1]


# print(nextGreaterElementOne([4, 1, 2], [1, 3, 4, 2]))

def nextGreaterElementTwo(nums):
    """
    NGE is the next greater element that comes to the right of the element.

    Stack is used to store the positions for which we haven't found the
    next greater element yet.
    """
    n = len(nums)
    ans = [-1] * n
    stack = [0]

    for i in range(1, n):
        current = nums[i]
        while stack and nums[stack[-1]] < current:
            ans[stack.pop()] = current
        stack.append(i)

    for i in range(n):
        current = nums[i]
        while stack and nums[stack[-1]] < current:
            ans[stack.pop()] = current
    return ans


# print(nextGreaterElementTwo([1, 2, 3, 4, 3]))

def merge(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))
    result = [[intervals[0][0], intervals[0][1]]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= result[-1][-1]:
            result[-1][-1] = max(interval[1], result[-1][-1])
        else:
            result.append([interval[0], interval[1]])
    return result

# print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))