import scala.annotation.tailrec

/**
 * Problem 22. Generate Parentheses
 *
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 *
 *
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 *
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 *
 *
 * Constraints:
 * - 1 <= n <= 8
 */
object Solution {

  case class State(current: String, open: Int, close: Int)

  def generateParenthesis(n: Int): List[String] = {

    @tailrec
    def loop(
              stack: List[State],
              result: List[String]
            ): List[String] = stack match {

      case Nil =>
        result.reverse

      case State(curr, open, close) :: rest => {
        println(s"stack: $stack")
        if (curr.length == 2 * n)
          loop(rest, curr :: result)
        else {
          val nextStates =
            (if (open < n)
              List(State(curr + "(", open + 1, close))
            else Nil) :::
              (if (close < open)
                List(State(curr + ")", open, close + 1))
              else Nil)

          loop(nextStates ::: rest, result)
        }
      }
    }

    loop(List(State("", 0, 0)), Nil)
  }
}
