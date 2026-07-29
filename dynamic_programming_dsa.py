"""
It is a technique using which we optimize problems.

Eg: Fibonacci series:
    0, 1, 1, 2, 3, 5, 8, 13
    f(i) = ith fibonacci
    f(i) = f(i-1) + f(i-2)

    Optimal substructure: Solving the problem by combining the solution its sub problem.

    Overlapping Sub problem: Trying to solve the same sub problem again and again.

    Memoization: When you compute something for the first time, store it so that it
                 can be used later on. Similar to cache.

    Compute sub problems in the correct order.
"""
from collections import deque
from typing import List


class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        prev1 = 3
        prev2 = 2

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return cur


# print(ClimbingStairs().climbStairs(45))


class JumpGame:
    def canJump(self, nums) -> bool:
        max_reachable = nums[0]
        i = 1
        while i < len(nums) and max_reachable >= i:
            if i + nums[i] > max_reachable:
                max_reachable = i + nums[i]
            i += 1
        if max_reachable >= len(nums) - 1:
            return True
        else:
            return False

    def canJump1(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


# print(JumpGame().canJump1([2, 3, 1, 1, 4]))


class CoinChangeDP:
    def __init__(self):
        self.coins = None
        self.dp = {}

    def coinChange(self, coins, amount: int) -> int:
        self.coins = coins
        return self.f(amount)

    def f(self, i):
        if i == 0:
            return 0
        if i < 0:
            return -1

        if i in self.dp:
            return self.dp[i]

        ans = -1

        for coin in self.coins:
            val = self.f(i - coin)
            if val != -1 and (ans == -1 or val + 1 < ans):
                ans = val + 1

        self.dp[i] = ans
        return ans

    def coinChangeBFS(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([(0, 0)])  # (current_sum, steps)
        visited = {0}

        while queue:
            curr, steps = queue.popleft()

            for coin in coins:
                nxt = curr + coin

                if nxt == amount:
                    return steps + 1

                if nxt < amount and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1


# print(CoinChangeDP().coinChange([1, 2, 5], 4))


class PartitionEqualSubsetSum:
    """
    To partition the array into two parts, we can find the half of total sum of nums.

    We keep adding the total (by summing one number at first and summing the next number to
    the calculated sum and adding the next number to the added sum of two numbers)

    If we find the target during the summing operation or after the whole dp is calculated,
    we return True.
    """

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)  # initial sum to be zero

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t)
                nextDp.add(t + nums[i])  # Summing of one element and two elements and so on.
            dp = nextDp
        return True if target in dp else False


# print(PartitionEqualSubsetSum().canPartition(nums = [1,5,11,5]))

