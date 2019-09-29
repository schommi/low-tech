import itertools
import z3

combinations = {
}


def create_combinations():
    for length in range(1, 12):
        length_combinations = {
            0: [],
            1: []
        }

        for combination in itertools.product([0, 1], repeat=length):
            result = sum(combination) % 2
            length_combinations[result].append(combination)

        combinations[length] = length_combinations

def get_possible_bytes(target, sources):
  result = []
  
  combinations_for_length = combinations[len(sources)]
  

  for bit in range(8):
    lowest_bit = target & 1
    result.append(combinations_for_length[lowest_bit])
    target = target >> 1

  return result


create_combinations()

variables = {
}

for byte in range(16):
  for bit in range(8):
    variables[(byte, bit)] = z3.Int("x{0}_{1}".format(byte, bit))

solver = z3.Solver()
solver.add(
  # insert constraints from create-constraints.py here
variables[0,7] >= 0 , variables [0,7] <=1,
variables[0,6] >= 0 , variables [0,6] <=1,
variables[0,5] >= 0 , variables [0,5] <=1,
variables[0,4] >= 0 , variables [0,4] <=1,
variables[0,3] >= 0 , variables [0,3] <=1,
variables[0,2] >= 0 , variables [0,2] <=1,
variables[0,1] >= 0 , variables [0,1] <=1,
variables[0,0] >= 0 , variables [0,0] <=1,
variables[1,7] >= 0 , variables [1,7] <=1,
variables[1,6] >= 0 , variables [1,6] <=1,
variables[1,5] >= 0 , variables [1,5] <=1,
variables[1,4] >= 0 , variables [1,4] <=1,
variables[1,3] >= 0 , variables [1,3] <=1,
variables[1,2] >= 0 , variables [1,2] <=1,
variables[1,1] >= 0 , variables [1,1] <=1,
variables[1,0] >= 0 , variables [1,0] <=1,
variables[2,7] >= 0 , variables [2,7] <=1,
variables[2,6] >= 0 , variables [2,6] <=1,
variables[2,5] >= 0 , variables [2,5] <=1,
variables[2,4] >= 0 , variables [2,4] <=1,
variables[2,3] >= 0 , variables [2,3] <=1,
variables[2,2] >= 0 , variables [2,2] <=1,
variables[2,1] >= 0 , variables [2,1] <=1,
variables[2,0] >= 0 , variables [2,0] <=1,
variables[3,7] >= 0 , variables [3,7] <=1,
variables[3,6] >= 0 , variables [3,6] <=1,
variables[3,5] >= 0 , variables [3,5] <=1,
variables[3,4] >= 0 , variables [3,4] <=1,
variables[3,3] >= 0 , variables [3,3] <=1,
variables[3,2] >= 0 , variables [3,2] <=1,
variables[3,1] >= 0 , variables [3,1] <=1,
variables[3,0] >= 0 , variables [3,0] <=1,
variables[4,7] >= 0 , variables [4,7] <=1,
variables[4,6] >= 0 , variables [4,6] <=1,
variables[4,5] >= 0 , variables [4,5] <=1,
variables[4,4] >= 0 , variables [4,4] <=1,
variables[4,3] >= 0 , variables [4,3] <=1,
variables[4,2] >= 0 , variables [4,2] <=1,
variables[4,1] >= 0 , variables [4,1] <=1,
variables[4,0] >= 0 , variables [4,0] <=1,
variables[5,7] >= 0 , variables [5,7] <=1,
variables[5,6] >= 0 , variables [5,6] <=1,
variables[5,5] >= 0 , variables [5,5] <=1,
variables[5,4] >= 0 , variables [5,4] <=1,
variables[5,3] >= 0 , variables [5,3] <=1,
variables[5,2] >= 0 , variables [5,2] <=1,
variables[5,1] >= 0 , variables [5,1] <=1,
variables[5,0] >= 0 , variables [5,0] <=1,
variables[6,7] >= 0 , variables [6,7] <=1,
variables[6,6] >= 0 , variables [6,6] <=1,
variables[6,5] >= 0 , variables [6,5] <=1,
variables[6,4] >= 0 , variables [6,4] <=1,
variables[6,3] >= 0 , variables [6,3] <=1,
variables[6,2] >= 0 , variables [6,2] <=1,
variables[6,1] >= 0 , variables [6,1] <=1,
variables[6,0] >= 0 , variables [6,0] <=1,
variables[7,7] >= 0 , variables [7,7] <=1,
variables[7,6] >= 0 , variables [7,6] <=1,
variables[7,5] >= 0 , variables [7,5] <=1,
variables[7,4] >= 0 , variables [7,4] <=1,
variables[7,3] >= 0 , variables [7,3] <=1,
variables[7,2] >= 0 , variables [7,2] <=1,
variables[7,1] >= 0 , variables [7,1] <=1,
variables[7,0] >= 0 , variables [7,0] <=1,
variables[8,7] >= 0 , variables [8,7] <=1,
variables[8,6] >= 0 , variables [8,6] <=1,
variables[8,5] >= 0 , variables [8,5] <=1,
variables[8,4] >= 0 , variables [8,4] <=1,
variables[8,3] >= 0 , variables [8,3] <=1,
variables[8,2] >= 0 , variables [8,2] <=1,
variables[8,1] >= 0 , variables [8,1] <=1,
variables[8,0] >= 0 , variables [8,0] <=1,
variables[9,7] >= 0 , variables [9,7] <=1,
variables[9,6] >= 0 , variables [9,6] <=1,
variables[9,5] >= 0 , variables [9,5] <=1,
variables[9,4] >= 0 , variables [9,4] <=1,
variables[9,3] >= 0 , variables [9,3] <=1,
variables[9,2] >= 0 , variables [9,2] <=1,
variables[9,1] >= 0 , variables [9,1] <=1,
variables[9,0] >= 0 , variables [9,0] <=1,
variables[10,7] >= 0 , variables [10,7] <=1,
variables[10,6] >= 0 , variables [10,6] <=1,
variables[10,5] >= 0 , variables [10,5] <=1,
variables[10,4] >= 0 , variables [10,4] <=1,
variables[10,3] >= 0 , variables [10,3] <=1,
variables[10,2] >= 0 , variables [10,2] <=1,
variables[10,1] >= 0 , variables [10,1] <=1,
variables[10,0] >= 0 , variables [10,0] <=1,
variables[11,7] >= 0 , variables [11,7] <=1,
variables[11,6] >= 0 , variables [11,6] <=1,
variables[11,5] >= 0 , variables [11,5] <=1,
variables[11,4] >= 0 , variables [11,4] <=1,
variables[11,3] >= 0 , variables [11,3] <=1,
variables[11,2] >= 0 , variables [11,2] <=1,
variables[11,1] >= 0 , variables [11,1] <=1,
variables[11,0] >= 0 , variables [11,0] <=1,
variables[12,7] >= 0 , variables [12,7] <=1,
variables[12,6] >= 0 , variables [12,6] <=1,
variables[12,5] >= 0 , variables [12,5] <=1,
variables[12,4] >= 0 , variables [12,4] <=1,
variables[12,3] >= 0 , variables [12,3] <=1,
variables[12,2] >= 0 , variables [12,2] <=1,
variables[12,1] >= 0 , variables [12,1] <=1,
variables[12,0] >= 0 , variables [12,0] <=1,
variables[13,7] >= 0 , variables [13,7] <=1,
variables[13,6] >= 0 , variables [13,6] <=1,
variables[13,5] >= 0 , variables [13,5] <=1,
variables[13,4] >= 0 , variables [13,4] <=1,
variables[13,3] >= 0 , variables [13,3] <=1,
variables[13,2] >= 0 , variables [13,2] <=1,
variables[13,1] >= 0 , variables [13,1] <=1,
variables[13,0] >= 0 , variables [13,0] <=1,
variables[14,7] >= 0 , variables [14,7] <=1,
variables[14,6] >= 0 , variables [14,6] <=1,
variables[14,5] >= 0 , variables [14,5] <=1,
variables[14,4] >= 0 , variables [14,4] <=1,
variables[14,3] >= 0 , variables [14,3] <=1,
variables[14,2] >= 0 , variables [14,2] <=1,
variables[14,1] >= 0 , variables [14,1] <=1,
variables[14,0] >= 0 , variables [14,0] <=1,
variables[15,7] >= 0 , variables [15,7] <=1,
variables[15,6] >= 0 , variables [15,6] <=1,
variables[15,5] >= 0 , variables [15,5] <=1,
variables[15,4] >= 0 , variables [15,4] <=1,
variables[15,3] >= 0 , variables [15,3] <=1,
variables[15,2] >= 0 , variables [15,2] <=1,
variables[15,1] >= 0 , variables [15,1] <=1,
variables[15,0] >= 0 , variables [15,0] <=1,

# 115 (0)
0 == (variables[2,7] + variables[3,7] + variables[4,7] + variables[8,7] + variables[11,7] + variables[14,7]) %2,
1 == (variables[2,6] + variables[3,6] + variables[4,6] + variables[8,6] + variables[11,6] + variables[14,6]) %2,
1 == (variables[2,5] + variables[3,5] + variables[4,5] + variables[8,5] + variables[11,5] + variables[14,5]) %2,
1 == (variables[2,4] + variables[3,4] + variables[4,4] + variables[8,4] + variables[11,4] + variables[14,4]) %2,
0 == (variables[2,3] + variables[3,3] + variables[4,3] + variables[8,3] + variables[11,3] + variables[14,3]) %2,
0 == (variables[2,2] + variables[3,2] + variables[4,2] + variables[8,2] + variables[11,2] + variables[14,2]) %2,
1 == (variables[2,1] + variables[3,1] + variables[4,1] + variables[8,1] + variables[11,1] + variables[14,1]) %2,
1 == (variables[2,0] + variables[3,0] + variables[4,0] + variables[8,0] + variables[11,0] + variables[14,0]) %2,
# 29 (1)
0 == (variables[0,7] + variables[1,7] + variables[8,7] + variables[11,7] + variables[13,7] + variables[14,7]) %2,
0 == (variables[0,6] + variables[1,6] + variables[8,6] + variables[11,6] + variables[13,6] + variables[14,6]) %2,
0 == (variables[0,5] + variables[1,5] + variables[8,5] + variables[11,5] + variables[13,5] + variables[14,5]) %2,
1 == (variables[0,4] + variables[1,4] + variables[8,4] + variables[11,4] + variables[13,4] + variables[14,4]) %2,
1 == (variables[0,3] + variables[1,3] + variables[8,3] + variables[11,3] + variables[13,3] + variables[14,3]) %2,
1 == (variables[0,2] + variables[1,2] + variables[8,2] + variables[11,2] + variables[13,2] + variables[14,2]) %2,
0 == (variables[0,1] + variables[1,1] + variables[8,1] + variables[11,1] + variables[13,1] + variables[14,1]) %2,
1 == (variables[0,0] + variables[1,0] + variables[8,0] + variables[11,0] + variables[13,0] + variables[14,0]) %2,
# 32 (2)
0 == (variables[0,7] + variables[1,7] + variables[2,7] + variables[4,7] + variables[5,7] + variables[8,7] + variables[9,7] + variables[10,7] + variables[13,7] + variables[14,7] + variables[15,7]) %2,
0 == (variables[0,6] + variables[1,6] + variables[2,6] + variables[4,6] + variables[5,6] + variables[8,6] + variables[9,6] + variables[10,6] + variables[13,6] + variables[14,6] + variables[15,6]) %2,
1 == (variables[0,5] + variables[1,5] + variables[2,5] + variables[4,5] + variables[5,5] + variables[8,5] + variables[9,5] + variables[10,5] + variables[13,5] + variables[14,5] + variables[15,5]) %2,
0 == (variables[0,4] + variables[1,4] + variables[2,4] + variables[4,4] + variables[5,4] + variables[8,4] + variables[9,4] + variables[10,4] + variables[13,4] + variables[14,4] + variables[15,4]) %2,
0 == (variables[0,3] + variables[1,3] + variables[2,3] + variables[4,3] + variables[5,3] + variables[8,3] + variables[9,3] + variables[10,3] + variables[13,3] + variables[14,3] + variables[15,3]) %2,
0 == (variables[0,2] + variables[1,2] + variables[2,2] + variables[4,2] + variables[5,2] + variables[8,2] + variables[9,2] + variables[10,2] + variables[13,2] + variables[14,2] + variables[15,2]) %2,
0 == (variables[0,1] + variables[1,1] + variables[2,1] + variables[4,1] + variables[5,1] + variables[8,1] + variables[9,1] + variables[10,1] + variables[13,1] + variables[14,1] + variables[15,1]) %2,
0 == (variables[0,0] + variables[1,0] + variables[2,0] + variables[4,0] + variables[5,0] + variables[8,0] + variables[9,0] + variables[10,0] + variables[13,0] + variables[14,0] + variables[15,0]) %2,
# 68 (3)
0 == (variables[5,7] + variables[6,7] + variables[8,7] + variables[9,7] + variables[10,7] + variables[12,7] + variables[15,7]) %2,
1 == (variables[5,6] + variables[6,6] + variables[8,6] + variables[9,6] + variables[10,6] + variables[12,6] + variables[15,6]) %2,
0 == (variables[5,5] + variables[6,5] + variables[8,5] + variables[9,5] + variables[10,5] + variables[12,5] + variables[15,5]) %2,
0 == (variables[5,4] + variables[6,4] + variables[8,4] + variables[9,4] + variables[10,4] + variables[12,4] + variables[15,4]) %2,
0 == (variables[5,3] + variables[6,3] + variables[8,3] + variables[9,3] + variables[10,3] + variables[12,3] + variables[15,3]) %2,
1 == (variables[5,2] + variables[6,2] + variables[8,2] + variables[9,2] + variables[10,2] + variables[12,2] + variables[15,2]) %2,
0 == (variables[5,1] + variables[6,1] + variables[8,1] + variables[9,1] + variables[10,1] + variables[12,1] + variables[15,1]) %2,
0 == (variables[5,0] + variables[6,0] + variables[8,0] + variables[9,0] + variables[10,0] + variables[12,0] + variables[15,0]) %2,
# 106 (4)
0 == (variables[1,7] + variables[6,7] + variables[7,7] + variables[8,7] + variables[12,7] + variables[13,7] + variables[14,7] + variables[15,7]) %2,
1 == (variables[1,6] + variables[6,6] + variables[7,6] + variables[8,6] + variables[12,6] + variables[13,6] + variables[14,6] + variables[15,6]) %2,
1 == (variables[1,5] + variables[6,5] + variables[7,5] + variables[8,5] + variables[12,5] + variables[13,5] + variables[14,5] + variables[15,5]) %2,
0 == (variables[1,4] + variables[6,4] + variables[7,4] + variables[8,4] + variables[12,4] + variables[13,4] + variables[14,4] + variables[15,4]) %2,
1 == (variables[1,3] + variables[6,3] + variables[7,3] + variables[8,3] + variables[12,3] + variables[13,3] + variables[14,3] + variables[15,3]) %2,
0 == (variables[1,2] + variables[6,2] + variables[7,2] + variables[8,2] + variables[12,2] + variables[13,2] + variables[14,2] + variables[15,2]) %2,
1 == (variables[1,1] + variables[6,1] + variables[7,1] + variables[8,1] + variables[12,1] + variables[13,1] + variables[14,1] + variables[15,1]) %2,
0 == (variables[1,0] + variables[6,0] + variables[7,0] + variables[8,0] + variables[12,0] + variables[13,0] + variables[14,0] + variables[15,0]) %2,
# 108 (5)
0 == (variables[0,7] + variables[4,7] + variables[7,7] + variables[8,7] + variables[9,7] + variables[10,7] + variables[12,7] + variables[13,7] + variables[14,7] + variables[15,7]) %2,
1 == (variables[0,6] + variables[4,6] + variables[7,6] + variables[8,6] + variables[9,6] + variables[10,6] + variables[12,6] + variables[13,6] + variables[14,6] + variables[15,6]) %2,
1 == (variables[0,5] + variables[4,5] + variables[7,5] + variables[8,5] + variables[9,5] + variables[10,5] + variables[12,5] + variables[13,5] + variables[14,5] + variables[15,5]) %2,
0 == (variables[0,4] + variables[4,4] + variables[7,4] + variables[8,4] + variables[9,4] + variables[10,4] + variables[12,4] + variables[13,4] + variables[14,4] + variables[15,4]) %2,
1 == (variables[0,3] + variables[4,3] + variables[7,3] + variables[8,3] + variables[9,3] + variables[10,3] + variables[12,3] + variables[13,3] + variables[14,3] + variables[15,3]) %2,
1 == (variables[0,2] + variables[4,2] + variables[7,2] + variables[8,2] + variables[9,2] + variables[10,2] + variables[12,2] + variables[13,2] + variables[14,2] + variables[15,2]) %2,
0 == (variables[0,1] + variables[4,1] + variables[7,1] + variables[8,1] + variables[9,1] + variables[10,1] + variables[12,1] + variables[13,1] + variables[14,1] + variables[15,1]) %2,
0 == (variables[0,0] + variables[4,0] + variables[7,0] + variables[8,0] + variables[9,0] + variables[10,0] + variables[12,0] + variables[13,0] + variables[14,0] + variables[15,0]) %2,
# 89 (6)
0 == (variables[1,7] + variables[3,7] + variables[7,7] + variables[9,7] + variables[10,7] + variables[11,7] + variables[12,7] + variables[13,7] + variables[15,7]) %2,
1 == (variables[1,6] + variables[3,6] + variables[7,6] + variables[9,6] + variables[10,6] + variables[11,6] + variables[12,6] + variables[13,6] + variables[15,6]) %2,
0 == (variables[1,5] + variables[3,5] + variables[7,5] + variables[9,5] + variables[10,5] + variables[11,5] + variables[12,5] + variables[13,5] + variables[15,5]) %2,
1 == (variables[1,4] + variables[3,4] + variables[7,4] + variables[9,4] + variables[10,4] + variables[11,4] + variables[12,4] + variables[13,4] + variables[15,4]) %2,
1 == (variables[1,3] + variables[3,3] + variables[7,3] + variables[9,3] + variables[10,3] + variables[11,3] + variables[12,3] + variables[13,3] + variables[15,3]) %2,
0 == (variables[1,2] + variables[3,2] + variables[7,2] + variables[9,2] + variables[10,2] + variables[11,2] + variables[12,2] + variables[13,2] + variables[15,2]) %2,
0 == (variables[1,1] + variables[3,1] + variables[7,1] + variables[9,1] + variables[10,1] + variables[11,1] + variables[12,1] + variables[13,1] + variables[15,1]) %2,
1 == (variables[1,0] + variables[3,0] + variables[7,0] + variables[9,0] + variables[10,0] + variables[11,0] + variables[12,0] + variables[13,0] + variables[15,0]) %2,
# 76 (7)
0 == (variables[0,7] + variables[1,7] + variables[2,7] + variables[3,7] + variables[4,7] + variables[8,7] + variables[10,7] + variables[11,7] + variables[14,7]) %2,
1 == (variables[0,6] + variables[1,6] + variables[2,6] + variables[3,6] + variables[4,6] + variables[8,6] + variables[10,6] + variables[11,6] + variables[14,6]) %2,
0 == (variables[0,5] + variables[1,5] + variables[2,5] + variables[3,5] + variables[4,5] + variables[8,5] + variables[10,5] + variables[11,5] + variables[14,5]) %2,
0 == (variables[0,4] + variables[1,4] + variables[2,4] + variables[3,4] + variables[4,4] + variables[8,4] + variables[10,4] + variables[11,4] + variables[14,4]) %2,
1 == (variables[0,3] + variables[1,3] + variables[2,3] + variables[3,3] + variables[4,3] + variables[8,3] + variables[10,3] + variables[11,3] + variables[14,3]) %2,
1 == (variables[0,2] + variables[1,2] + variables[2,2] + variables[3,2] + variables[4,2] + variables[8,2] + variables[10,2] + variables[11,2] + variables[14,2]) %2,
0 == (variables[0,1] + variables[1,1] + variables[2,1] + variables[3,1] + variables[4,1] + variables[8,1] + variables[10,1] + variables[11,1] + variables[14,1]) %2,
0 == (variables[0,0] + variables[1,0] + variables[2,0] + variables[3,0] + variables[4,0] + variables[8,0] + variables[10,0] + variables[11,0] + variables[14,0]) %2,
# 21 (8)
0 == (variables[1,7] + variables[2,7] + variables[3,7] + variables[5,7] + variables[9,7] + variables[10,7] + variables[11,7] + variables[12,7]) %2,
0 == (variables[1,6] + variables[2,6] + variables[3,6] + variables[5,6] + variables[9,6] + variables[10,6] + variables[11,6] + variables[12,6]) %2,
0 == (variables[1,5] + variables[2,5] + variables[3,5] + variables[5,5] + variables[9,5] + variables[10,5] + variables[11,5] + variables[12,5]) %2,
1 == (variables[1,4] + variables[2,4] + variables[3,4] + variables[5,4] + variables[9,4] + variables[10,4] + variables[11,4] + variables[12,4]) %2,
0 == (variables[1,3] + variables[2,3] + variables[3,3] + variables[5,3] + variables[9,3] + variables[10,3] + variables[11,3] + variables[12,3]) %2,
1 == (variables[1,2] + variables[2,2] + variables[3,2] + variables[5,2] + variables[9,2] + variables[10,2] + variables[11,2] + variables[12,2]) %2,
0 == (variables[1,1] + variables[2,1] + variables[3,1] + variables[5,1] + variables[9,1] + variables[10,1] + variables[11,1] + variables[12,1]) %2,
1 == (variables[1,0] + variables[2,0] + variables[3,0] + variables[5,0] + variables[9,0] + variables[10,0] + variables[11,0] + variables[12,0]) %2,
# 71 (9)
0 == (variables[6,7] + variables[7,7] + variables[8,7] + variables[10,7] + variables[11,7] + variables[12,7] + variables[15,7]) %2,
1 == (variables[6,6] + variables[7,6] + variables[8,6] + variables[10,6] + variables[11,6] + variables[12,6] + variables[15,6]) %2,
0 == (variables[6,5] + variables[7,5] + variables[8,5] + variables[10,5] + variables[11,5] + variables[12,5] + variables[15,5]) %2,
0 == (variables[6,4] + variables[7,4] + variables[8,4] + variables[10,4] + variables[11,4] + variables[12,4] + variables[15,4]) %2,
0 == (variables[6,3] + variables[7,3] + variables[8,3] + variables[10,3] + variables[11,3] + variables[12,3] + variables[15,3]) %2,
1 == (variables[6,2] + variables[7,2] + variables[8,2] + variables[10,2] + variables[11,2] + variables[12,2] + variables[15,2]) %2,
1 == (variables[6,1] + variables[7,1] + variables[8,1] + variables[10,1] + variables[11,1] + variables[12,1] + variables[15,1]) %2,
1 == (variables[6,0] + variables[7,0] + variables[8,0] + variables[10,0] + variables[11,0] + variables[12,0] + variables[15,0]) %2,
# 78 (10)
0 == (variables[0,7] + variables[3,7] + variables[4,7] + variables[7,7] + variables[8,7] + variables[10,7] + variables[11,7] + variables[12,7] + variables[13,7] + variables[14,7] + variables[15,7]) %2,
1 == (variables[0,6] + variables[3,6] + variables[4,6] + variables[7,6] + variables[8,6] + variables[10,6] + variables[11,6] + variables[12,6] + variables[13,6] + variables[14,6] + variables[15,6]) %2,
0 == (variables[0,5] + variables[3,5] + variables[4,5] + variables[7,5] + variables[8,5] + variables[10,5] + variables[11,5] + variables[12,5] + variables[13,5] + variables[14,5] + variables[15,5]) %2,
0 == (variables[0,4] + variables[3,4] + variables[4,4] + variables[7,4] + variables[8,4] + variables[10,4] + variables[11,4] + variables[12,4] + variables[13,4] + variables[14,4] + variables[15,4]) %2,
1 == (variables[0,3] + variables[3,3] + variables[4,3] + variables[7,3] + variables[8,3] + variables[10,3] + variables[11,3] + variables[12,3] + variables[13,3] + variables[14,3] + variables[15,3]) %2,
1 == (variables[0,2] + variables[3,2] + variables[4,2] + variables[7,2] + variables[8,2] + variables[10,2] + variables[11,2] + variables[12,2] + variables[13,2] + variables[14,2] + variables[15,2]) %2,
1 == (variables[0,1] + variables[3,1] + variables[4,1] + variables[7,1] + variables[8,1] + variables[10,1] + variables[11,1] + variables[12,1] + variables[13,1] + variables[14,1] + variables[15,1]) %2,
0 == (variables[0,0] + variables[3,0] + variables[4,0] + variables[7,0] + variables[8,0] + variables[10,0] + variables[11,0] + variables[12,0] + variables[13,0] + variables[14,0] + variables[15,0]) %2,
# 51 (11)
0 == (variables[0,7] + variables[2,7] + variables[4,7] + variables[6,7] + variables[13,7]) %2,
0 == (variables[0,6] + variables[2,6] + variables[4,6] + variables[6,6] + variables[13,6]) %2,
1 == (variables[0,5] + variables[2,5] + variables[4,5] + variables[6,5] + variables[13,5]) %2,
1 == (variables[0,4] + variables[2,4] + variables[4,4] + variables[6,4] + variables[13,4]) %2,
0 == (variables[0,3] + variables[2,3] + variables[4,3] + variables[6,3] + variables[13,3]) %2,
0 == (variables[0,2] + variables[2,2] + variables[4,2] + variables[6,2] + variables[13,2]) %2,
1 == (variables[0,1] + variables[2,1] + variables[4,1] + variables[6,1] + variables[13,1]) %2,
1 == (variables[0,0] + variables[2,0] + variables[4,0] + variables[6,0] + variables[13,0]) %2,
# 75 (12)
0 == (variables[0,7] + variables[3,7] + variables[6,7] + variables[7,7] + variables[10,7] + variables[12,7] + variables[15,7]) %2,
1 == (variables[0,6] + variables[3,6] + variables[6,6] + variables[7,6] + variables[10,6] + variables[12,6] + variables[15,6]) %2,
0 == (variables[0,5] + variables[3,5] + variables[6,5] + variables[7,5] + variables[10,5] + variables[12,5] + variables[15,5]) %2,
0 == (variables[0,4] + variables[3,4] + variables[6,4] + variables[7,4] + variables[10,4] + variables[12,4] + variables[15,4]) %2,
1 == (variables[0,3] + variables[3,3] + variables[6,3] + variables[7,3] + variables[10,3] + variables[12,3] + variables[15,3]) %2,
0 == (variables[0,2] + variables[3,2] + variables[6,2] + variables[7,2] + variables[10,2] + variables[12,2] + variables[15,2]) %2,
1 == (variables[0,1] + variables[3,1] + variables[6,1] + variables[7,1] + variables[10,1] + variables[12,1] + variables[15,1]) %2,
1 == (variables[0,0] + variables[3,0] + variables[6,0] + variables[7,0] + variables[10,0] + variables[12,0] + variables[15,0]) %2,
# 1 (13)
0 == (variables[2,7] + variables[3,7] + variables[4,7] + variables[5,7] + variables[6,7] + variables[7,7] + variables[11,7] + variables[12,7] + variables[13,7] + variables[14,7]) %2,
0 == (variables[2,6] + variables[3,6] + variables[4,6] + variables[5,6] + variables[6,6] + variables[7,6] + variables[11,6] + variables[12,6] + variables[13,6] + variables[14,6]) %2,
0 == (variables[2,5] + variables[3,5] + variables[4,5] + variables[5,5] + variables[6,5] + variables[7,5] + variables[11,5] + variables[12,5] + variables[13,5] + variables[14,5]) %2,
0 == (variables[2,4] + variables[3,4] + variables[4,4] + variables[5,4] + variables[6,4] + variables[7,4] + variables[11,4] + variables[12,4] + variables[13,4] + variables[14,4]) %2,
0 == (variables[2,3] + variables[3,3] + variables[4,3] + variables[5,3] + variables[6,3] + variables[7,3] + variables[11,3] + variables[12,3] + variables[13,3] + variables[14,3]) %2,
0 == (variables[2,2] + variables[3,2] + variables[4,2] + variables[5,2] + variables[6,2] + variables[7,2] + variables[11,2] + variables[12,2] + variables[13,2] + variables[14,2]) %2,
0 == (variables[2,1] + variables[3,1] + variables[4,1] + variables[5,1] + variables[6,1] + variables[7,1] + variables[11,1] + variables[12,1] + variables[13,1] + variables[14,1]) %2,
1 == (variables[2,0] + variables[3,0] + variables[4,0] + variables[5,0] + variables[6,0] + variables[7,0] + variables[11,0] + variables[12,0] + variables[13,0] + variables[14,0]) %2,
# 55 (14)
0 == (variables[1,7] + variables[2,7] + variables[3,7] + variables[5,7] + variables[7,7] + variables[11,7] + variables[13,7] + variables[14,7] + variables[15,7]) %2,
0 == (variables[1,6] + variables[2,6] + variables[3,6] + variables[5,6] + variables[7,6] + variables[11,6] + variables[13,6] + variables[14,6] + variables[15,6]) %2,
1 == (variables[1,5] + variables[2,5] + variables[3,5] + variables[5,5] + variables[7,5] + variables[11,5] + variables[13,5] + variables[14,5] + variables[15,5]) %2,
1 == (variables[1,4] + variables[2,4] + variables[3,4] + variables[5,4] + variables[7,4] + variables[11,4] + variables[13,4] + variables[14,4] + variables[15,4]) %2,
0 == (variables[1,3] + variables[2,3] + variables[3,3] + variables[5,3] + variables[7,3] + variables[11,3] + variables[13,3] + variables[14,3] + variables[15,3]) %2,
1 == (variables[1,2] + variables[2,2] + variables[3,2] + variables[5,2] + variables[7,2] + variables[11,2] + variables[13,2] + variables[14,2] + variables[15,2]) %2,
1 == (variables[1,1] + variables[2,1] + variables[3,1] + variables[5,1] + variables[7,1] + variables[11,1] + variables[13,1] + variables[14,1] + variables[15,1]) %2,
1 == (variables[1,0] + variables[2,0] + variables[3,0] + variables[5,0] + variables[7,0] + variables[11,0] + variables[13,0] + variables[14,0] + variables[15,0]) %2,
# 102 (15)
0 == (variables[1,7] + variables[3,7] + variables[5,7] + variables[9,7] + variables[10,7] + variables[11,7] + variables[13,7] + variables[15,7]) %2,
1 == (variables[1,6] + variables[3,6] + variables[5,6] + variables[9,6] + variables[10,6] + variables[11,6] + variables[13,6] + variables[15,6]) %2,
1 == (variables[1,5] + variables[3,5] + variables[5,5] + variables[9,5] + variables[10,5] + variables[11,5] + variables[13,5] + variables[15,5]) %2,
0 == (variables[1,4] + variables[3,4] + variables[5,4] + variables[9,4] + variables[10,4] + variables[11,4] + variables[13,4] + variables[15,4]) %2,
0 == (variables[1,3] + variables[3,3] + variables[5,3] + variables[9,3] + variables[10,3] + variables[11,3] + variables[13,3] + variables[15,3]) %2,
1 == (variables[1,2] + variables[3,2] + variables[5,2] + variables[9,2] + variables[10,2] + variables[11,2] + variables[13,2] + variables[15,2]) %2,
1 == (variables[1,1] + variables[3,1] + variables[5,1] + variables[9,1] + variables[10,1] + variables[11,1] + variables[13,1] + variables[15,1]) %2,
0 == (variables[1,0] + variables[3,0] + variables[5,0] + variables[9,0] + variables[10,0] + variables[11,0] + variables[13,0] + variables[15,0]) %2
)

#x = get_possible_bytes(203, [1, 2, 3, 4, 5])
solver.check()
print(solver.model())


