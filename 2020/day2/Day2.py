# Part a: Check password using string processing
def check_valid_password(line):
    # Split input
    lst = line.split(' ')
    print(lst)
    (min_occ, max_occ) = [int(x) for x in lst[0].split('-')]
    char_policy = lst[1][:-1]
    password = lst[2][:-1]
    # Check occurrences in string
    return min_occ <= password.count(char_policy) <= max_occ

# Part b: Check password using string processing
def check_valid_password_new(line):
    # Split input
    lst = line.split(' ')
    print(lst)
    (first_pos, second_pos) = [int(x) for x in lst[0].split('-')]
    char_policy = lst[1][:-1]
    password = lst[2][:-1]
    # Check occurrences in string
    if password[first_pos-1] == char_policy and password[second_pos-1] != char_policy or password[first_pos-1] != char_policy and password[second_pos-1] == char_policy:
        return True
    return False


# Driver code
if __name__ == "__main__":
    valid_passes = 0
    valid_passes_new = 0
    with open("input.txt") as f:
        for line in f:
            # Check if password is valid
            if check_valid_password(line):
                valid_passes += 1
            if check_valid_password_new(line):
                valid_passes_new += 1
    print(valid_passes)
    print(valid_passes_new)
