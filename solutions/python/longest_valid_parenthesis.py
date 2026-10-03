"""
Problem 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
parentheses substring.


Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0


Constraints:
- 0 <= s.length <= 3 * 104
- s[i] is '(', or ')'.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base for length calculation
        best = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # reset base
                else:
                    best = max(best, i - stack[-1])
        return best
