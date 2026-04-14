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
                l[i - 1], l[i] = l[i], l[i - 1] # a,b = b
            else:
                break
            i -= 1
    return l


print(insertion_sort(l=[10, 20, 50, 40, 15, 25])) 


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

# myList = [54, 26, 93, 17]
# mergeSort(myList)
# print(myList)
