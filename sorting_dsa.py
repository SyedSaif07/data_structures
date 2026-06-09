from typing import List


def bubble_sort(l):
    """
    Compare each element with its next neighbour and shift elements accordingly.

    So that the largest element settles at the end,
    and we iterate again until n-1 to shift the second largest to the second last,
    and we iterate again until n-2 to shift the third largest to the third last

    Complexity : O(N**2)
    """

    n = len(l)

    for i in range(n):  # driver
        for j in range(n - i - 1):  # driven
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l


# print(bubble_sort(l=[10, 20, 50, 40, 15, 25]))


def selection_sort(l):
    """
    Keep swapping the smallest element to the beginning of the array.

    Once the first smallest is swapped at 0th index then array window becomes 1 to n
    the second smallest is swapped to 1st index then array window becomes 2 to n

    Complexity : O(N**2)
    """

    n = len(l)

    def find_minimum(idx, arr):
        minimum_idx = idx
        for j in range(idx, n):  # WINDOW idx to n where idx=0,1,2..n
            if arr[j] < arr[minimum_idx]:
                minimum_idx = j
        return minimum_idx

    for i in range(n):  # driver
        small_index = find_minimum(i, l)
        l[small_index], l[i] = l[i], l[small_index]

    return l


# print(selection_sort(l=[10, 20, 50, 40, 15, 25]))

def insertion_sort(l):
    """
    Considering our 0th element is already sorted meaning "Single element array is sorted".

    Pick the element from the unsorted array i.e 1 to n and insert in its place. The 1st element is compared with the
    0th,and it is inserted at its place. Now sorted part is increased to 0,1.

    The 2nd element is compared with the 0th & 1st
    elements and inserted at its place.Now sorted part is increased to 0,1,2.

    The nth element is compared with the
    previous elements and inserted at its place

    Complexity : Best case : O(N) Worst case O(N**2)
    """
    n = len(l)

    for i in range(1, n):
        while i > 0:
            if l[i] < l[i - 1]:
                l[i - 1], l[i] = l[i], l[i - 1]  # a,b = b
            else:
                break
            i -= 1
    return l


# print(insertion_sort(l=[10, 20, 50, 40, 15, 25]))


def merge_sorted_arrays(a, b):
    """
    How to merge two sorted arrays?
        Take two pointers i, j for two sorted arrays A and B.
        One counter k for third array C which will contain the merged sorted array.

        Initially i=j=k=0

        Compare A[i] and B[j] whichever is smaller insert in C[k].
        Assuming A[i] < B[j], C[k] = A[i] - Now i=1, j=0, k=1

        Compare A[i] i.e A[1] and B[j] i.e B[0] whichever is smaller insert in C[k].
        Assuming A[i] > B[j], C[k] = B[j] - Now i=1, j=1, k=2

        Keep repeating this until all the elements are added in sorted order in array C

        If one of the arrays in finished, then add the all the remaining elements of the other array in C

        Complexity of merging two sorted arrays : O(N+M) which is linear
    """
    n = len(a)
    m = len(b)
    c = [0] * (n + m)

    i = j = k = 0

    while i < n or j < m:  # Keep the while loop active as long as there is an element remains in any array
        if i < n and j < m:  # As long as both arrays have elements before one of each array finishes
            if a[i] <= b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
        elif i < n:  # If elements of array A still remains
            c[k] = a[i]
            i += 1
        else:  # If elements of array B still remains
            c[k] = b[j]
            j += 1
        k += 1

    return c


def mergeSort(myList):
    """
    Firstly split the array l in two equal arrays i.e. left side array and right side array

    Then split the those two arrays into two arrays of each array from the left and right

    Repeat this until you get arrays of size 1 on both sides

    Use this rule "Single element array is sorted" - Now we have two sorted arrays of size 1

    Merge the size 1 array using merge_sorted_arrays to get sorted size 2 arrays

    Repeat this to get equal sized two sorted arrays and then finally merge them to get the final sorted array

    """

    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # print("Step1", left, right)
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            # print("Step2", i, j, left, right)
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            # print("Step3", i, left)
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            # print("Step4", j, right)
            myList[k] = right[j]
            j += 1
            k += 1


