from typing import List


class MinimumAddToMakeParenthesisValid:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                ans += 1
                count += 1
        ans += count
        return ans


# print(MinimumAddToMakeParenthesisValid().minAddToMakeValid(")))"))


class LongestCommonPrefix:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


# print(LongestCommonPrefix().longestCommonPrefix(v=["flower", "flow", "flight"]))
