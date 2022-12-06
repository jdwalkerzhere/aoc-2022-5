def move_one(stacks, from_stack, to_stack, quantity):
    moved = 0
    while moved < quantity:
        moving = stacks[from_stack].pop()
        stacks[to_stack].append(moving)
        moved += 1
    return stacks

def move_mult(stacks, from_stack, to_stack, quantity):
    stacks[to_stack] += stacks[from_stack][-1*quantity::]
    for i in range(quantity):
        stacks[from_stack].pop()
    return stacks
    
def part1(stacks, instructions):
    for instruction in instructions:
        quant = instruction[0]
        froms = instruction[1]
        to = instruction[2]
        move_one(stacks, froms, to, quant)
    return ''.join(i[-1] for i in stacks.values())

def part2(stacks, instructions):
    for instruction in instructions:
        quant = instruction[0]
        froms = instruction[1]
        to = instruction[2]
        move_mult(stacks, froms, to, quant)
    return ''.join(i[-1] for i in stacks.values())