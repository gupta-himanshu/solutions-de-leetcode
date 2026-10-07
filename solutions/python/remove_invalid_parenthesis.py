"""
Problem 301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the
input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any
order.


Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]


Constraints:
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.
"""
from functools import cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        @cache
        def invalid_parenthesis_count(st: str) -> int:
            stack = []
            unpaired_closing_parenthesis_count = 0
            for c in st:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        unpaired_closing_parenthesis_count += 1
                else:
                    continue
            return len(stack) + unpaired_closing_parenthesis_count

        num_invalid_brackets = invalid_parenthesis_count(s)

        ans = set()
        @cache
        def generate_valid_parenthesis(s: str, i: int, count: int, valid_s: str):
            if count == 0 and len(valid_s) == len(s) - num_invalid_brackets:
                ans.add(valid_s)
                return
            else:
                if i < len(s):
                    if s[i] == '(':
                        # use character
                        generate_valid_parenthesis(s, i + 1, count + 1, valid_s + s[i])
                        # not use character
                        generate_valid_parenthesis(s, i + 1, count, valid_s)
                    elif s[i] == ')':
                        # use character
                        generate_valid_parenthesis(s, i + 1, count - 1, valid_s + s[i])
                        # not use character
                        generate_valid_parenthesis(s, i + 1, count, valid_s)
                    else:
                        # use character
                        generate_valid_parenthesis(s, i + 1, count, valid_s + s[i])
                else:
                    return

        generate_valid_parenthesis(s, 0, 0, "")
        ans = list(filter(lambda parenthesis_s: invalid_parenthesis_count(parenthesis_s) == 0, ans))
        return ans
