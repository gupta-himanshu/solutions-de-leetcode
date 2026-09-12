"""
Problem 3414. Maximum Score of Non-overlapping Intervals

You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li
and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen
intervals is defined as the total sum of their weights.
Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your
choice of non-overlapping intervals.
Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left
or right boundary are considered overlapping.


Example 1:
Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
Output: [2,3]
Explanation: You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:
Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
Output: [1,3,5,6]
Explanation: You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.


Constraints:
- 1 <= intevals.length <= 5 * 10^4
- intervals[i].length == 3
- intervals[i] = [li, ri, weighti]
- 1 <= li <= ri <= 10^9
- 1 <= weighti <= 10^9
"""
from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted(
            (l, r, w, i) for i, (l, r, w) in enumerate(intervals)
        )
        sorted_intervals.sort(key=lambda x: x[1])

        n = len(intervals)
        r_values = [interval[1] for interval in sorted_intervals]

        dp = [[(float('inf'), []) for _ in range(n + 1)] for _ in range(5)]

        for i in range(n + 1):
            dp[0][i] = (0, [])

        for i in range(1, n + 1):
            l, r, w, orig_idx = sorted_intervals[i - 1]

            p = bisect_right(r_values, l - 1)

            for c in range(1, 5):
                best = dp[c][i - 1]

                prev_w, prev_list = dp[c - 1][p]
                if prev_w != float('inf'):
                    cand_w = prev_w - w
                    cand_list = sorted(prev_list + [orig_idx])
                    cand = (cand_w, cand_list)

                    if cand < best:
                        best = cand

                dp[c][i] = best

        ans_tuple = (float('inf'), [])
        for c in range(1, 5):
            if dp[c][n] < ans_tuple:
                ans_tuple = dp[c][n]

        return ans_tuple[1]
