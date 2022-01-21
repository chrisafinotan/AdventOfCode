data = []
with open('input1.txt') as file:
    for index, line in enumerate(file.readlines()):
        data.append(line.strip())

#part 1
# prev = -1
# count = 0
# for value in data:
#     val = int(value)
#     if val > prev > 0:
#         count += 1
#     prev = val
#
# print(count)

#part 2
prev = -1, count = 0
threewindow = []
winCount = 0
for value in data:
    val = int(value)
    threewindow.append(val)
    if len(threewindow) == 4:
        prev = sum(threewindow[0:3])
        curr = sum(threewindow[1:])
        threewindow.pop(0)
        if curr > prev:
            count += 1
print(count)


