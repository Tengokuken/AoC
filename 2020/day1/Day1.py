# Part a: TwoSum using dicts
def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        key = target - nums[i]
        if key in seen:
            return [seen[key], i]
        seen[nums[i]] = i
    return -1


# Part b: ThreeSum using TwoSum
def three_sum(nums, target):
    # Fix i, check if TwoSum of the difference exists
    for i in range(len(nums)):
        target2 = target - nums[i]
        result = two_sum(nums, target2)
        if result != -1:
            return result + [i]
    return -1


# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = [int(i) for i in lines]
    two_sum_indices = two_sum(lines, 2020)
    print(lines[two_sum_indices[0]] * lines[two_sum_indices[1]])
    three_sum_indices = three_sum(lines, 2020)
    print(lines[three_sum_indices[0]] * lines[three_sum_indices[1]] * lines[three_sum_indices[2]])
