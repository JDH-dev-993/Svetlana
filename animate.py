import math
import time

from cube_render import render_cube


def clear_screen():
    # ANSI: move cursor home + clear screen
    print("\033[H\033[2J", end="")


def ask_float(prompt, default):
    raw = input(f"{prompt} [{default}]: ").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        print(f"Не число, использую {default}")
        return default


def main():
    print("Настройка анимации (Enter — оставить значение по умолчанию)")
    size = ask_float("Размер куба", 10)
    speed_x = ask_float("Скорость по X (град/кадр)", 5)
    speed_y = ask_float("Скорость по Y (град/кадр)", 15)
    speed_z = ask_float("Скорость по Z (град/кадр)", 0)
    delay = ask_float("Задержка между кадрами (сек)", 1.0)

    angle_x = angle_y = angle_z = 0.0
    while True:
        angles = (
            math.radians(angle_x),
            math.radians(angle_y),
            math.radians(angle_z),
        )
        clear_screen()
        render_cube(size, angles)
        time.sleep(delay)
        angle_x = (angle_x + speed_x) % 360
        angle_y = (angle_y + speed_y) % 360
        angle_z = (angle_z + speed_z) % 360


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
