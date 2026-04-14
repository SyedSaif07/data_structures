"""
Using bitwise operators to perform operations.

& ^ | << >> These are some bitwise operators.

&& Logical AND needs to two operands and should be Boolean.

Bitwise operators operate at bit level.

Eg: 5 & 9 = 1
5 - 0 1 0 1
9 - 1 0 0 1
-----------
    0 0 0 1
-----------

Bitwise & (AND) operator will only give 1 if both the bits are 1.
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

Bitwise | (OR) operator
1 | 1  = 1
1 | 0  = 1
0 | 1  = 1
0 | 0  = 1

Eg: 5 | 9 = 13
5 - 0 1 0 1
9 - 1 0 0 1
-----------
    1 1 0 1
-----------

Bitwise ^ (XOR Exclusive OR) operator: It gives 1 if both the bits are different.
1 ^ 1  = 0
1 ^ 0  = 1
0 ^ 1  = 1
0 ^ 0  = 0

a ^ a = 0
a ^ 0 = a
a ^ b = b ^ a

<< Left shift operator: Shifts the bits left side.
8 << 3
8 -  1 0 0 0
Shifting 3 bits to the left side
1 0 0 0 0 0 0
8 << 3 = 64 = 8 * 2^3 = 8 * 8 = 64

5 << x = 5 * 2^x

>> Right shift operator. Shifts the bits to right side.
9 >> 2
9 - 1 0 0 1
9 >> 2 = 1 0 = 2 ( 0 1 will be gone because of right shifting)

9 >> 2 = 9/2^2 = 9 / 4 = 2

"""


class BitwiseXORSingleNumber:
    def singleNumber(self, nums) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans


# print(BitwiseXORSingleNumber().singleNumber([4,1,2,1,2]))

class BitWiseCountingBits:
    def countBits(self, n: int):
        result = []
        for i in range(n + 1):
            result.append(self.getNoOfSetBits(i))
        return result

    def getNoOfSetBits(self, num):
        count = 0
        for i in range(32):
            if (num & (1 << i)) > 0:
                count += 1
        return count

# print(BitWiseCountingBits().countBits(5))
