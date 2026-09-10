/**
 * Problem 3501. Maximize Active Section with Trade II
 *
 * You are given a binary string s of length n, where:
 * - '1' represents an active section.
 * - '0' represents an inactive section.
 *
 * You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
 * - Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
 * - Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
 * Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].
 *
 * For each query, determine the maximum possible number of active sections in s after making the optimal trade on the
 * substring s[li...ri].
 *
 * Return an array answer, where answer[i] is the result for queries[i].
 *
 * Note
 * - For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'.
 * The augmented '1's do not contribute to the final count.
 * - The queries are independent of each other.
 *
 *
 * Example 1:
 * Input: s = "01", queries = [[0,1]]
 * Output: [1]
 * Explanation:
 * Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active
 * sections is 1.
 *
 * Example 2:
 * Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]
 * Output: [4,3,1,1]
 * Explanation:
 * - Query [0, 3] → Substring "0100" → Augmented to "101001"
 * Choose "0100", convert "0100" → "0000" → "1111".
 * The final string without augmentation is "1111". The maximum number of active sections is 4.
 *
 * - Query [0, 2] → Substring "010" → Augmented to "10101"
 * Choose "010", convert "010" → "000" → "111".
 * The final string without augmentation is "1110". The maximum number of active sections is 3.
 *
 * - Query [1, 3] → Substring "100" → Augmented to "11001"
 * Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
 *
 * - Query [2, 3] → Substring "00" → Augmented to "1001"
 * Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
 *
 * Example 3:
 * Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]
 * Output: [6,7,2]
 * Explanation:
 * - Query [1, 5] → Substring "00010" → Augmented to "1000101"
 * Choose "00010", convert "00010" → "00000" → "11111".
 * The final string without augmentation is "1111110". The maximum number of active sections is 6.
 *
 * - Query [0, 6] → Substring "1000100" → Augmented to "110001001"
 * Choose "000100", convert "000100" → "000000" → "111111".
 * The final string without augmentation is "1111111". The maximum number of active sections is 7.
 *
 * - Query [0, 4] → Substring "10001" → Augmented to "1100011"
 * Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.
 *
 * Example 4:
 * Input: s = "01010", queries = [[0,3],[1,4],[1,3]]
 * Output: [4,4,2]
 * Explanation:
 * - Query [0, 3] → Substring "0101" → Augmented to "101011"
 * Choose "010", convert "010" → "000" → "111".
 * The final string without augmentation is "11110". The maximum number of active sections is 4.
 *
 * - Query [1, 4] → Substring "1010" → Augmented to "110101"
 * Choose "010", convert "010" → "000" → "111".
 * The final string without augmentation is "01111". The maximum number of active sections is 4.
 *
 * - Query [1, 3] → Substring "101" → Augmented to "11011"
 * Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.
 *
 *
 * Constraints:
 * - 1 <= n == s.length <= 105
 * - 1 <= queries.length <= 105
 * - s[i] is either '0' or '1'.
 * - queries[i] = [li, ri]
 * - 0 <= li <= ri < n
 */

import java.util.*;

class Solution {
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        int n = s.length();
        int activeCount = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                activeCount++;
            }
        }

        List<int[]> zeroBlocks = new ArrayList<>();
        int i = 0;
        while (i < n) {
            if (s.charAt(i) == '0') {
                int start = i;
                while (i < n && s.charAt(i) == '0') {
                    i++;
                }
                zeroBlocks.add(new int[]{start, i - 1});
            } else {
                i++;
            }
        }

        int m = zeroBlocks.size();
        int numQueries = queries.length;
        int[] result = new int[numQueries];

        if (m < 2) {
            Arrays.fill(result, activeCount);
            return Arrays.stream(result).boxed().collect(Collectors.toList());
        }

        int[] blockStart = new int[m];
        int[] blockEnd = new int[m];
        int[] blockSize = new int[m];

        for (int k = 0; k < m; k++) {
            blockStart[k] = zeroBlocks.get(k)[0];
            blockEnd[k] = zeroBlocks.get(k)[1];
            blockSize[k] = blockEnd[k] - blockStart[k] + 1;
        }

        int N = m - 1;
        int[] pairSum = new int[N];
        for (int k = 0; k < N; k++) {
            pairSum[k] = blockSize[k] + blockSize[k + 1];
        }

        SparseTable st = new SparseTable(pairSum);

        for (int q = 0; q < numQueries; q++) {
            int l = queries[q][0];
            int r = queries[q][1];

            int low = lowerBound(blockEnd, m, l);
            int high = upperBound(blockStart, m, r) - 1;

            if (low >= high) {
                result[q] = activeCount;
            } else {
                int firstLen = blockEnd[low] - Math.max(blockStart[low], l) + 1;
                int lastLen = Math.min(blockEnd[high], r) - blockStart[high] + 1;

                int maxGain;
                if (high - low == 1) {
                    maxGain = firstLen + lastLen;
                } else {
                    int pair1 = firstLen + blockSize[low + 1];
                    int pair2 = blockSize[high - 1] + lastLen;
                    int internalMax = st.query(low + 1, high - 2);
                    maxGain = Math.max(pair1, Math.max(pair2, internalMax));
                }
                result[q] = activeCount + maxGain;
            }
        }

        return Arrays.stream(result).boxed().collect(Collectors.toList());
    }

    private int lowerBound(int[] arr, int len, int target) {
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private int upperBound(int[] arr, int len, int target) {
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] > target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private static class SparseTable {
        private final int[][] st;
        private final int[] log;

        public SparseTable(int[] arr) {
            int n = arr.length;
            log = new int[n + 1];
            for (int i = 2; i <= n; i++) {
                log[i] = log[i / 2] + 1;
            }
            int k = log[n] + 1;
            st = new int[n][k];
            for (int i = 0; i < n; i++) {
                st[i][0] = arr[i];
            }
            for (int j = 1; j < k; j++) {
                for (int i = 0; i + (1 << j) <= n; i++) {
                    st[i][j] = Math.max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
                }
            }
        }

        public int query(int L, int R) {
            if (L > R) return 0;
            int j = log[R - L + 1];
            return Math.max(st[L][j], st[R - (1 << j) + 1][j]);
        }
    }
}
