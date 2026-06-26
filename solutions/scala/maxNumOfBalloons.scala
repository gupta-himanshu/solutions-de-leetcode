"""
Problem: 1189. Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
"""
object Solution {
    def maxNumberOfBalloons(text: String): Int = {
      val textMap = text.toList.groupBy(identity).map((k, l) => k -> l.length)
      List(
        textMap.getOrElse('b', 0),
        textMap.getOrElse('a', 0),
        textMap.getOrElse('l', 0) / 2,
        textMap.getOrElse('o', 0) / 2,
        textMap.getOrElse('n', 0)
      ).min
    }
}