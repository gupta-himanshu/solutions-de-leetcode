"""
Problem 3310: Remove Methods From Project

You are maintaining a project that has n methods numbered from 0 to n - 1.
You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that
method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are
considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the
answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.


Example 1:
Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
Output: [0,1,2,3]
Explanation: Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not
suspicious. We return all elements without removing anything.

Example 2:
Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]
Output: [3,4]
Explanation: Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove
them.

Example 3:
Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]
Output: []
Explanation: All methods are suspicious. We can remove them.


Constraints:
* 1 <= n <= 105
* 0 <= k <= n - 1
* 0 <= invocations.length <= 2 * 105
* invocations[i] == [ai, bi]
* 0 <= ai, bi <= n - 1
* ai != bi
* invocations[i] != invocations[j]
"""


from collections import deque
from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        relationships = [[] for _ in range(n)]
        reverse_relationships = [[] for _ in range(n)]

        for calling_method, called_method in invocations:
            relationships[calling_method].append(called_method)
            reverse_relationships[called_method].append(calling_method)

        # Find suspicious methods
        suspicious_methods = {k}
        queue = deque([k])

        while queue:
            suspicious_method = queue.popleft()
            nxt_suspicious_methods = relationships[suspicious_method]
            for nxt_suspicious_method in nxt_suspicious_methods:
                if nxt_suspicious_method > -1 and nxt_suspicious_method not in suspicious_methods:
                    suspicious_methods.add(nxt_suspicious_method)
                    queue.append(nxt_suspicious_method)

        # Check whether any outside method invokes a suspicious method
        all_methods = set(range(n))
        remaining_methods = all_methods - suspicious_methods
        non_suspicious_methods = remaining_methods
        queue = deque(list(non_suspicious_methods))

        while queue:
            non_suspicious_method = queue.popleft()
            called_methods = relationships[non_suspicious_method]
            for called_method in called_methods:
                if called_method in suspicious_methods and called_method not in non_suspicious_methods:
                    non_suspicious_methods.add(called_method)
                    queue.append(called_method)
            calling_methods = reverse_relationships[non_suspicious_method]
            for calling_method in calling_methods:
                if calling_method in suspicious_methods and calling_method not in non_suspicious_methods:
                    non_suspicious_methods.add(calling_method)
                    queue.append(calling_method)

        return list(non_suspicious_methods)