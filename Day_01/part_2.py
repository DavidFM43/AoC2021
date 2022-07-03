def solve(input):

    answer = 0
    nums = [int(x) for x in input]

    for idx in range(1, len(nums)):

        prev_win = nums[idx - 1 : idx + 2]
        win = nums[idx : idx + 3]

        if sum(win) > sum(prev_win):
            answer += 1

    return answer
