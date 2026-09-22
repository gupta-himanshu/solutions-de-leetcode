from typing import List

"""
Problem 3525. Find X Value of Array II

You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where
queries[i] = [indexi, valuei, starti, xi].
You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains
non-empty.
The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the
remaining elements leaves a remainder of x modulo k.
For each query in queries you need to determine the x-value of nums for xi after performing the following actions:
- Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
- Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.
Note that x-value has a different definition in this version.
 

Example 1:
Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
Output: [2,2,2]
Explanation:
- For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
    - Remove the suffix [2, 4, 5]. nums becomes [1, 2].
    - Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
- For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
    - Remove the empty suffix. nums becomes [3, 5].
    - Remove the suffix [5]. nums becomes [3].
- For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
    - Remove the suffix [2, 2, 3, 5]. nums becomes [1].
    - Remove the suffix [3, 5]. nums becomes [1, 2, 2].

Example 2:
Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]
Output: [1,0]
Explanation:
- For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
    - Remove the suffix [2, 4, 8, 16, 32].
- For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.

Example 3:
Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]
Output: [5]

 
Constraints:

- 1 <= nums[i] <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= k <= 5
- 1 <= queries.length <= 2 * 10^4
- queries[i] == [indexi, valuei, starti, xi]
- 0 <= indexi <= nums.length - 1
- 1 <= valuei <= 10^9
- 0 <= starti <= nums.length - 1
- 0 <= xi <= k - 1
"""
class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [None] * (4 * self.n)
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left_prod: int, left_cnt: List[int], right_prod: int, right_cnt: List[int]):
        prod = (left_prod * right_prod) % self.k
        cnt = list(left_cnt)
        for r in range(self.k):
            if right_cnt[r] > 0:
                new_r = (left_prod * r) % self.k
                cnt[new_r] += right_cnt[r]
        return prod, cnt

    def _build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[node] = val
            cnt = [0] * self.k
            cnt[val] = 1
            self.tree_cnt[node] = cnt
            return

        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        self._build(nums, left_node, l, mid)
        self._build(nums, right_node, mid + 1, r)

        self.tree_prod[node], self.tree_cnt[node] = self._merge(
            self.tree_prod[left_node],
            self.tree_cnt[left_node],
            self.tree_prod[right_node],
            self.tree_cnt[right_node]
        )

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val_mod = val % self.k
            self.tree_prod[node] = val_mod
            cnt = [0] * self.k
            cnt[val_mod] = 1
            self.tree_cnt[node] = cnt
            return

        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if idx <= mid:
            self.update(left_node, l, mid, idx, val)
        else:
            self.update(right_node, mid + 1, r, idx, val)

        self.tree_prod[node], self.tree_cnt[node] = self._merge(
            self.tree_prod[left_node],
            self.tree_cnt[left_node],
            self.tree_prod[right_node],
            self.tree_cnt[right_node]
        )

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_cnt[node]

        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if qr <= mid:
            return self.query(left_node, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_node, mid + 1, r, ql, qr)

        left_prod, left_cnt = self.query(left_node, l, mid, ql, qr)
        right_prod, right_cnt = self.query(right_node, mid + 1, r, ql, qr)

        return self._merge(left_prod, left_cnt, right_prod, right_cnt)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = SegmentTree(nums, k)
        result = []

        for idx, val, start, x in queries:
            seg_tree.update(0, 0, n - 1, idx, val)

            if start >= n:
                result.append(0)
            else:
                _, cnt = seg_tree.query(0, 0, n - 1, start, n - 1)
                result.append(cnt[x])

        return result
