import math
import time

from cube_render import render_cube


def clear_screen():
    # ANSI: move cursor home + clear screen
    print("\033[H\033[2J", end="")


def main():
    size = 10
    delay = 1.0
    step_deg = 15  # degrees the cube rotates between frames
    tilt_deg = 30  # constant X-axis tilt so the cube looks 3D

    angle_y = 0
    while True:
        angles = (math.radians(tilt_deg), math.radians(angle_y), 0)
        clear_screen()
        render_cube(size, angles)
        time.sleep(delay)
        angle_y = (angle_y + step_deg) % 360


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
