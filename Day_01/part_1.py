def solve(input):

    nums = [int(x) for x in input]
    answer = 0

    for idx in range(1, len( nums)):
        if nums[idx] > nums[idx - 1]:
            answer += 1

    return answer 