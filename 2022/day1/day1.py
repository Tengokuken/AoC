winners = [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19), (20, 21, 22, 23, 24),
           (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 19, 22), (3, 8, 13, 18, 23), (4, 9, 14, 19, 24)]
"""
numbers is a list of integers
bingo_cards is a list where each element contains a 2D list representing a 5x5 bingo card
"""
def highest_cals(lines):
    cal_list = [0]
    cur = 0
    for i in range(len(lines)):
        # Read line by line the input. Convert each line into an int and store in list, ending cell if blank read
        if lines[i] == "\n":
            cur += 1
            cal_list.append(0)
            continue
        cals = int(lines[i])
        cal_list[cur] += cals
    return (max(cal_list), cal_list)

def highest_three(cal_list):
    # take the top 3 and then return
    cal_list.sort()
    return sum(cal_list[-3::])

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    (result, cal_list) = highest_cals(lines)
    print(result)
    result = highest_three(cal_list)
    print(result)