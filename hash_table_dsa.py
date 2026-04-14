"""
Overview:
    Hash function is a special type of function i.e. pure function - stateless processing and
    produces the same output always. Eg: h('toyota') = 79 always.

    Chances of collision is very less - for h('toyota') it outputs 79 there is no other value
    for which it will output 79.

    When you create a hash table, any programming language internally creates an array of size n eg:7
    Eg: ht.update({"toyota":67}).

    Steps:
        Compute hash value of key which is "toyota" using hash function -
        hash value of toyota is 79.

        Take mod value of 79 w.r.t 7 - 79 % 7 = 2 (used for index in the array).

        The value for toyota which is 67 will be stored in the 2nd index of the array.

Collisions:
    Collisions mean two keys get mapped to the same index either hash function gives
    the same output for two different keys or getting the same index during the mod
    operation.

    Eg: h("toyota")=79 h("Tesla")=1034 h("VW")=51
    The mod of 79 and 51 is 2 which means there is a collision for "toyota" and "VW".

    The more the collisions there is a decrease in performance of the hash table.

    The Complexity of hash table is O(1).

    The fix collisions the common technique used is called as Chaining.

    During chaining, we create a linked list for that index and create nodes for each key.
    In this case, a node for "toyota" and its value and a node for "VM" and its value.

    The problem occurs when getting the value ht.get("toyota") = 79 which gives 2nd index.
    In the worst case, all the n keys can come in the same index slot. If we have to
    find the specific key, we have to traverse through the linked list - the worst case
    the value can be at the end of the linked list which makes the complexity O(N).

    In an unordered hash table - the best case is O(1) if there are no collisions.
    average case will also be O(1) amortized. amortized means most of the case is O(1)
    sometimes there can be O(N) due to collisions.

Hash Table Types:
    Unordered hash table:
        Time complexity - worst case O(N) which is very rare | average O(1) amortized.
        Frequently used.

    Ordered hash table:
        Uses a Balanced Binary Search Tree instead of an array.
        Time Complexity: worst O(log n) | average O(log n).
        The advantage of ordered over unordered is the worst case scenario which is
        better in ordered hash table.
        The disadvantage of ordered hash table is its average case is higher than
        the unordered hash table.

"""

from collections import OrderedDict

ht = OrderedDict()

ht["Toyota"] = 67
ht["Tesla"] = 50


# for i in ht:
#     print(i)

def contains_duplicate(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            return True
    return False


# print(contains_duplicate([1, 2, 3, 1]))

def group_anagram(strs):
    """
    An anagram is a word which is formed by jumbling its letters.
    Eg: ate, eat, tea
    """
    h_table = {}
    for item in strs:
        key = "".join(sorted(item))
        if key not in h_table:
            h_table[key] = []
        h_table[key].append(item)
    ans = []
    for i in h_table:
        ans.append(h_table[i])
    return ans


# print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))


def two_sum(nums, target):
    h_table = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in h_table:
            return [i, h_table[diff]]
        h_table[nums[i]] = i

    return nums


# print(two_sum([2,7,11,15], 9))


def three_sum(nums):
    data = set()
    nums.sort()

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if temp == 0:
                data.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif temp < 0:
                j += 1
            else:
                k -= 1
    return list(data)


# print(three_sum([-1, 0, 1, 2, -1, -4]))


def longest_consecutive_sequence(nums):
    longest = 0
    num_set = set(nums)

    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest


print(longest_consecutive_sequence([0, 0, -1]))
