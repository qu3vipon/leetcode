class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                n.append(int(t))
            else:
                a = n.pop()
                b = n.pop()

                if t == "+":
                    v = b + a
                elif t == "-":
                    v = b - a
                elif t == "*":
                    v = b * a
                elif t == "/":
                    v = int(b/a)
                n.append(v)
        return n.pop()