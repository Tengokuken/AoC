import itertools
digit_mapping = ['abcdeg', 'ab', 'acdfg', 'abcdf', 'abef', 'bcdef', 'bcdefg', 'abd', 'abcdefg', 'abcdef']
def digits(lines):
    # number of 1, 4, 7, 8
    counter = 0

    for line in lines:
        line = line.split(' ')
        for i in range(4):
            digit = line[i + len(line) - 4]
            if len(digit) in [2, 3, 4, 7]:
                counter += 1
    return counter

def decode_digits(lines):
    num_sum = 0
    for line in lines:
        dig, out = line.split(' | ')
        dig = dig.split(' ')
        out = out.split(' ')
        # Get all permutations of the strings
        for perm in itertools.permutations("abcdefg"):
            pmap = {dig: out for dig, out in zip(perm, "abcdefg")}
            aperms = ["".join(pmap[c] for c in x) for x in dig]
            bperms = ["".join(pmap[c] for c in x) for x in out]
            if all("".join(sorted(an)) in digit_mapping for an in aperms):
                bperms = ["".join(sorted(x)) for x in bperms]
                num_sum += int("".join([str(digit_mapping.index(x)) for x in bperms]))
                break
    return num_sum

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    numbers = digits(lines)
    print(numbers)
    numbers = decode_digits(lines)
    print(numbers)