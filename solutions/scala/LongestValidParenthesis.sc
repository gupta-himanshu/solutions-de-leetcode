/**
 * Problem 32. Longest Valid Parentheses
 *
 * Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
 * parentheses substring.
 *
 *
 * Example 1:
 * Input: s = "(()"
 * Output: 2
 * Explanation: The longest valid parentheses substring is "()".
 *
 * Example 2:
 * Input: s = ")()())"
 * Output: 4
 * Explanation: The longest valid parentheses substring is "()()".
 *
 * Example 3:
 * Input: s = ""
 * Output: 0
 *
 *
 * Constraints:
 * - 0 <= s.length <= 3 * 104
 * - s[i] is '(', or ')'.
 */
object Solution {
  def longestValidParentheses(s: String): Int = {
    // FP Version
//    s.zipWithIndex.foldLeft((0, List(-1))){case((best, stack), (ch, i)) =>
//      if (ch == '(') {
//        (best, stack :+ i)
//      } else {
//        val midStack = stack.dropRight(1)
//        if (midStack.isEmpty) {
//          (best, midStack :+ i)
//        } else {
//          (best.max(i - midStack.lastOption.getOrElse(0)), midStack)
//        }
//      }
//    }._1
    // Non-FP Version
val stack = scala.collection.mutable.ListBuffer[Int](-1)
    s.zipWithIndex.foldLeft(0){case(best, (ch, i)) =>
      if (ch == '(') {
        stack += i
        best
      } else {
        stack.dropRightInPlace(1)
        if (stack.isEmpty) {
          stack += i
          best
        } else {
          best.max(i - stack.lastOption.getOrElse(0))
        }
      }
    }
  }
}
