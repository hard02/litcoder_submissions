from collections import Counter

def isValidSudoku(board):
    rows = [set() for _ in range(len(board))]
    cols = [set() for _ in range(len(board[0]))]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != ".":
                if val in rows[i] or val in cols[j] or val in squares[i//3][j//3]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[i//3][j//3].add(val)

    return True

# Example usage
board_size = int(input().strip())
board = [list(input().strip().split()) for _ in range(board_size)]

result = isValidSudoku(board)
print("YES" if result else "NO")
                                     
