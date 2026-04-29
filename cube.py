import math


def get_vertices(size, angles):
    """Return 8 cube vertices in 3D space.

    size:   edge length of the cube.
    angles: rotation angles in radians around the X, Y, Z axes
            as a tuple (ax, ay, az).

    The cube is centered at the origin, then rotated around X, Y, Z in order.
    """
    s = size / 2
    base = [
        (-s, -s, -s),
        ( s, -s, -s),
        ( s,  s, -s),
        (-s,  s, -s),
        (-s, -s,  s),
        ( s, -s,  s),
        ( s,  s,  s),
        (-s,  s,  s),
    ]

    ax, ay, az = angles
    cos_x, sin_x = math.cos(ax), math.sin(ax)
    cos_y, sin_y = math.cos(ay), math.sin(ay)
    cos_z, sin_z = math.cos(az), math.sin(az)

    rotated = []
    for x, y, z in base:
        # rotation around X
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
        # rotation around Y
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y
        # rotation around Z
        x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z
        rotated.append((x, y, z))
    return rotated


def project_2d(vertices_3d):
    """Orthographic projection: drop the Z axis (no perspective)."""
    return [(x, y) for x, y, _ in vertices_3d]


if __name__ == "__main__":
    size = 4
    angles = (math.radians(30), math.radians(45), 0)

    verts3d = get_vertices(size, angles)
    verts2d = project_2d(verts3d)

    print("3D vertices:")
    for v in verts3d:
        print(f"  ({v[0]:6.2f}, {v[1]:6.2f}, {v[2]:6.2f})")

    print("\n2D projection:")
    for v in verts2d:
        print(f"  ({v[0]:6.2f}, {v[1]:6.2f})")
