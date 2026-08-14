"""
Problem 3090. Maximum Length Substring With Two Occurrences

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.


Example 1:
Input: s = "bcbbbcba"
Output: 4
Explanation: The following substring has a length of 4 and contains at most two occurrences of each character:
"bcbbbcba".

Example 2:
Input: s = "aaaa"
Output: 2
Explanation: The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


Constraints:
* 2 <= s.length <= 100
* s consists only of lowercase English letters.
"""
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        chars = list(s)
        n = len(chars)
        count = Counter()
        left = 0
        ans = 0

        for right in range(n):
            count[chars[right]] += 1

            while count[chars[right]] > 2:
                count[chars[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
