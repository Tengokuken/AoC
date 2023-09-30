winners = [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19), (20, 21, 22, 23, 24),
           (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 19, 22), (3, 8, 13, 18, 23), (4, 9, 14, 19, 24)]
"""
numbers is a list of integers
bingo_cards is a list where each element contains a 2D list representing a 5x5 bingo card
"""
def win_bingo(numbers, bingo_cards):
    cards = []
    for i in range(len(bingo_cards)):
        cards.append([])
    for number in numbers:
        for i in range(len(bingo_cards)):
            for row in range(5):
                if number in bingo_cards[i][row]:
                    loc = row * 5 + bingo_cards[i][row].index(number)
                    cards[i].append(loc)
                    # Check if there is a winning card
                    for winner in winners:
                        if all(elem in cards[i] for elem in winner):
                            unmarked = [x for x in list(range(0, 25)) if x not in cards[i]]
                            summation = 0
                            for unmarked_num in unmarked:
                                summation += int(bingo_cards[i][unmarked_num // 5][unmarked_num % 5])
                            return summation * int(number)

# Get last winning card
def lose_dingo(numbers, bingo_cards):
    cards = []
    for i in range(len(bingo_cards)):
        cards.append([])
    for number in numbers:
        winning_cards = []
        for i in range(len(bingo_cards)):
            for row in range(5):
                if number in bingo_cards[i][row]:
                    loc = row * 5 + bingo_cards[i][row].index(number)
                    cards[i].append(loc)
                    # Check if there is a winning card
                    for winner in winners:
                        if all(elem in cards[i] for elem in winner):
                            winning_cards.append(i)
                            # Check if it is the last bingo card
                            if len(bingo_cards) == 1:
                                unmarked = [x for x in list(range(0, 25)) if x not in cards[i]]
                                summation = 0
                                for unmarked_num in unmarked:
                                    summation += int(bingo_cards[i][unmarked_num // 5][unmarked_num % 5])
                                print(summation)
                                return summation * int(number)
        if len(winning_cards) > 0:
            winning_cards.sort()
            deleted = 0
            for win in winning_cards:
                # Remove from playing cards
                bingo_cards.pop(win - deleted)
                cards.pop(win - deleted)
                deleted += 1

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    numbers = lines[0][:-1].split(',')
    bingo_cards = []
    bingo = []
    for i in range(2, len(lines)):
        # Read the bingo cards. Break the card if "" is read
        line = lines[i]
        bingo_line = line.split(" ")
        # remove white space, extra characters
        while '' in bingo_line:
            bingo_line.remove('')
        if i == len(lines) - 1:
            bingo_line[len(bingo_line) - 1] = bingo_line[len(bingo_line) - 1]
        else:
            bingo_line[len(bingo_line) - 1] = bingo_line[len(bingo_line) - 1][:-1]
        if bingo_line != ['']:
            bingo.append(bingo_line)
        if i == len(lines) - 1 or len(lines[i+1].split(' ')) == 1:
            bingo_cards.append(bingo)
            bingo = []
    file.close()
    result = win_bingo(numbers, bingo_cards)
    print(result)
    result = lose_dingo(numbers, bingo_cards)
    print(result)