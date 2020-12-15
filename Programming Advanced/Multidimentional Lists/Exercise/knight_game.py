def get_killed_knights(row_d, col_d, size, board_d):
    pass


n = int(input())

board = []
for _ in range(n):
    line = [x for x in input().split()]
    matrix.append(line)

most_kills = 0
total_kills = 0
to_kill = []

for row in range(n):
    for col in range(n):
        if board[row][col] == 'K':
            killed_knights = get_killed_knights(row, col, n, board)
            if killed_knights > most_kills:
                most_kills = killed_knights
                to_kill = [row, col]

to_kill_row = to_kill[0]
to_kill_col = to_kill[1]
board[to_kill_row][to_kill_col] = '0'
total_kills += 1
