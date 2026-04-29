import math

SIZE = 20

pos1, pos2 = (0, 0), (3, 8)

field = [["-"] * SIZE for _ in range(SIZE)]

dx = pos2[0] - pos1[0]
dy = pos2[1] - pos1[1]

if abs(dx) == 0 and abs(dy) == 0:
    if 0 <= pos1[0] < SIZE and 0 <= pos1[1] < SIZE:
        field[pos1[1]][pos1[0]] = "*"
elif abs(dy) >= abs(dx):
    step = dx / dy
    sign = 1 if dy > 0 else -1
    for i in range(abs(dy) + 1):
        y = pos1[1] + i * sign
        normal = pos1[0] + i * sign * step
        f_cand = math.floor(normal)
        if (normal - f_cand) <= 0.5:
            x = f_cand
        else:
            x = f_cand + 1
        if 0 <= x < SIZE and 0 <= y < SIZE:
            field[y][x] = "*"
else:
    step = dy / dx
    sign = 1 if dx > 0 else -1
    for i in range(abs(dx) + 1):
        x = pos1[0] + i * sign
        normal = pos1[1] + i * sign * step
        f_cand = math.floor(normal)
        if (normal - f_cand) <= 0.5:
            y = f_cand
        else:
            y = f_cand + 1
        if 0 <= x < SIZE and 0 <= y < SIZE:
            field[y][x] = "*"

for row in field:
    print(*row, sep=' ')
