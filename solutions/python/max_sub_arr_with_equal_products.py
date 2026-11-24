from math import gcd, lcm
from typing import List


"""
Problem 3411. Maximum Subarray With Equal Products

You are given an array of positive integers nums.
An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.


Example 1:
Input: nums = [1,2,1,2,1,1,1]
Output: 5
Explanation: The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2,
gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:
Input: nums = [2,3,4,5,6]
Output: 3
Explanation: The longest product equivalent subarray is [3, 4, 5].

Example 3:
Input: nums = [1,2,3,1,4,5,1]
Output: 5


Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10
"""
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            prod, g, l = nums[i], nums[i], nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if prod == g * l:
                    best = max(best, j - i + 1)
                else:
                    continue

        return best
