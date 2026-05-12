class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if (cell in cols[c] or cell in rows[r] or cell in squares[(r//3),(c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3),(c//3)].add(board[r][c])
        return True