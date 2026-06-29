"""
Problem: 1967. Number of Strings That Appear as Substrings in Word
Given an array of strings patterns and a string word, return the number of strings in patterns that appear as a substring in word.

Example 1:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation: The strings "a", "abc", and "bc" appear as substrings in word.
The string "d" does not appear as a substring in word.

Example 2:
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation: The strings "a" and "b" appear as substrings in word.

Constraints:
1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
"""
class Solution:
    def num_of_strings(self, patterns: list[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
