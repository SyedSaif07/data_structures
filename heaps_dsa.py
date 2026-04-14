"""
Heaps is a special type of binary tree which has two properties.
    1. Complete binary tree
    2.
       a. node.data > node.left.data, node.right.data
       b. node.data <= node.left.data, node.right.data

    Follow 1 + 2a to get Max heap or 1 + 2b to get Min heap

In a max heap, always the maximum element in the top.
In a min heap, always the minimum element in the top.

Complete binary tree : All levels must be filled except last level.
                       Last level can be partially filled.

                       Levels should always start filling from
                       left side.

Following this, implementation of heap is easier and addition/removal is O(logN)

For any node its children can be accessed in a stack like
Left child will be at 2i + 1 Right child will be at 2i + 2

For any child, its parent will be at (i-1)/2

"""
import heapq


def kth_largest_element_array(nums, k):
    """
    Using min heap we can get min heap of top k elements. So the top of the min heap is
    the answer to the kth largest element in an array.

    Smallest number among the highest K numbers is the Kth largest element.
    """
    arr = nums[:k]
    heapq.heapify(arr)

    for i in range(k, len(nums)):
        if nums[i] >= arr[0]:
            heapq.heappush(arr, nums[i])
            heapq.heappop(arr)
    return arr[0]


# print(kth_largest_element_array([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


class MedianFinder:
    """
    In a sorted stream, given number of elements is even, median is the average of the highest number in lower half
    and lowest number in upper half.

    Max heap for the lower half to get the highest smallest number.
    Min heap for the upper half to get the lowest largest number.

    Two rules:
        Max heap should always contain the numbers in the lower half and min heap should always
        contain the number in the upper half.

        Size of min heap can never be greater than the size of max heap.

        Max heap size can be greater than min heap size not more than 1.
        Size difference of max heap and min heap cannot be greater than 1.

        Highest element of the max heap should always be lesser than the lowest element
        of the min heap.

    Always we start pushing to max heap first.

    """

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, - num)  # minus to create a max heap

        heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap,
                           - heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return - self.maxHeap[0]
        else:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(2)
# obj.addNum(5)
# obj.addNum(1)
# obj.addNum(7)
# obj.addNum(4)
# param_2 = obj.findMedian()
# print(param_2)

class KthLargestStream:
    """
    Store highest k elements seen so far in the min heap. Whichever is the smallest of that
    heap is the kth highest element in a stream.
    """

    def __init__(self, k: int, nums):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)

        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]

    def printKLargest(self):
        print(self.minHeap[0])


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargestStream(3, [1, 7, 9, 54, 0])
# obj.printKLargest()
