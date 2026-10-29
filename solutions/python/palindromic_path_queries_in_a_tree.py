"""
Problem 3841. Palindromic Path Queries in a Tree

You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length
n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.
You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character
assigned to node i.
You are also given a string array queries, where each queries[i] is either:
- "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
- "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive)
can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi" can be rearranged into a
palindrome, and false otherwise.


Example 1:
Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
Output: [true,false]
Explanation:
- "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
- "update 1 b": Update node 1 to 'b', now s = "abc".
- "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:
Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
Output: [false,false,true]
Explanation:
- "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
- "update 0 b": Update node 0 to 'b', now s = "bbca".
- "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
- "update 3 a": Update node 3 to 'a', s = "bbca".
- "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].


Constraints:
- 1 <= n == s.length <= 5 * 104
- edges.length == n - 1
- edges[i] = [ui, vi]
- 0 <= ui, vi <= n - 1
- s consists of lowercase English letters.
- The input is generated such that edges represents a valid tree.
- 1 <= queries.length <= 5 * 10^4
    - queries[i] = "update ui c" or
    - queries[i] = "query ui vi"
    - 0 <= ui, vi <= n - 1
    - c is a lowercase English letter.
"""
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, idx, val):
        pos = idx + self.n
        self.tree[pos] = val
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[2 * pos] ^ self.tree[2 * pos + 1]
            pos //= 2

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res ^= self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res ^= self.tree[r]
            l //= 2
            r //= 2
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        sz = [1] * n
        heavy = [-1] * n

        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            max_sz = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sz:
                        max_sz = sz[v]
                        heavy[u] = v

        dfs1(0, -1, 0)

        head = [0] * n
        tin = [0] * n
        timer = 0

        def dfs2(u, h):
            nonlocal timer
            head[u] = h
            tin[u] = timer
            timer += 1
            if heavy[u] != -1:
                v = heavy[u]
                dfs2(v, h)
                for v in adj[u]:
                    if v != parent[u] and v != heavy[u]:
                        dfs2(v, v)

        dfs2(0, 0)

        seg = SegmentTree(n)
        for i in range(n):
            mask = 1 << (ord(s[i]) - ord('a'))
            seg.update(tin[i], mask)

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                seg.update(tin[u], mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                res = 0
                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]:
                        u, v = v, u
                    res ^= seg.query(tin[head[u]], tin[u])
                    u = parent[head[u]]
                if depth[u] > depth[v]:
                    u, v = v, u
                res ^= seg.query(tin[u], tin[v])

                if res == 0 or (res & (res - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans
