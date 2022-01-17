from pathlib import Path
import part_1, part_2
import time

def get_input():
          
    input_file = Path(__file__).parent.resolve() / "input.txt"

    with open(input_file) as f:
        input = f.read()
        return input


def main():
    
    input = get_input()
    start = time.time()
    print(part_1.solve(input))
    print("Part1 solved in", time.time()- start, "seconds")
    start = time.time()
    print(part_2.solve(input))
    print("Part2 solved in", time.time()- start, "seconds")


if __name__ == "__main__":
    main()
