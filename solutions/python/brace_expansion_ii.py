"""
Problem 1096. Brace Expansion II

Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the
expression represents.
The grammar can best be understood through simple examples:
- Single letters represent a singleton set containing that word.
    - R("a") = {"a"}
    - R("w") = {"w"}
- When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
    - R("{a,b,c}") = {"a","b","c"}
    - R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
- When we concatenate two expressions, we take the set of possible concatenations between two words where the first word
  comes from the first expression and the second word comes from the second expression.
    - R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
    - R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the three rules for our grammar:
- For every lowercase letter x, we have R(x) = {x}.
- For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
- For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation,
and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the
expression represents.


Example 1:
Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

Example 2:
Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.


Constraints:
- 1 <= expression.length <= 60
- expression[i] consists of '{', '}', ','or lowercase English letters.
- The given expression represents a set of words based on the grammar given in the description.
"""
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        buf = []
        expr_len = len(expression)

        for i in range(expr_len):
            buf.append(expression[i])
            if i + 1 < expr_len:
                c1, c2 = expression[i], expression[i + 1]
                if (c1.isalpha() or c1 == '}') and (c2.isalpha() or c2 == '{'):
                    buf.append('.')

        expr = "".join(buf)

        ops = []
        operands = []
        precedence = {',': 1, '.': 2}

        def apply_op():
            op = ops.pop()
            right = operands.pop()
            left = operands.pop()
            if op == ".":
                res = {x + y for x in left for y in right}
            elif op == ',':
                res = left | right
            operands.append(res)

        for c in expr:
            if c.isalpha():
                operands.append({c})
            elif c == '{':
                ops.append('{')
            elif c == '}':
                while ops and ops[-1] != '{':
                    apply_op()
                ops.pop()
            elif c in precedence:
                while ops and ops[-1] != '{' and precedence[ops[-1]] >= precedence[c]:
                    apply_op()
                ops.append(c)

        while ops:
            apply_op()

        return sorted(list(operands[0]))
