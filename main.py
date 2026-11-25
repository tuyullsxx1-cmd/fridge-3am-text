"""One line from a smart fridge, sent at 3am."""

import os

LINE = "It's 3am. The light is on, the milk expired yesterday, and the leftovers have formed a union."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
