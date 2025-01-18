from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)  # Track each column
        rows = defaultdict(set)  # Track each row
        squares = defaultdict(set)  # Track each 3x3 square

        # Iterate over each cell in the board in one pass
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # Skip empty cells
                    continue

                # Check if the number is already in the current row, column, or square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # Invalid if duplicate is found
                
                # Add the number to the current row, column, and square
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True  # Board is valid if no duplicates are found
