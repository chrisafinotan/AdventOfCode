# part 1
from bitarray import bitarray
from bitarray.util import ba2int
report_len = 0
poscount1 = [0] * 12
poscount0 = [0] * 12
with open('day3_input1.txt') as file:
    for index, line in enumerate(file.readlines()):
        cmd = line.strip()
        for index2 in range(0, len(cmd)):
            if cmd[index2] == '1':
                poscount1[index2] += 1
            else:
                poscount0[index2] += 1
    report_len = index + 1

gR = eR = ""
for count in poscount1:
    if count > report_len / 2:
        gR += '1'
        eR += '0'
    else:
        gR += '0'
        eR += '1'

ba1 = bitarray(gR)
gammaRate = ba2int(ba1)
ba2 = bitarray(eR)
epsilonRate = ba2int(ba2)
print(f'gamma Rate: {gammaRate}\n'
      f'binary:[{gR}],-> {poscount1}\n'
      f'epsilon Rate: {epsilonRate}\n'
      f'binary:[{eR}],-> {poscount0}\n'
      f'power Consumption: {gammaRate*epsilonRate}')
