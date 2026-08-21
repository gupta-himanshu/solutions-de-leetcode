"""
Problem 3116. Kth Smallest Amount With Single Denomination Combination

You are given an integer array coins representing coins of different denominations and an integer k.
You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different
denominations.
Return the kth smallest amount that can be made using these coins.


Example 1:
Input: coins = [3,6,9], k = 3
Output: 9
Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:
Input: coins = [5,2], k = 7
Output: 12
Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.


Constraints:
* 1 <= coins.length <= 15
* 1 <= coins[i] <= 25
* 1 <= k <= 2 * 109
* coins contains pairwise distinct integers.


Note: The approach works for small value of k only. Hence, do not follow this approach for large value of k.
For large value of k, binary search along with inclusion-exclusion can be used, to find the kth smallest amount.
"""
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        multiples = [1] * n
        smallest_denomination = 0

        for i in range(k):
            mn_denomination = float('inf')
            mn_idxs = []
            for j in range(n):
                coin = coins[j]
                multiple = multiples[j]
                # print(f"coin x multiple: {(coin * multiple)}")
                if (coin * multiple) < mn_denomination:
                    mn_denomination = (coin * multiple)
                    if len(mn_idxs) > 0:
                        mn_idxs.pop()
                    mn_idxs.append(j)
                elif (coin * multiple) == mn_denomination:
                    mn_idxs.append(j)
                else:
                    continue
            smallest_denomination = mn_denomination
            for mn_idx in mn_idxs:
                multiples[mn_idx] += 1

        return smallest_denomination