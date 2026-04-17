"""
For a sliding window algorithm, start the two pointers from the beginning.

Now move the 2nd pointer one step. Check for valid condition.

If valid move the 2nd pointer again one step and check for valid condition. If not valid, then shrink the window,
by moving the 1st pointer one step and check for valid condition.

Keep doing this until the 2nd pointer reaches the end.

This is process of creating the window by keeping the 1st pointer stationary and
moving the 2nd pointer. Sliding the window by moving the 2nd pointer as long as it meets
valid condition. Shrink the window by moving the 1st pointer when valid condition is not
met.
"""

from collections import deque
from typing import List


class LongestSubstringLength:
    def addTodict(self, ht, ch):
        if ch not in ht:
            ht[ch] = 1
        else:
            ht[ch] += 1

    def removeFromdict(self, ht, ch):
        ht[ch] -= 1

    def isValid(self, ht):
        for ch in ht:
            if ht[ch] > 1:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        fp = 0
        sp = 0
        ans = 0
        ht = {}
        while sp < n:
            self.addTodict(ht, s[sp])
            while fp < sp and not self.isValid(ht):
                self.removeFromdict(ht, s[fp])
                fp += 1
            length = sp - fp + 1
            ans = max(ans, length)
            sp += 1
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    def lengthOfLongestSubstring3(self, s: str) -> int:
        """
        Even Better (Most Optimal Pattern) by ChatGPT

        You can improve further using a hashmap (index jump):
        Index-map jump (best)
        ✅ O(n)
        🔥 Best

        character-to-index map — jump
        """
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length


# print(LongestSubstringLength().lengthOfLongestSubstring2("abcabcbb"))

class SlidingWindowMaximum:
    """
    An element becomes useless when

        It is not a part of the current window.
        For a window size of k, the last element of that window is at j, then the start element of the
        window is at j-k + 1. Pop from the left.

        If a high value element is found on the right side of it. Pop from the right.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        de = deque()
        n = len(nums)
        de.append(0)
        for i in range(1, k):
            while len(de) > 0 and nums[de[-1]] < nums[i]:
                de.pop()
            de.append(i)
        ans.append(nums[de[0]])

        for j in range(k, n):
            start_pos = j - k + 1
            while len(de) > 0 and de[0] < start_pos:
                de.popleft()
            while len(de) > 0 and nums[de[-1]] < nums[j]:
                de.pop()
            de.append(j)
            ans.append(nums[de[0]])
        return ans


# print(SlidingWindowMaximum().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
