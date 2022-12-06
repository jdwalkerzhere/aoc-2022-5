from utils import move_one, move_mult, part1, part2

if __name__ == '__main__':
    with open('stacks.txt','r') as stacks:
        stacks = [i.strip('\n').split(':') for i in stacks.readlines()]

    first_stacks = {int(i[0]):list(i[1]) for i in stacks}
    second_stacks = {int(i[0]):list(i[1]) for i in stacks}

    with open('instructions.txt','r') as inst:
        inst = [i.strip('\n').split(' ') for i in inst.readlines()]

    inst = [[int(i[j]) for j in range(len(i)) if j in [1,3,5]] for i in inst]

    print(part1(first_stacks, inst))
    print(part2(second_stacks, inst))