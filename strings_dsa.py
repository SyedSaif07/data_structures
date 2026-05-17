from collections import Counter
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


class ZigZagConversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        arr = [""] * numRows
        idx, d = 0, 1

        for i in s:
            arr[idx] += i
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        return "".join(arr)


# print(ZigZagConversion().convert(s="PAYPALISHIRING", numRows=3))


class StringToIntegerAtoi:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # Constants for 32-bit signed integer range
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check if we've reached the end
        if i == n:
            return 0

        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit

            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX

            i += 1

        # Step 4: Apply sign and return
        return res * sign


# print(StringToIntegerAtoi().myAtoi("1337c0d3"))


class ValidParenthesisString:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


# s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
# print(ValidParenthesisString().checkValidString(s))


class IndexOfFirstOccurrence:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


# haystack = "sadbutsad"
# needle = "sad"
#
# print(IndexOfFirstOccurrence().strStr(haystack, needle))


class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        start = end

        while start >= 0 and s[start] != " ":
            start -= 1

        return end - start


# print(LengthOfLastWord().lengthOfLastWord("luffy is still joyboy"))


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> int:
        c_dict = Counter(s)
        length = 0
        if_odd = False

        for count in c_dict.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                if_odd = True

        if if_odd: length += 1
        return length


# s = "abccccdd"
# print(LongestPalindrome().longestPalindrome(s))


class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        res = []

        while m >= 0 or n >= 0 or carry:
            if m >= 0:
                carry += int(a[m])
                m -= 1
            if n >= 0:
                carry += int(b[n])
                n -= 1
            res = [str(carry % 2)] + res
            carry = carry // 2
        return "".join(res)


# print(AddBinary().addBinary(a="1010", b="1011"))


class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def backtrack(comb, idx):
            if idx == len(digits):
                res.append(comb)
                return

            for letter in mapping[digits[idx]]:
                backtrack(comb + letter, idx + 1)

        backtrack("", 0)
        return res


# print(LetterCombinationsOfPhoneNumber().letterCombinations(digits="23"))
