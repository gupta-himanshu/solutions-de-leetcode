"""
Problem 628. Maximum Product of Three Numbers
You are given an integer array nums.
Find three numbers whose product is maximum and return the maximum product.


Example 1:
Input: nums = [1,2,3]
Output: 6
Explanation: The only three numbers are 1, 2, and 3, so the maximum product is 1 * 2 * 3 = 6.

Example 2:
Input: nums = [1,2,3,4]
Output: 24
Explanation: The largest product comes from the three greatest numbers: 2 * 3 * 4 = 24.

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
Explanation: The only three numbers are -1, -2, and -3, so the maximum product is (-1) * (-2) * (-3) = -6.


Constraints:
* 3 <= nums.length <= 104
* -1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        mx = sec_mx = third_mx = float("-inf")
        mn = sec_mn = float("inf")

        for num in nums:
            if num > mx:
                mx, sec_mx, third_mx = num, mx, sec_mx
            elif num > sec_mx:
                sec_mx, third_mx = num, sec_mx
            elif num > third_mx:
                third_mx = num

            if num < mn:
                mn, sec_mn = num, mn
            elif num < sec_mn:
                sec_mn = num

        prod1 = mx * sec_mx * third_mx
        prod2 = mx * mn * sec_mn

        return prod1 if prod1 > prod2 else prod2
