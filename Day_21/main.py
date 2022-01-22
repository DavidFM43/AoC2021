from pathlib import Path
import part_1, part_2

def get_input():
          
    input_file = Path(__file__).parent.resolve() / "input.txt"

    with open(input_file) as f:
        input = f.read().splitlines()
        return input


def main():

    input = get_input()

    print("Part 1: {}".format(part_1.solve(input)))

    print("Part 2: {}".format(part_2.solve(input)))


if __name__ == "__main__":
    main()
