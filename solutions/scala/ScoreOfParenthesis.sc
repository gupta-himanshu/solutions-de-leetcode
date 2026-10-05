/**
 * Problem 856. Score of Parenthesis
 *
 * Given a balanced parentheses string s, return the score of the string.
 *
 * The score of a balanced parentheses string is based on the following rule:
 *
 * - "()" has score 1.
 * - AB has score A + B, where A and B are balanced parentheses strings.
 * - (A) has score 2 * A, where A is a balanced parentheses string.
 *
 *
 * Example 1:
 * Input: s = "()"
 * Output: 1
 *
 * Example 2:
 * Input: s = "(())"
 * Output: 2
 *
 * Example 3:
 * Input: s = "()()"
 * Output: 2
 *
 *
 * Constraints:
 * - 2 <= s.length <= 50
 * - s consists of only '(' and ')'.
 * - s is a balanced parentheses string.
 */
object Solution {
  def scoreOfParentheses(s: String): Int = {
    s.foldLeft(List(0)){case(stack, ch) =>
      if (ch == '(') {
        stack :+ 0
      } else {
        val lastTwo = stack.takeRight(2)
        val last = lastTwo.last
        val secondLast = lastTwo.head
        stack.dropRight(2) :+ (secondLast + (2 * last).max(1))
      }
    }.last
  }
}
