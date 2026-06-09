"""
1. Go over all configurations. 2. Construct the solution step by step.

Backtracking is a technique to go back and change the previous implementation so that
the current scenario becomes valid. Because the previous implementation lead us to dead-end.

Eg: Generate all possible subsets of an array containing N elements.
[1,2,3]
Start from the beginning - we have two decisions include the element or exclude the element.

"""
from typing import List


class CombinationSum:
    """
    [2, 3, 6, 7] target = 7
    f(i, remainder, combination)
    Initially f(0, 7, [])
                |
    f(1, 7, []) f(1, 5, [2]) f(1, 3, [2,2]) f(1, 1, [2,2,2])

    Like this we will try all the combinations.
    """

    def __init__(self):
        self.answers = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answers = []
        self.f(0, target, [], candidates)
        return self.answers

    def f(self, i, rem, combinations, candidates):
        if i == len(candidates):
            if rem == 0:
                self.answers.append([num for num in combinations])
        else:

            maxTimes = rem // candidates[i]
            for k in range(maxTimes + 1):
                newTarget = rem
                for j in range(k):
                    combinations.append(candidates[i])
                    newTarget -= candidates[i]
                self.f(i + 1, newTarget, combinations, candidates)
                for j in range(k):
                    combinations.pop()


# print(CombinationSum().combinationSum([2, 3, 6, 7], 7))


class Subsets:
    def __init__(self):
        self.nums = None
        self.subset = []
        self.subsets = []

    def getSubsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack(0)
        return self.subsets

    def backtrack(self, i):
        if i == len(self.nums):
            ans = []
            for num in self.subset:
                ans.append(num)
            self.subsets.append(ans)
        else:
            self.backtrack(i + 1)

            self.subset.append(self.nums[i])
            self.backtrack(i + 1)
            self.subset.pop()


# print(Subsets().getSubsets([1, 2, 3]))


class GenerateParentheses:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, s):
            if open == close and open + close == n * 2:
                res.append(s)
                return

            if open < n:
                backtrack(open + 1, close, s + "(")

            if close < open:
                backtrack(open, close + 1, s + ")")

        backtrack(0, 0, "")
        return res


# print(GenerateParentheses().generateParenthesis(3))


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, pms):
            if i == len(nums):
                res.append(pms)
                return

            dfs(i+1, pms + [nums[i]])
        dfs(0, [])
        return res


# print(Permutations().permute([1, 2, 3]))
