/*
Problem: 1358. Number of Substrings Containing All Three Characters
Given a string s consisting only of characters a, b and c. Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are
"abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (10 in total).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Constraints:
1 <= s.length <= 5 x 10^4
*/
object Solution extends App {
  def numberOfSubstrings(s: String): Int = {
    s.toList.zipWithIndex.foldLeft((Map('a' -> -1, 'b' -> -1, 'c' -> -1), 0)) {
      case ((lastSeen, resultSum), (ch, idx)) => {
        val newLastSeen = lastSeen + (ch -> idx)
        val newResultSum = (resultSum + newLastSeen.values.min) + 1
        (newLastSeen, newResultSum)
      }
    }._2
  }
}
