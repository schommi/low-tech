import ctypes
import struct
import itertools

image = ''


def f_034E16B9(image, image_offset, code):
    ebp_p8 = 0x20
    esi = image
    edi = struct.unpack("I", esi[0 + image_offset:4 + image_offset])[0]
    ebx = struct.unpack("I", esi[4 + image_offset:8 + image_offset])[0]
    esi = 0

    while ebp_p8 > 0:
        ecx = code
        eax = esi & 3
        edx = ecx[eax]
        ecx = ebx
        ecx = ctypes.c_uint32(ecx << 4).value
        eax = ebx
        eax = eax >> 5
        edx = ctypes.c_uint32(edx + esi).value
        ecx = ecx ^ eax
        esi = ctypes.c_uint32(esi - 0x61c88647).value
        ecx = ctypes.c_uint32(ecx + ebx).value
        ecx ^= edx
        edx = code
        edi = ctypes.c_uint32(edi + ecx).value
        ecx = edi
        eax = edi
        eax >>= 5
        ecx = ctypes.c_uint32(ecx << 4).value
        ecx ^= eax
        eax = esi
        eax >>= 0xb
        ecx = ctypes.c_uint32(ecx + edi).value
        eax &= 3
        eax = edx[eax]
        eax = ctypes.c_uint32(eax + esi).value
        ecx ^= eax
        ebx = ctypes.c_uint32(ebx + ecx).value
        ebp_p8 -= 1

    return image[0: + image_offset] + struct.pack("I", edi) + struct.pack("I", ebx) + image[8 + image_offset:]


#with open("schommi.gif", "rb") as image_file:
#  expected = [0x24, 0x8E, 0xB0, 0x50, 0xE8, 0xB2, 0x68, 0x6F]
#  image = image_file.read()
#  for key in itertools.product(range(256),repeat=4):
#    print (key)
#    for width in range(100, 2000):
#      image_start = image[0:6] + struct.pack("H", width)
#      image = f_034E16B9(image_start, 0, key)
#      image_asarray = [x for x in image]
#      if expected == image_asarray:
#        print (key + ":" + width)
#
#exit()

with open("schommi.gif", "rb") as image_file:
    image = image_file.read()
    original_len = len(image)
    key = [
        0x7C, 0x7F, 0x7E, 0x79, 0x78, 0x7B, 0x7A, 0x75, 0x74, 0x7D, 0x7C, 0x7F, 0x7E, 0x79, 0x78, 0x7B,
        0x7A, 0x75, 0x74, 0x7D]

    for offset in range(0, (original_len // 8) * 8, 8):
        image = f_034E16B9(image, offset, key)

    with open("schommi.gif.encrypted", "wb") as out_file:
      out_file.write(image[0:original_len])

esp_p10 = 0x37b3  # file size
esp_p14 = 0
esp_p18 = 8
esp_p1c = 0

edi = 0
eax = esp_p14

if eax < 0:
    print("duh")
    edi += 1
    edx = esp_p10
    eax = -eax
    edx = -edx
    # sbb eax, 0
    esp_p14 = eax
    esp_p10 = edx

eax = esp_p1c
if eax < 0:
    print("duh")

if eax == 0:
    ecx = esp_p18
    eax = esp_p14
    edx = 0
    ebx = eax // 8
    eax = esp_p10 // 8
    edx = ebx
else:
    print("duh")

edi -= 1
if edi == 0:
    print("duh")
