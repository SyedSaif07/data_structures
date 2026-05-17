from typing import List


class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10
        return rev == x


# x = 121
# print(PalindromeNumber().isPalindrome(x))


class ReverseInteger:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        rev = 0

        while temp > 0:
            rev = (rev * 10) + temp % 10
            temp //= 10
        if rev > (1 << 31) - 1:
            return 0
        return -rev if x < 0 else rev


# x = -123
# print(ReverseInteger().reverse(x))


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i == 0:
                return [1] + digits


# print(PlusOne().plusOne([4, 3, 2, 1]))


class RomantoInteger:
    def romanToInt(self, s: str) -> int:
        ref = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for i, j in zip(s, s[1:]):
            if ref[i] < ref[j]:
                result -= ref[i]
            else:
                result += ref[i]
        result += ref[s[-1]]
        return result

# print(RomantoInteger().romanToInt("MCMXCIV"))
