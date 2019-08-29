name = "Andreas"

upper_name = name.upper()

sum = 0
for character in upper_name:
  if character != " ":
    sum = sum + (ord(character) * 0x1749) - 1

print("SnD-{0}".format(sum))
