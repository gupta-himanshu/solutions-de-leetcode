/**
 * Problem 3090. Maximum Length Substring With Two Occurrences
 *
 * Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 *
 *
 * Example 1:
 * Input: s = "bcbbbcba"
 * Output: 4
 * Explanation: The following substring has a length of 4 and contains at most two occurrences of each character:
 * "bcbbbcba".
 *
 * Example 2:
 * Input: s = "aaaa"
 * Output: 2
 * Explanation: The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 *
 *
 * Constraints:
 * * 2 <= s.length <= 100
 * * s consists only of lowercase English letters.
 */

import scala.annotation.tailrec

object Solution {
  def maximumLengthSubstring(s: String): Int = {
    @tailrec
    def shrink(left: Int, count: Map[Char, Int], current: Char, chars: List[Char]): (Int, Map[Char, Int]) = {
      if (count.getOrElse(current, 0) <= 2) {
        (left, count)
      } else {
        val leftNum = chars(left)
        val updatedCount = count ++ Map(leftNum -> (count(leftNum) - 1))
        shrink(left + 1, updatedCount, current, chars)
      }
    }

    val chars = s.toList
    chars.indices.foldLeft((0, Map.empty[Char, Int], 0)) {
      case ((left, count, ans), right) =>
        val current = chars(right)
        val (newLeft, newCount) =
          shrink(
            left,
            count ++ Map(current -> (count.getOrElse(current, 0) + 1)),
            current,
            chars
          )

        (newLeft, newCount, ans.max(right - newLeft + 1))
    }._3
  }
}
