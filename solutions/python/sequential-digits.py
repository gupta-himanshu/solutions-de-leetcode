"""
Problem: 1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9
"""
import math
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        l = int(math.log10(low)) + 1
        h = int(math.log10(high)) + 1
        num_digits = [i for i in range(l, (h + 1)) if i < 10]

        base = "123456789"
        for n in num_digits:
            i = 0
            j = n
            num = int(base[i:j])

            while num <= high:
                if low <= num:
                    result.append(num)
                i += 1
                j += 1
                if j <= 9:
                    num = int(base[i:j])
                else:
                    break

        return result