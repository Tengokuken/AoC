def syntax_score(char, last):
    if char == ')' and last != '(':
        return 3
    if char == ']' and last != '[':
        return 57
    if char == '}' and last != '{':
        return 1197
    if char == '>' and last != '<':
        return 25137
    return 0

def corrupted(lines):
    score = 0
    closing = [')', ']', '}', '>']
    stack = []
    for line in lines:
        stack.clear()
        for char in line:
            if len(stack) != 0:
                last = stack[len(stack)-1]
                if char in closing:
                    this_score = syntax_score(char, last)
                    if this_score != 0:
                        score += this_score
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        else:
            continue
        # break
    return score

def incomplete(lines):
    scores = []
    score_dict = {')': 1, ']': 2, '}': 3, '>': 4}

    stack = []
    incomplete_closers = []
    for line in lines:
        stack.clear()
        for char in line:
            if len(stack) != 0:
                last = stack[len(stack)-1]
                if char in score_dict.keys():
                    this_score = syntax_score(char, last)
                    if this_score != 0: # corrupted, discard
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        else:
            # go through the stack, get the closing characters
            complete = ''
            while len(stack) != 0:
                symbol = stack.pop(len(stack) - 1)
                if symbol == '(':
                    complete += ')'
                elif symbol == '{':
                    complete += '}'
                elif symbol == '[':
                    complete += ']'
                elif symbol == '<':
                    complete += '>'
            incomplete_closers.append(complete)
            continue
    for sequence in incomplete_closers:
        score = 0
        for symbol in sequence:
            score = score * 5 + score_dict[symbol]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    score = corrupted(lines)
    print(score)
    numbers = incomplete(lines)
    print(numbers)