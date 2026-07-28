"""
Problem 3517: Smallest Palindromic Rearrangement I

You are given a palindromic string s.
Return the lexicographically smallest palindromic permutation of s.

Example 1:
Input: s = "z"
Output: "z"
Explanation:
A string of only one character is already the lexicographically smallest palindrome.

Example 2:
Input: s = "babab"
Output: "abbba"
Explanation:
Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:
Input: s = "daccad"
Output: "acddca"
Explanation:
Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

Constraints:
* 1 <= s.length <= 105
* s consists of lowercase English letters.
* s is guaranteed to be palindromic.
"""
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s
        else:
            m = n // 2
            first_half_sub_str_list = list(s[:m])
            first_half_sub_str_list.sort()
            first_half_sub_str = ''.join(first_half_sub_str_list)

            first_half_sub_str_list.reverse()
            second_half_sub_str = ''.join(first_half_sub_str_list)

            if n % 2 == 0:
                return first_half_sub_str + second_half_sub_str
            else:
                return first_half_sub_str + s[n // 2] + second_half_sub_str
