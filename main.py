import math

pos1, pos2 = (0, 0), (3, 8)
step = pos2[0] / pos2[1]
for y in range(pos2[1]):
    normal = y * step
    line = ["-"] * pos2[1]
    f_cand = math.floor(normal)
    if (normal - f_cand) <= 0.5:
        line[f_cand] = "*"
    else:
        line[f_cand + 1] = "*"
    print(*line, sep=' ')