#
# myList = [54, 26, 93, 17]
# mergeSort(myList)
# print(myList)


class MergeSortedArrays:
    """
    To solve this we start filling from the end with the largest number.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1


# print(MergeSortedArrays().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

def partition_algorithm():
    """
    Partition function: P(arr, key) => To place the key at the correct position and the key
                        has to be within the array.
                        Eg: arr [2,5, 1, 0, 4, 6, 3] key=3
                        Arrange in such a way that the left side of key is less than 3
                        and the right side elements are greater than 3.
                        This is called partitioning into three parts.
                        First part - less than key
                        Second part - Equal to key
                        Third part - Greater than key
                        2 1 0 3 5 4 6 - Partitioning itself is not sorting. It is to arrange
                        element in this desired structure.

                        How to do partitioning? It always assumes that the key is at the end.
                        initially left = -1
                        We have to go over the elements from left to right.If I find the element
                        less than key we will shift it to left of key.

                        if arr[i] < key:
                            left += 1
                            arr[i], arr[left] = arr[left], arr[i]

                        for i =0, 2 < 3
                        left = 0
                        arr[0],arr[0] = arr[0],arr[0]

                        for i=1, 5 > 3 so skip it

                        for i=2, 1 < 3
                        left =1
                        arr[2],arr[1] = arr[1],arr[2]

                        2 1 5 0 4 6 3

                        for i=3, 0 < 3
                        left = 2
                        arr[3],arr[2] = arr[2],arr[3]

                        2 1 0 5 4 6 3

                        for i =4 4 > 3 so skip it

                        for i =5 6 > 3 so skip it

                        now we have reached the end, we know that until left = 2 all the elements
                        where less than 3, so we do once again,
                        left += 1 which is 3

                        arr[6],arr[3] = arr[3],arr[6]

                        2 1 0 3 4 6 5
    Advantage of partitioning is all the elements that are equal to key end up in correct position.
    Here 3 is in its correct position.
    """
    a = [1, 5, 2, 6, 0, 4, 3]
    n = len(a)
    key = a[n - 1]
    left = -1

    for i in range(n - 1):
        if a[i] <= key:
            left += 1
            a[i], a[left] = a[left], a[i]

    left += 1  # This is when we reached the element before our key
    a[n - 1], a[left] = a[left], a[n - 1]

    print(a)


partition_algorithm()


# a = [10, 50, 40, 20, 15, 16, 2, 3, 8, 9, 99, 34, 43, 100, 121, 104, 132]
a = [1, 5, 2, 6, 0, 4, 3]


def partition(start, end):
    left = start - 1
    pivot = a[end]  # key
    for i in range(start, end):
        if a[i] <= pivot:
            left += 1
            a[left], a[i] = a[i], a[left]
    left += 1
    a[end], a[left] = a[left], a[end]
    return left  # this is the partition point


def quick_sort(left, right):
    """
    Quick sort takes advantage of partitioning.

    2 5 1 0 4 3 key = 3
    2 1 0 3 4 5 after partitioning.

    Recursively do the same thing for elements before key and after key.

    Partition point is index 3.

    Best case or Average case:  TC:O(NlogN) SC:O(logN)
    Worst case if the array is already sorted: O(N**2)
    """
    if left < right:
        partition_point = partition(left, right)
        quick_sort(left, partition_point - 1)  # elements in the left before partition point
        quick_sort(partition_point + 1, right)  # elements in the right after partition point


quick_sort(0, len(a) - 1)
print(a)


class MoveZeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # fp = 0
        # sp = 1
        # while n > sp > fp:
        #     if nums[sp] != 0:
        #         if nums[fp] == 0:
        #             nums[fp], nums[sp] = nums[sp], nums[fp]
        #             fp += 1
        #             sp += 1
        #         else:
        #             fp += 1
        #             sp = fp + 1
        #     else:
        #         sp += 1
        # return nums

        non_zero = 0  # Pointer for non-zero elements

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
        return nums


# print(MoveZeroes().moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))


class MajorityElement:
    """
    Boye moore voting algorithm: This is only applicable if the majority element exists.
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


# print(MajorityElement().majorityElement([3, 3, 4]))


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1

        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        return nums

# print(SortColors().sortColors([2,0,2,1,1,0]))
