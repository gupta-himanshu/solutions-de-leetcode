/**
 * Problem: 1291. Sequential Digits
 * An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
 * Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
 *
 * Example 1:
 * Input: low = 100, high = 300
 * Output: [123,234]
 *
 * Example 2:
 * Input: low = 1000, high = 13000
 * Output: [1234,2345,3456,4567,5678,6789,12345]
 *
 * Constraints:
 * 10 <= low <= high <= pow(10, 9)
 */
object Solution {
  def sequentialDigits(low: Int, high: Int): List[Int] = {
    val l = math.log10(low.toDouble).toInt + 1
    val h = math.log10(high.toDouble).toInt + 1

    (l to h)
      .filter(_ < 10)
      .toList.flatMap(numDigit => {
        "123456789".toList.sliding(numDigit)
          .toList.map(_.mkString.toInt)
          .filter(num => low <= num && num <= high)
      })
  }
}
