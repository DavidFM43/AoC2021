from math import prod


def solve(packet):
    packet = packet.strip()
    packet = list(bin(int(packet, 16))[2:].zfill(len(packet) * 4))
    return process_packet(packet)[1]

def process_packet(packet):
    version = int("".join(packet[:3]), 2)
    id = int("".join(packet[3:6]), 2)
    info = packet[6:]
    # literal packet
    if id == 4:
        go = True
        bin = "0b"
        while go:
            prefix = info.pop(0)
            if prefix == '0':
                go = False
            bin += "".join(info[:4])
            info = info[4:]
        num = int(bin, 2)

        return info, num
    # operator packet
    else:
        nums = []
        operations = [lambda nums: sum(nums),
                      lambda nums: prod(nums),
                      lambda nums: min(nums),
                      lambda nums: max(nums),
                      False,
                      lambda nums: int(nums[0] > nums[1]),
                      lambda nums: int(nums[0] < nums[1]),
                      lambda nums: int(nums[0] == nums[1])]
        operation = operations[id]
        length_id = info.pop(0)
        if length_id == '0':
            total_length = int("0b"+"".join(info[:15]), 2)
            info = info[15:]
            to_process = info[:total_length]
            while to_process:
                to_process, num = process_packet(to_process)
                nums.append(num)
            to_process = info[total_length:]
        else:
            num_packets = int("0b"+"".join(info[:11]), 2)
            to_process = info[11:]
            for _ in range(num_packets):
                to_process, num = process_packet(to_process)
                nums.append(num)

        num = operation(nums)
        return to_process, num
