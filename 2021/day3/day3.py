def diagnostic(nums):
    # Get length of numbers in diagnostic report
    bit_len = len(nums[0])
    bits = [0] * bit_len
    for num in nums:
        for i in range(bit_len):
            # Get ith digit from each number
            digit = int(num[i])
            if digit == 1:
                bits[i] += 1
            else:
                bits[i] -= 1
    gamma = epsilon = ''
    for bit in bits:
        gamma += '1' if bit > 0 else '0'
        epsilon += '1' if bit < 0 else '0'
    return int(gamma, 2) * int(epsilon, 2)

def consume(nums):
    # Get length of numbers in diagnostic report
    bit_len = len(nums[0])
    o2_gen = nums
    co2_scrub = nums[:]
    for i in range(bit_len):
        # Find the most common bit
        most_common = 0
        least_common = 0
        for num in o2_gen:
            if int(num[i]) == 1:
                most_common += 1
            else:
                most_common -= 1
        # Find least common
        for num in co2_scrub:
            if int(num[i]) == 1:
                least_common += 1
            else:
                least_common -= 1
        most_common = 1 if most_common >= 0 else 0
        least_common = 1 if least_common < 0 else 0
        if len(o2_gen) == 1 and len(co2_scrub) == 1:
            break
        # Keep values with most common bit in o2_gen
        if len(o2_gen) != 1:
            o2_gen = [x for x in o2_gen if int(x[i]) == most_common]
        if len(co2_scrub) != 1:
            co2_scrub = [x for x in co2_scrub if int(x[i]) == least_common]

    return int(o2_gen[0], 2) * int(co2_scrub[0], 2)

# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    rating = diagnostic(lines)
    print(rating)
    rating = consume(lines)
    print(rating)
