"""
Stores the information for a monkey

@items: list containing the items the monkey holds. Will be initalized on start
@operation: worry level multiplier. new = old * operation
@test: number to test worry level
@true: monkey will throw to <true> if <test> is true
@false: monkey will throw to <false> otherwise
"""
class Monkey:
    def __init__(self, items, operand, operator, test, true, false):
        self.items = items
        self.operand = operand
        self.operator = operator
        self.test = test
        self.true = true
        self.false = false

    def __repr__(self):
        return (str(self.items))

    def eval_operation(self, item):
        op = item if self.operand == "old" else int(self.operand)
        match self.operator:
            case "+":
                return item + op
            case "*":
                return item * op

    def eval_test(self, item):
        return self.true if item % self.test == 0 else self.false
def monkey_business(monkeys, part):
    # For part 2. division with large numbers is too expensive, while modulus isn't. checking if lcm is a factor
    # means its divisible.
    lcm = 1
    for i in range(len(monkeys)):
        lcm *= monkeys[i].test
    activity = [0] * len(monkeys)
    rounds = 20 if part == 1 else 10000
    for i in range(rounds):
        print("round", i+1)
        for j in range(len(monkeys)):
            # print("Monkey", j)
            for item in monkeys[j].items:
                result = monkeys[j].eval_operation(item)
                if part == 1:
                    result = result // 3
                else:
                    result = result % lcm
                throw_to = monkeys[j].eval_test(result)
                monkeys[throw_to].items.append(result)
                activity[j] += 1
            # simulate throwing all the items away
            monkeys[j].items = []

    print(activity)
    activity.sort(reverse=True)
    print(activity)
    return activity[0] * activity[1]

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    monkeys = []
    # every 7 lines is a monkey
    for i in range(0, len(lines), 7):
        num = lines[i].split()[1]
        starting = lines[i+1].split(":")[1]
        starting = starting.split(",")
        starting = [int(x) for x in starting]
        operation = lines[i+2].split(":")[1].strip().split()
        operand = operation[-1]
        operator = operation[-2]
        test = int(lines[i+3].split()[-1])
        true = int(lines[i+4].split()[-1])
        false = int(lines[i+5].split()[-1])
        print(num, starting, operation, operand, operator, test, true, false)
        monkey = Monkey(starting, operand, operator, test, true, false)
        monkeys.append(monkey)
    print(monkeys)
    result = monkey_business(monkeys, 2)
    print(result)

