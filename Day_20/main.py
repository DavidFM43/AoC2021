from pathlib import Path
import part_1, part_2
from time import time


def get_input():

    input_file = Path(__file__).parent.resolve() / "input.txt"

    with open(input_file) as f:
        input = f.read()
        return input


def main():

    input = get_input()
    start = time()
    print(part_1.solve(input))
    print("Part 1 took", time() - start, "seconds")
    start = time()
    print(part_2.solve(input))
    print("Part 2 took", time() - start, "seconds")


if __name__ == "__main__":
    main()
