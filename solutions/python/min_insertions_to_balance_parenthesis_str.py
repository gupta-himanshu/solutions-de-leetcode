"""
Problem 1541. Minimum Insertions to Balance a Parentheses String

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.


Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')'
at the end of the string to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.


Constraints:
- 1 <= s.length <= 10^5
- s consists of '(' and ')' only.
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                if (i + 1) < n:
                    if s[i + 1] == ')':
                        if (i + 2) < n:
                            if s[i + 2] == ')':
                                i += 3
                            else:
                                ans += 1
                                i += 2
                        else:
                            ans += 1
                            i += 2
                    else:
                        stack.append(s[i])
                        i += 1
                else:
                    ans += 2
                    i += 1
            else:
                if (i + 1) < n:
                    if s[i + 1] == ')':
                        if len(stack) != 0:
                            stack.pop()
                            i += 2
                        else:
                            ans += 1
                            i += 2
                    else:
                        if len(stack) != 0:
                            stack.pop()
                            ans += 1
                            i += 1
                        else:
                            ans += 2
                            i += 1
                else:
                    if len(stack) != 0:
                        stack.pop()
                        ans += 1
                    else:
                        ans += 2
                    i += 1

        return ans + (len(stack) * 2)
