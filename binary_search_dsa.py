"""
Binary search is a searching technique for sorted arrays or sorted ranges.

For linear search, the time complexity is O(N) which is not good.
Best case O(1) Worst case O(N) Average case O(N). This is acceptable for unsorted arrays.

Binary search can only be applied for sorted arrays. Time Complexity is logN

Steps:
    Define the search space - finding the value in that area or range. Initially it
    will be the entire array.

    Choose the midpoint of the space.
    If the value is lesser than the midpoint value, then the value must be in the left of midpoint.
    If the value is greater than the midpoint value, then the value must be in the right of midpoint.

    Now the search space is reduced to half.

    Repeat this process to get the exact element matching midpoint.

"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return -1


# print(binary_search([1, 5, 7, 10, 15, 78, 99], 5))
