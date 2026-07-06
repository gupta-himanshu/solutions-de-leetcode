/*
Problem: 1288. Remove Covered Intervals
Given an array of intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list. An interval [a, b) is covered by an interval [c, d) if and only if c <= a and b <= d. Return the number of remaining intervals.

Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1
Explanation: Interval [2,3] is covered by [1,4], therefore it is removed.

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 10^5
 */
object Solution {
  def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
    intervals.indices.count { i =>
      !intervals.indices.exists { j =>
        i != j &&
          intervals(j)(0) <= intervals(i)(0) &&
          intervals(i)(1) <= intervals(j)(1)
      }
    }
  }
}
