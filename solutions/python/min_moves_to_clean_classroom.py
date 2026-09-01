"""
Problem 3568. Minimum Moves to Clean the Classroom
You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the
room. Each cell in the grid is one of the following:
* 'S': Starting position of the student
* 'L': Litter that must be collected (once collected, the cell becomes empty)
* 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be
used multiple times)
* 'X': Obstacle the student cannot pass through
* '.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this
energy from the starting position 'S'.
Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student
can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.
Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.


Example 1:
Input: classroom = ["S.", "XL"], energy = 2
Output: 2
Explanation:
* The student starts at cell (0, 0) with 2 units of energy.
* Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
* A valid sequence of moves to collect all litter is as follows:
  * Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
  * Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
* The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:
Input: classroom = ["LS", "RL"], energy = 4
Output: 3
Explanation:
* The student starts at cell (0, 1) with 4 units of energy.
* A valid sequence of moves to collect all litter is as follows:
  * Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
  * Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
  * Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
* The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:
Input: classroom = ["L.S", "RXL"], energy = 3
Output: -1
Explanation:
No valid path collects all 'L'.


Constraints:
* 1 <= m == classroom.length <= 20
* 1 <= n == classroom[i].length <= 20
* classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
* 1 <= energy <= 50
* There is exactly one 'S' in the grid.
* There are at most 10 'L' cells in the grid.
"""
from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litters = {}
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters[(r, c)] = len(litters)

        k = len(litters)
        if k == 0:
            return 0

        target_mask = (1 << k) - 1

        start_r, start_c = start
        start_mask = 0
        if (start_r, start_c) in litters:
            start_mask |= (1 << litters[(start_r, start_c)])
            if start_mask == target_mask:
                return 0

        total_states = m * n * (1 << k)
        use_array = total_states <= 2000000

        start_idx = ((start_r * n + start_c) << k) | start_mask
        if use_array:
            best_energy = [-1] * total_states
            best_energy[start_idx] = energy
        else:
            best_energy = {start_idx : energy}

        queue = deque([(start_r, start_c, start_mask, energy)])
        steps = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            steps += 1
            for _ in range(len(queue)):
                r, c, mask, curr_e = queue.popleft()

                if curr_e == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        cell = classroom[nr][nc]
                        next_e = energy if cell == 'R' else curr_e - 1

                        next_mask = mask
                        if cell == 'L' and (nr, nc) in litters:
                            next_mask |= (1 << litters[(nr, nc)])
                            if next_mask == target_mask:
                                return steps

                        idx = ((nr * n + nc) << k) | next_mask

                        if use_array:
                            if next_e > best_energy[idx]:
                                best_energy[idx] = next_e
                                queue.append((nr, nc, next_mask, next_e))
                        else:
                            if next_e > best_energy.get(idx, -1):
                                best_energy[idx] = next_e
                                queue.append((nr, nc, next_mask, next_e))

        return -1
