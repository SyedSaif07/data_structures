li = [(i, j) for i in range(5) for j in range(4)]
# print(li)

li_2d = [[0 for i in range(3)] for i in range(3)]
# print(li_2d)

a = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1]


def max_ones(a):
    count = 0
    ans = 0
    for i in a:
        if i == 1:
            count += 1
        else:
            count = 0
        ans = max(count, ans)
    return ans


# print(max_ones(a))


def buy_and_sell(l):
    buy = l[0]
    ans = 0
    for i in range(1, len(l)):
        if buy < l[i]:
            ans = max(ans, l[i] - buy)
        else:
            buy = l[i]
    return ans


# print(buy_and_sell([7, 1, 3, 4, 6, 2, 7, 1, 10]))


def product_except_self(l):
    n = len(l)
    left = [1] * n
    right = [1] * n
    output = []

    for i in range(1, n):
        left[i] = left[i - 1] * l[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * l[i + 1]

    for i in range(n):
        output.append(left[i] * right[i])

    return output


# print(product_except_self([5, 2, 3, 4]))


'''Rotate array k times

Algorithm
1. Divide k by n i.e len(arr) because if k is greater than n 
and rotating the arr n times gets the same array so it is better to skip n rotations
by dividing k by n 

2. reverse the entire arr

3. reverse k elements first

4. reverse n-k elements
'''


def rotate_arr(nums, k):
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


def reverse(nums, start, end):
    i = start
    j = end

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


# print(rotate_arr([1, 2, 3, 4, 5, 6, 7], k=3))


# Maximum subarray

def maximum_subarray(nums):
    ans = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        ans = max(ans, current_sum)
    return ans


# print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def max_product(nums):
    maxPr = nums[0]
    minPr = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] >= 0:
            maxPr = max(nums[i], maxPr * nums[i])
            minPr = min(nums[i], minPr * nums[i])
        else:
            temp = maxPr
            maxPr = max(nums[i], minPr * nums[i])
            minPr = min(nums[i], temp * nums[i])
        result = max(maxPr, result)
    return result


# print(max_product([2, 3, -2, 4]))


def valid_sudoku(board):
    rowSet = [set() for _ in range(9)]
    colSet = [set() for _ in range(9)]
    gridSet = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            grid = (i // 3 * 3) + (j // 3)
            # if i=0,1,2 then grid will be j//3
            # if i=3,4,5 then grid will be j//3 + 3
            # if i=6,7,8 then grid will be j//3 + 6
            # or general formula j//3 + (i//3 * 3)
            presentInRow = board[i][j] in rowSet[i]
            presentInCol = board[i][j] in colSet[j]
            presentInGrid = board[i][j] in gridSet[grid]

            if presentInRow or presentInCol or presentInGrid:
                return False
            rowSet[i].add(board[i][j])
            colSet[j].add(board[i][j])
            gridSet[grid].add(board[i][j])
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# print(valid_sudoku(board))
