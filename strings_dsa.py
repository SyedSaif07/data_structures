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