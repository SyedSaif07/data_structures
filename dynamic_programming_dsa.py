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


# print(JumpGame().canJump([2, 3, 1, 1, 4]))


class CoinChangeDP:
    def __init__(self):
        self.coins = None
        self.dp = None

    def coinChange(self, coins, amount: int) -> int:
        self.dp = {}
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


print(CoinChangeDP().coinChange([1, 2, 5], 2))
