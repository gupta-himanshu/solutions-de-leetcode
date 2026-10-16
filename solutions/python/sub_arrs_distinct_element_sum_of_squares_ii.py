from typing import List

"""
Problem 2916. Subarrays Distinct Element Sum of Squares II

You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length.
Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
Since the answer may be very large, return it modulo 109 + 7.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

Example 2:
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.


Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.count = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (start + end) // 2

            left_node = 2 * node
            left_len = mid - start + 1
            self.tree[left_node] = (self.tree[left_node] + 2 * self.count[left_node] * val + val * val * left_len) % self.MOD
            self.count[left_node] = (self.count[left_node] + val * left_len) % self.MOD
            self.lazy[left_node] = (self.lazy[left_node] + val) % self.MOD

            right_node = 2 * node + 1
            right_len = end - mid
            self.tree[right_node] = (self.tree[right_node] + 2 * self.count[right_node] * val + val * val * right_len) % self.MOD
            self.count[right_node] = (self.count[right_node] + val * right_len) % self.MOD
            self.lazy[right_node] = (self.lazy[right_node] + val) % self.MOD

            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.tree[node] = (self.tree[node] + 2 * self.count[node] * val + val * val * length) % self.MOD
            self.count[node] = (self.count[node] + val * length) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)

        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD
        self.count[node] = (self.count[2 * node] + self.count[2 * node + 1]) % self.MOD

    def query(self):
        return self.tree[1]


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        total_sum = 0

        for r in range(n):
            l = last_seen.get(nums[r], -1) + 1
            last_seen[nums[r]] = r

            tree.update(1, 0, n - 1, l, r, 1)

            total_sum = (total_sum + tree.query()) % MOD

        return total_sum
