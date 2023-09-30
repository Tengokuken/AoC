#!/usr/bin/python3

data = open('input.txt', 'r').read().split('\n')[:-1]

firstPolymer = data[0]
insertions = dict()
for d in data[2:]:
    k,v = d.split(' -> ')
    insertions[k] = v

def createDatabase():
    database = dict()
    for i in range(len(firstPolymer)-1):
        pair = firstPolymer[i:i+2]
        if not pair in database:
            database[pair] = 0
        database[pair] += 1
    return database

def growPolymer(database):
    database_next = dict()
    for k,v in database.items():
        a = k[0]+insertions[k]
        b = insertions[k]+k[1]
        if (not a in database_next): database_next[a] = 0
        if (not b in database_next): database_next[b] = 0
        database_next[a] += v
        database_next[b] += v
    return database_next

def statsPolymer(database):
    atoms = dict()
    for k,v in database.items():
        # 2 chars 
        for i in k:
            if i not in atoms:
                atoms[i] = 0
            atoms[i] += v
    # the first and last atoms of the polymer never change
    # and they don't appear twice in the database as the middle atoms do
    atoms[firstPolymer[0]] += 1
    atoms[firstPolymer[-1]] += 1
    for k in atoms.keys():
        atoms[k] = int(atoms[k]/2)
    return atoms

def calculate(n):
    database = createDatabase()
    for i in range(n):
        database = growPolymer(database)
    atoms = statsPolymer(database)
    v = [v for v in atoms.values()]
    return max(v) - min(v)
    
print("Part 1:",calculate(10))
print("Part 2:",calculate(40))