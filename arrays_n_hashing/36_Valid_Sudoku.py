def is_valid(l):
    from collections import Counter
    c = Counter(l)
    c.pop(".")
    s = set(c.values())
    if not s == {1} and not s == set():
        return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            if not is_valid(l):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if not is_valid(col):
                return False

        t = []
        for h in (1, 4, 7):
            for w in (1, 4, 7):
                t.append((h, w))

        for a, b in t:
            sec = []
            for h in (-1, 0, 1):
                for w in (-1, 0, 1):
                    sec.append(board[a + h][b + w])
            if not is_valid(sec):
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                if v in rows[r]:
                    return False

                if v in cols[c]:
                    return False

                if v in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                squares[(r // 3, c // 3)].add(v)
        return True
