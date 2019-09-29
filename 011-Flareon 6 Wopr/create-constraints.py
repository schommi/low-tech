result_from_wrong = [
    0xA7, 0xBF, 0xD2, 0x9E, 0x0F, 0x01, 0x6B, 0x53,
    0x68, 0x37, 0xB7, 0x60, 0x7C, 0xBA, 0xB4, 0xA8]

xor_with = [212, 162, 242, 218, 101, 109, 50, 31, 125, 112, 249, 83, 55, 187, 131, 206]

h = []
for index in range(len(xor_with)):
    h.append (result_from_wrong[index] ^ xor_with[index])

# h = [115, 29, 32, 68, 106, 108, 89, 76, 21, 71, 78, 51, 75, 1, 55, 102]

calcs = [
    "x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[11] ^ x[14]",
    "x[0] ^ x[1] ^ x[8] ^ x[11] ^ x[13] ^ x[14]",
    "x[0] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[8] ^ x[9] ^ x[10] ^ x[13] ^ x[14] ^ x[15]",
    "x[5] ^ x[6] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[15]",
    "x[1] ^ x[6] ^ x[7] ^ x[8] ^ x[12] ^ x[13] ^ x[14] ^ x[15]",
    "x[0] ^ x[4] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[13] ^ x[14] ^ x[15]",
    "x[1] ^ x[3] ^ x[7] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[15]",
    "x[0] ^ x[1] ^ x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[10] ^ x[11] ^ x[14]",
    "x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[12]",
    "x[6] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[15]",
    " x[0] ^ x[3] ^ x[4] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15]",
    " x[0] ^ x[2] ^ x[4] ^ x[6] ^ x[13]",
    " x[0] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[12] ^ x[15]",
    " x[2] ^ x[3] ^ x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[11] ^ x[12] ^ x[13] ^ x[14]",
    " x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[7] ^ x[11] ^ x[13] ^ x[14] ^ x[15]",
    " x[1] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[13] ^ x[15]"
]

def get_vars(line, bit):
    result = ""
    for fragment in line.split("^"):
        fragment = fragment.strip()
        fragment = fragment.replace("x", "variables")
        fragment = fragment[:-1] + "," + str(bit) + fragment[-1:]
        if result != "":
            result = result + " + "
        result = result + fragment
    return result

for byte in range(len(h)):
  for bit in range(8):
    print ("variables[{0},{1}] >= 0 , variables [{0},{1}] <=1,".format(byte, 7-bit))

print("")

for byte in enumerate(h):
    print("# {0} ({1})".format(byte[1], byte[0]))

    for bit in range(8):
        target = (byte[1] >> 7-bit) & 1
        variables = get_vars(calcs[byte[0]], 7-bit)
        print ("{0} == ({1}) %2,".format(target, variables))
