import math

from cube import get_vertices, project_2d

SIZE = 20

# 12 cube edges as pairs of vertex indices (matching get_vertices ordering).
EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # top face
    (0, 4), (1, 5), (2, 6), (3, 7),  # vertical edges
]


def draw_line(field, pos1, pos2):
    """Draw a line between pos1 and pos2 on `field`. Same algorithm as main.py."""
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


def render_cube(size, angles):
    """Render a wireframe cube on a SIZE x SIZE console field."""
    verts3d = get_vertices(size, angles)
    verts2d = project_2d(verts3d)

    cx, cy = SIZE // 2, SIZE // 2
    pixel_verts = [(round(x) + cx, round(y) + cy) for x, y in verts2d]

    field = [["-"] * SIZE for _ in range(SIZE)]
    for a, b in EDGES:
        draw_line(field, pixel_verts[a], pixel_verts[b])

    for row in field:
        print(*row, sep=' ')


if __name__ == "__main__":
    size = 10
    angles = (math.radians(30), math.radians(45), 0)
    render_cube(size, angles)
