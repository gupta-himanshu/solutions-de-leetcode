"""
Problem 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

You are given two strings s and target, each of length n, consisting of lowercase English letters.
Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than
target. If no such permutation exists, return an empty string.


Example 1:
Input: s = "baba", target = "abba"
Output: "baab"
Explanation:
* The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
* The lexicographically smallest permutation that is strictly greater than target is "baab".

Example 2:
Input: s = "baba", target = "bbaa"
Output: ""
Explanation:
* The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
* None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Example 3:
Input: s = "abc", target = "abb"
Output: ""
Explanation:
* s has no palindromic permutations. Therefore, the answer is "".

Example 4:
Input: s = "aac", target = "abb"
Output: "aca"
Explanation:
* The only palindromic permutation of s is "aca".
* "aca" is strictly greater than target. Therefore, the answer is "aca".


Constraints:
* 1 <= n == s.length == target.length <= 300
* s and target consist of only lowercase English letters.
"""
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        counts = Counter(s)
        odd_chars = [ch for ch, freq in counts.items() if freq % 2 == 1]

        if len(odd_chars) > 1:
            return ""

        mid = odd_chars[0] if len(odd_chars) == 1 else ""

        half_counts = Counter()
        for ch, freq in counts.items():
            if freq // 2 > 0:
                half_counts[ch] = freq // 2

        half_len = n // 2
        target_half = target[:half_len]

        def make_palindrome(H: str) -> str:
            return H + mid + H[::-1]

        if half_len == 0:
            return mid if mid > target else ""

        if Counter(target_half) == half_counts:
            p_same = make_palindrome(target_half)
            if p_same > target:
                return p_same

        def get_next_permutation(half_counts: Counter, target_half: str, M: int) -> str:
            counts = half_counts.copy()

            matched = 0
            for ch in target_half:
                if counts[ch] > 0:
                    counts[ch] -= 1
                    matched += 1
                else:
                    break

            if matched == M:
                matched = M - 1
                counts[target_half[M - 1]] += 1

            for i in range(matched, -1, -1):
                target_char = target_half[i]

                best_ch = None
                for code in range(ord(target_char) + 1, ord("z") + 1):
                    ch = chr(code)
                    if counts[ch] > 0:
                        best_ch = ch
                        break

                if best_ch is not None:
                    counts[best_ch] -= 1

                    remaining = []
                    for code in range(ord("a"), ord("z") + 1):
                        ch = chr(code)
                        if counts[ch] > 0:
                            remaining.append(ch * counts[ch])

                    return target_half[:i] + best_ch + "".join(remaining)

                if i > 0:
                    counts[target_half[i - 1]] += 1

            return ""

        H_next = get_next_permutation(half_counts, target_half, half_len)
        if H_next:
            return make_palindrome(H_next)

        return ""
