import math

from sortedcontainers import SortedList
from typing import List

"""
Problem 3505. Minimum Operations to Make Elements Within K Subarrays Equal

You are given an integer array nums and two integers, x and k. You can perform the following operation any number of
times (including zero):
- Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums,
where all elements within each subarray are equal.


Example 1:
Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
Output: 8
Explanation:
- Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is
[5, 1, 1, 1, 7, 3, 6, 4, -1].
- Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is
[5, 1, 1, 1, 7, 4, 4, 4, -1].
- Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal.
Since 8 total operations were used, 8 is the output.

Example 2:
Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
Output: 3
Explanation:
- Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
- Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal.
Since 3 operations were used, 3 is the output.


Constraints:
- 2 <= nums.length <= 10^5
- -10^6 <= nums[i] <= 10^6
- 2 <= x <= nums.length
- 1 <= k <= 15
- 2 <= k * x <= nums.length
"""
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        lower = SortedList()
        upper = SortedList()
        lower_sum = 0
        upper_sum = 0
        min_ops = []

        for i, num in enumerate(nums):
            if not lower or num <= lower[-1]:
                lower.add(num)
                lower_sum += num
            else:
                upper.add(num)
                upper_sum += num

            if i >= x:
                out_num = nums[i - x]
                if out_num in lower:
                    lower.remove(out_num)
                    lower_sum -= out_num
                else:
                    upper.remove(out_num)
                    upper_sum -= out_num

            if len(lower) < len(upper):
                val = upper.pop(0)
                lower.add(val)
                upper_sum -= val
                lower_sum += val
            elif len(lower) - len(upper) > 1:
                val = lower.pop()
                upper.add(val)
                lower_sum -= val
                upper_sum += val

            if i >= x - 1:
                median = lower[-1]
                ops = (median * len(lower) - lower_sum) + (upper_sum - median * len(upper))
                min_ops.append(ops)

        m = len(min_ops)
        dp = [[math.inf] * (m + 2) for _ in range(k + 1)]

        for i in range(m + 2):
            dp[0][i] = 0

        for rem_k in range(1, k + 1):
            for i in range(m - 1, -1, -1):
                res = dp[rem_k][i + 1]

                next_idx = i + x
                if rem_k - 1 == 0:
                    future_cost = 0
                else:
                    future_cost = dp[rem_k - 1][next_idx] if next_idx <= m else math.inf

                res = min(res, min_ops[i] + future_cost)
                dp[rem_k][i] = res

        return dp[k][0]
