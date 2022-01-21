#part 1
fwd = depth = 0
with open('day2_input1.txt') as file:
    for index, line in enumerate(file.readlines()):
        cmd = line.strip()
        if 'forward' in cmd:
            fwd += int(cmd.split(" ")[1])
        if 'down' in cmd:
            depth += int(cmd.split(" ")[1])
        if 'up' in cmd:
            depth -= int(cmd.split(" ")[1])
print(fwd, depth, fwd * depth)

#part 2
fwd = depth = aim = 0
with open('day2_input1.txt') as file:
    for index, line in enumerate(file.readlines()):
        cmd = line.strip()
        if 'forward' in cmd:
            fwd += int(cmd.split(" ")[1])
            if aim > 0:
                depth += int(cmd.split(" ")[1])*aim
        if 'down' in cmd:
            aim += int(cmd.split(" ")[1])
        if 'up' in cmd:
            aim -= int(cmd.split(" ")[1])
print(fwd, depth, fwd * depth)
