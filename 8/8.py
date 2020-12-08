#!/usr/bin/python3
from collections import namedtuple

def run(instructions, inst_to_change=-1):
    visited = set() # already-visited instructions
    acc, i = 0, 0
    
    while i not in visited and i != len(instructions):
        visited.add(i)
        # change the name of the inst if specified
        name = instructions[i].name
        name = (name if (i != inst_to_change or name == "acc") else ("nop" if name == "jmp" else "jmp"))
        i, acc = do_inst[name](i, acc, instructions[i].val)
    
    return (i == len(instructions), acc)

do_inst = {
    "nop": lambda i, a, val: (i + 1, a),
    "acc": lambda i, a, val: (i + 1, a + val),
    "jmp": lambda i, a, val: (i + val, a),
}

with open("8/input.txt", "r") as f:
    lines = f.read().split("\n")

Inst = namedtuple("Inst", ["name", "val"])
instructions = list(map(lambda i: Inst(i.split(" ")[0], int(i.split(" ")[1])), lines))    


print("PART 1:")
finished, acc = run(instructions)
print(acc)

print("PART 2:")
for i, inst in enumerate(instructions):
    # just pass the instruction to the run fn - easier than playing around 
    # with the list mid-iteration
    finished, acc = run(instructions, i)
    if finished: 
        print(acc)