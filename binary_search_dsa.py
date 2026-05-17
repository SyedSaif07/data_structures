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
from typing import List


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


class FirstAndLastPositionOfElementInSortedArray:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        return [left, right]

    def findLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        return ans

    def findRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                start = mid + 1
        return ans


# print(FirstAndLastPositionOfElementInSortedArray().searchRange([5, 7, 7, 8, 8, 10], 8))


class FindMinimumInRotateSortedArray:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        ans = nums[0]

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= nums[-1]:
                ans = nums[mid]
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def findMin1(self, nums):
        n = len(nums)
        start = 0
        end = n - 1
        ans = nums[0]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                ans = nums[mid]
                end = mid - 1
        return ans

    def findMin3(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


# print(FindMinimumInRotateSortedArray().findMin3([6, 7, 0, 1, 2, 3, 4, 5]))


class SearchInARotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= nums[0] > target:
                start = mid + 1
            elif nums[mid] < nums[0] <= target:
                end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    ans = mid
                    break
        return ans

    def search1(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# print(SearchInARotatedSortedArray().search1([6, 7, 0, 1, 2, 3, 4, 5], 4))


class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return mid + 1 if target > nums[mid] else mid


# print(SearchInsertPosition().searchInsert([1, 3, 5, 6], 0))
