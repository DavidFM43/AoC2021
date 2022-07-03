def sort_str(string):
    """sorts a string in lexicographic order"""

    return "".join(sorted(list(string)))


def solve(input):
    """builds a dictionary with signal-number pairs"""

    counter = 0

    for line in input:

        instruction = line.split(" | ")
        signal = instruction[0].split(" ")
        output = instruction[1].split(" ")

        number_map = [0 for x in range(10)]
        signal_map = dict()

        sorted_signal = sorted(signal, key=lambda x: len(x))

        signal_map[sort_str(sorted_signal[0])] = 1
        number_map[1] = sorted_signal[0]

        signal_map[sort_str(sorted_signal[1])] = 7
        number_map[7] = sorted_signal[1]

        signal_map[sort_str(sorted_signal[2])] = 4
        number_map[4] = sorted_signal[2]

        signal_map[sort_str(sorted_signal[9])] = 8
        number_map[8] = sorted_signal[9]

        len5 = sorted_signal[3:6]
        len6 = sorted_signal[6:9]

        for num in len5:
            sorted_num = sort_str(num)

            if len(set(num) & set(number_map[1])) == 2:
                signal_map[sorted_num] = 3
                number_map[3] = num
            elif len(set(num) & set(number_map[4])) == 3:
                signal_map[sorted_num] = 5
                number_map[5] = num
            else:
                signal_map[sorted_num] = 2
                number_map[2] = num

        for num in len6:
            sorted_num = sort_str(num)
            if len(set(num) & set(number_map[4])) == 4:
                signal_map[sorted_num] = 9
                number_map[9] = num
            elif len(set(num) & set(number_map[5])) == 5:
                signal_map[sorted_num] = 6
                number_map[6] = num
            else:
                signal_map[sorted_num] = 0
                number_map[0] = num

        number = ""

        for digit in output:
            digit = sort_str(digit)
            number += str(signal_map[digit])
        counter += int(number)

    return counter
