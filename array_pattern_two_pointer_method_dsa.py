from typing import List


class TwoPointerTwoSum:
    """
    This two pointer method only works for sorted array.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp = 0
        sp = len(numbers) - 1
        while fp < sp:
            currSumm = numbers[fp] + numbers[sp]
            if currSumm < target:
                fp += 1
            elif currSumm > target:
                sp -= 1
            else:
                return [fp + 1, sp + 1]


class TrappingRainWater:
    """
    Find max height on the right side and find max height on the left side.

    Get the minimum of the two and subtract it with the bar height if any to get the height
    trapped water.
    """

    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        right[n - 1] = height[n - 1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        print(left, right)
        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
        return ans


# print(TrappingRainWater().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        return res


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# k = RemoveDuplicatesFromSortedArray().removeDuplicates(nums)
# print(nums)
# print(nums[:k])
