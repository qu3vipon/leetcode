pair = {
    "(": ")",
    "{": "}",
    "[": "]",
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if not stack:
                    return False
                op = stack.pop()
                if not c == pair[op]:
                    return False
        return not stack