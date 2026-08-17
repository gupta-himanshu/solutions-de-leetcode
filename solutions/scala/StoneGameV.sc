/**
 * Problem 1563. Stone Game V
 *
 * There are several stones arranged in a row, and each stone has an associated value which is an integer given in the
 * array stoneValue.
 *
 * In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob
 * calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the
 * row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the
 * two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining
 * row.
 *
 * The game ends when there is only one stone remaining. Alice's score is initially zero.
 *
 * Return the maximum score that Alice can obtain.
 *
 *
 * Example 1:
 * Input: stoneValue = [6,2,3,4,5,5]
 * Output: 18
 * Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the
 * right row has value 14. Bob throws away the right row and Alice's score is now 11.
 * In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score
 * becomes 16 (11 + 5).
 * The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and
 * Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
 *
 * Example 2:
 * Input: stoneValue = [7,7,7,7,7,7,7]
 * Output: 28
 *
 * Example 3:
 * Input: stoneValue = [4]
 * Output: 0
 *
 *
 * Constraints:
 * * 1 <= stoneValue.length <= 500
 * * 1 <= stoneValue[i] <= 106
 */
object Solution {
  def stoneGameV(stoneValue: Array[Int]) = {
    val n = stoneValue.length

    // Immutable prefix sums
    val prefixSum =
      stoneValue.foldLeft(Vector(0)) { (acc, value) =>
        acc :+ (acc.last + value)
      }

    def rangeSum(l: Int, r: Int) =
      prefixSum(r + 1) - prefixSum(l)

    def dfs(
             l: Int,
             r: Int,
             memo: Map[(Int, Int), Int]
           ) = if (l == r) (0, memo) else memo.get((l, r)) match {
               case Some(value) =>
                 (value, memo)

               case None =>
                 val (best, updatedMemo) =
                   (l until r).foldLeft((0, memo)) {
                     case ((currentBest, currentMemo), i) =>

                       val leftSum = rangeSum(l, i)
                       val rightSum = rangeSum(i + 1, r)

                       if (leftSum < rightSum) {
                         val (leftScore, memo1) =
                           dfs(l, i, currentMemo)

                         (
                           currentBest.max(leftSum + leftScore),
                           memo1
                         )
                       } else if (leftSum > rightSum) {
                         val (rightScore, memo1) =
                           dfs(i + 1, r, currentMemo)

                         (
                           currentBest.max(rightSum + rightScore),
                           memo1
                         )
                       } else {
                         val (leftScore, memo1) =
                           dfs(l, i, currentMemo)

                         val (rightScore, memo2) =
                           dfs(i + 1, r, memo1)

                         (
                           currentBest.max(
                             leftSum + leftScore.max(rightScore)
                           ),
                           memo2
                         )
                       }
                   }

                 val finalMemo = updatedMemo.updated((l, r), best)

                 (best, finalMemo)
             }

    dfs(0, n - 1, Map.empty)._1
  }
}
