class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(o, c):
            if o == c == n:
                res.append("".join(stack))
                return

            if o < n:
                stack.append("(")
                backtrack(o + 1, c)
                stack.pop()

            if c < o:
                stack.append(")")
                backtrack(o, c + 1)
                stack.pop()

        backtrack(0, 0)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def f(p, left, right):
            if left:
                f(p + "(", left - 1, right)
            if right > left:
                f(p + ")", left, right - 1)
            if not right:
                res.append(p)
            return res

        return f("", n, n)
