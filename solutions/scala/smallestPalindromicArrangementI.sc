/**
 * Problem 3517: Smallest Palindromic Rearrangement I
 *
 * You are given a palindromic string s.
 * Return the lexicographically smallest palindromic permutation of s.
 *
 * Example 1:
 * Input: s = "z"
 * Output: "z"
 * Explanation:
 * A string of only one character is already the lexicographically smallest palindrome.
 *
 * Example 2:
 * Input: s = "babab"
 * Output: "abbba"
 * Explanation:
 * Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
 *
 * Example 3:
 * Input: s = "daccad"
 * Output: "acddca"
 * Explanation:
 * Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
 *
 * Constraints:
 * * 1 <= s.length <= 105
 * * s consists of lowercase English letters.
 * * s is guaranteed to be palindromic.
 */
object Solution {
  def smallestPalindrome(s: String): String = {
    val n = s.length

    if (n == 1) {
      s
    } else {
      val m = n / 2
      val firstHalfSubStr = s.substring(0, m).toList.sorted.mkString
      val secondHalfSubStr = firstHalfSubStr.reverse

      if ((n % 2) == 0) {
        firstHalfSubStr + secondHalfSubStr
      } else {
        firstHalfSubStr + s(m) + secondHalfSubStr
      }
    }
  }
}
