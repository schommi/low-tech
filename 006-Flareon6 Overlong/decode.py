encrypted = [
	0xe0, 0x81, 0x89, 0xC0, 0xA0, 0xC1, 0xAE, 0xE0, 0x81, 0xA5, 0xC1, 0xB6,
	0xF0, 0x80, 0x81, 0xA5, 0xE0, 0x81, 0xB2, 0xF0, 0x80, 0x80, 0xA0, 0xE0,
	0x81, 0xA2, 0x72, 0x6F, 0xC1, 0xAB, 0x65, 0xE0, 0x80, 0xA0, 0xE0, 0x81,
	0xB4, 0xE0, 0x81, 0xA8, 0xC1, 0xA5, 0x20, 0xC1, 0xA5, 0xE0, 0x81, 0xAE,
	0x63, 0xC1, 0xAF, 0xE0, 0x81, 0xA4, 0xF0, 0x80, 0x81, 0xA9, 0x6E, 0xC1,
	0xA7, 0xC0, 0xBA, 0x20, 0x49, 0xF0, 0x80, 0x81, 0x9F, 0xC1, 0xA1, 0xC1,
	0x9F, 0xC1, 0x8D, 0xE0, 0x81, 0x9F, 0xC1, 0xB4, 0xF0, 0x80, 0x81, 0x9F,
	0xF0, 0x80, 0x81, 0xA8, 0xC1, 0x9F, 0xF0, 0x80, 0x81, 0xA5, 0xE0, 0x81,
	0x9F, 0xC1, 0xA5, 0xE0, 0x81, 0x9F, 0xF0, 0x80, 0x81, 0xAE, 0xC1, 0x9F,
	0xF0, 0x80, 0x81, 0x83, 0xC1, 0x9F, 0xE0, 0x81, 0xAF, 0xE0, 0x81, 0x9F,
	0xC1, 0x84, 0x5F, 0xE0, 0x81, 0xA9, 0xF0, 0x80, 0x81, 0x9F, 0x6E, 0xE0,
	0x81, 0x9F, 0xE0, 0x81, 0xA7, 0xE0, 0x81, 0x80, 0xF0, 0x80, 0x81, 0xA6,
	0xF0, 0x80, 0x81, 0xAC, 0xE0, 0x81, 0xA1, 0xC1, 0xB2, 0xC1, 0xA5, 0xF0,
	0x80, 0x80, 0xAD, 0xF0, 0x80, 0x81, 0xAF, 0x6E, 0xC0, 0xAE, 0xF0, 0x80,
	0x81, 0xA3, 0x6F, 0xF0, 0x80, 0x81, 0xAD, 0x00, 0xE0, 0x20, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF6, 0x20, 0x00, 0x00
]

def GetStepAndResult(encryptedBuffer, encryptedBufferIndex):

  # f0
  if (encryptedBuffer[encryptedBufferIndex] >> 3) == 0x1e:
    return (4, ((encryptedBuffer[encryptedBufferIndex + 2] & 0x3f) << 6) | encryptedBuffer[encryptedBufferIndex + 3] & 0x3f )

  # e0
  if (encryptedBuffer[encryptedBufferIndex] >> 4) == 0x0e:
    return (3, ((encryptedBuffer[encryptedBufferIndex + 1] & 0x3f) << 6) | encryptedBuffer[encryptedBufferIndex + 2] & 0x3f )
  
  # c0
  if (encryptedBuffer[encryptedBufferIndex] >> 5) == 6:
    return (2, ((encryptedBuffer[encryptedBufferIndex] & 0x1f) << 6) | encryptedBuffer[encryptedBufferIndex + 1] & 0x3f )

  return (1, encryptedBuffer[encryptedBufferIndex] )


def FindPossibleInstances(character):
  lower6Bits = character & 0x1f
  return map(lambda chr: chr[0], filter(lambda chr: chr[1] & 0x1f == lower6Bits, enumerate(encrypted)))

suffix = "@flare-on.com"

# Find possible instance of the known flag suffix "@flare-on.com"
for character in suffix:
  print(character)
  print(list(FindPossibleInstances(ord(character))))


# Iterate over encrypted data with ascending offsets
for startIndex in range(0, 0x8c):
  bufferIndex = startIndex
  output = ""
  for count in range(0, 0x3c):
    item = GetStepAndResult(encrypted, bufferIndex)

    bufferIndex += item [0]
    print(chr(item[1]),end="")