class TargetSum:
    """
    f(i, current_target) => returns no of ways to form current target starting
    from position i.

    nums = [1,1,1,1,1], target = 3, initially f(0, target) i.e f(0,3)

    I have two options either +1 or -1
    f(0,3) =  f(1,2) + f(1,4) => f(1,2) when +1, so we need to form +2 from the remaining elements
                                 to satisfy the target.
                                 f(1,4) when -1, so we need to for +4 from the remaining elements
                                 to satisfy the target.
    f(1,2) = f(2,1) + f(1,3)

    i = n - 1, if |arr[i]| == CT where CT is 1, arr[i] = 0, I can do +0 or -0 so 2.
                                                arr[i] = 1, so 1.
                                                ct != arr[i], then 0.

    f(i, ct) => f(i+1, ct + arr[i]) + f(i+1, ct-arr[i])
    """

    def __init__(self):
        self.h = {}
        self.nums = None

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        dp = {}

        def f1(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in self.h:
                return self.h[(i, total)]
            dp[(i, total)] = (f1(i + 1, total + nums[i]) + f1(i + 1, total - nums[i]))

            return dp[(i, total)]

        # return self.f(0, target)
        return f1(0, 0)

    def f(self, i, ct):
        if i < len(self.nums) - 1:
            key = (i, ct)
            if key in self.h:
                return self.h[key]
            self.h[key] = self.f(i + 1, ct - self.nums[i]) + self.f(i + 1, ct + self.nums[i])
            return self.h[key]
        else:
            if ct == 0 and self.nums[i] == 0:
                return 2
            elif abs(ct) == abs(self.nums[i]):
                return 1
            else:
                return 0


# print(TargetSum().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))


class LongestCommonSubsequence:
    """
    Longest common subsequence of any string are character picked from the parent string
    but in the same order and not necessarily continuous.

    Eg: s1 "abcde" s2 "ace" -  LCS is "ace".

    f(i,j) => LCS[s1[0,...i], s2[0,...j]] i.e s1[i] == s2[j]
    f(4,3) = 1 + f(3,2)
             1 is added because 'e' is common.

             f(3,2) s1[i] i.e "d" != s2[j] i.e "c"
             so we move s1 pointer or s2 pointer

             max(f(2,2), f(3,1)) => 2,2 if s1 pointer is moved and 3,1  if s2 pointer is moved.

    f(i,j) => f(i-1, j-1) + 1 if s1[i] == s2[j]
                    or
              max(f(i-1,j),f(i, j-1)

    Base case if i = -1 or  j = -1 there is nothing to compare return 0.

    """

    def __init__(self):
        self.text2 = None
        self.text1 = None
        self.dp = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        n = len(text1)
        m = len(text2)
        return self.lcs(n - 1, m - 1)

    def lcs(self, i, j):
        if i == -1 or j == -1:
            return 0
        else:
            if (i, j) not in self.dp:
                if self.text1[i] == self.text2[j]:
                    self.dp[(i, j)] = self.lcs(i - 1, j - 1) + 1
                else:
                    self.dp[(i, j)] = max(self.lcs(i - 1, j), self.lcs(i, j - 1))
            return self.dp[(i, j)]


text1 = "abcde"
text2 = "ace"


# print(LongestCommonSubsequence().longestCommonSubsequence(text1, text2))


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans

        return s[i: j + 1]


# print(LongestPalindrome().longestPalindrome('racecard'))


class HouseRobber:
    """
    f(i, canRob) max value that I can rob by robbing ith house. canRob tells me whether
    I can rob that house or not.

    f(0, True) => means by default 0th house can be robbed. It does not mean I have to rob it.
                  We can choose to rob it or not.

                  Eg: nums = [2,1,3,9]
                  If I chose to rob it, then
                  f(0, True) = nums[0] + f(1, False) => canRob is False here because previous house is robbed.

                  If I chose not to rob it, then
                  f(0, True) = f(1, True)

                  Finally f(0, True) => max( nums[0] + f(1, False), f(1, True) )

    f(1, False) => f(2, True)
                   f(1, True) => nums[1] + f(2, False)

                   max( nums[1] + f(2, False), f(2, True) )

    Last base case, when I'm at the end and if I can rob the house it is better to rob it.
    """

    def __init__(self):
        self.nums = None
        self.dp = {}

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.f(0, True)

    def f(self, i, canRob):
        if i == len(self.nums) - 1:
            if canRob:
                return self.nums[i]
            else:
                return 0
        else:
            if (i, canRob) not in self.dp:
                if canRob:
                    self.dp[(i, canRob)] = max(self.nums[i] + self.f(i + 1, False), self.f(i + 1, True))
                else:
                    self.dp[(i, canRob)] = self.f(i + 1, True)
            return self.dp[(i, canRob)]


# nums = [1, 2, 3, 1]
# print(HouseRobber().rob(nums))


class LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        ans = 1

        for i in range(1, len(nums)):
            currentVal = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    currentVal = max(currentVal, dp[j] + 1)
            dp.append(currentVal)
            ans = max(ans, dp[i])
        return ans


# print(LongestIncreasingSubsequence().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start: i] == w:
                    dp[i] = True
                    break
        return dp[-1]


# print(WordBreak().wordBreak(s="leetcode", wordDict=["leet", "code"]))


class DecodeWays:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0" or not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            oneDigit = int(s[i - 1:i])
            twoDigit = int(s[i - 2:i])
            if 1 <= oneDigit <= 9:
                dp[i] += dp[i - 1]
            if 10 <= twoDigit <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


# print(DecodeWays().numDecodings(s="226"))


class UniquePaths:
    """
    There is a robot on an m x n grid.
    The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths
    that the robot can take to reach the bottom-right corner.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i - 1] + aboveRow[i]
            aboveRow = currentRow
        return aboveRow[-1]


print(UniquePaths().uniquePaths(23, 12))
