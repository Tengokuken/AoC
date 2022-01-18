# Using a Python dictionary to act as an adjacency list
mapp = {

}
def tenchains(inp, n):
    chain = inp
    for i in range(n):
        newchain = ''
        for j in range(len(chain) - 1):
            newchain += chain[j] + mapp[chain[j:j+2]]
        newchain += chain[len(chain)-1]
        chain = newchain
    all_char = set()
    occ = {}
    for i in chain:
        all_char.add(i)
    for char in all_char:
        occ[char] = chain.count(char)
    print(occ)
    return occ[max(occ, key=occ.get)] - occ[min(occ, key=occ.get)]

# Driver Code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    for i in range(2, len(lines)):
        line = lines[i].split(' -> ')
        mapp[line[0]] = line[1]
    print(mapp)
    score = tenchains(lines[0], 40)
    print(score)
    #numbers = incomplete(lines)
    #print(numbers)
