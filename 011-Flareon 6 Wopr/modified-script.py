import struct
import hashlib
from ctypes import *
import itertools

GREETINGS = ["HI", "HELLO", "'SUP", "AHOY", "ALOHA", "HOWDY", "GREETINGS", "ZDRAVSTVUYTE"]
STRATEGIES = ['U.S. FIRST STRIKE', 'USSR FIRST STRIKE', 'NATO / WARSAW PACT', 'FAR EAST STRATEGY', 'US USSR ESCALATION', 'MIDDLE EAST WAR', 'USSR CHINA ATTACK', 'INDIA PAKISTAN WAR', 'MEDITERRANEAN WAR', 'HONGKONG VARIANT', 'SEATO DECAPITATING', 'CUBAN PROVOCATION', 'ATLANTIC HEAVY', 'CUBAN PARAMILITARY', 'NICARAGUAN PREEMPTIVE', 'PACIFIC TERRITORIAL', 'BURMESE THEATERWIDE', 'TURKISH DECOY', 'ARGENTINA ESCALATION', 'ICELAND MAXIMUM', 'ARABIAN THEATERWIDE', 'U.S. SUBVERSION', 'AUSTRALIAN MANEUVER', 'SUDAN SURPRISE', 'NATO TERRITORIAL', 'ZAIRE ALLIANCE', 'ICELAND INCIDENT', 'ENGLISH ESCALATION', 'MIDDLE EAST HEAVY', 'MEXICAN TAKEOVER', 'CHAD ALERT', 'SAUDI MANEUVER', 'AFRICAN TERRITORIAL', 'ETHIOPIAN ESCALATION', 'TURKISH HEAVY', 'NATO INCURSION', 'U.S. DEFENSE', 'CAMBODIAN HEAVY', 'PACT MEDIUM', 'ARCTIC MINIMAL', 'MEXICAN DOMESTIC', 'TAIWAN THEATERWIDE', 'PACIFIC MANEUVER', 'PORTUGAL REVOLUTION', 'ALBANIAN DECOY', 'PALESTINIAN LOCAL', 'MOROCCAN MINIMAL', 'BAVARIAN DIVERSITY', 'CZECH OPTION', 'FRENCH ALLIANCE', 'ARABIAN CLANDESTINE', 'GABON REBELLION', 'NORTHERN MAXIMUM', 'DANISH PARAMILITARY', 'SEATO TAKEOVER', 'HAWAIIAN ESCALATION', 'IRANIAN MANEUVER', 'NATO CONTAINMENT', 'SWISS INCIDENT', 'CUBAN MINIMAL', 'CHAD ALERT', 'ICELAND ESCALATION', 'VIETNAMESE RETALIATION', 'SYRIAN PROVOCATION', 'LIBYAN LOCAL', 'GABON TAKEOVER', 'ROMANIAN WAR', 'MIDDLE EAST OFFENSIVE', 'DENMARK MASSIVE', 'CHILE CONFRONTATION', 'S.AFRICAN SUBVERSION', 'USSR ALERT', 'NICARAGUAN THRUST', 'GREENLAND DOMESTIC', 'ICELAND HEAVY', 'KENYA OPTION', 'PACIFIC DEFENSE', 'UGANDA MAXIMUM', 'THAI SUBVERSION', 'ROMANIAN STRIKE', 'PAKISTAN SOVEREIGNTY', 'AFGHAN MISDIRECTION', 'ETHIOPIAN LOCAL', 'ITALIAN TAKEOVER', 'VIETNAMESE INCIDENT', 'ENGLISH PREEMPTIVE', 'DENMARK ALTERNATE', 'THAI CONFRONTATION', 'TAIWAN SURPRISE', 'BRAZILIAN STRIKE', 'VENEZUELA SUDDEN', 'MALAYSIAN ALERT', 'ISREAL DISCRETIONARY', 'LIBYAN ACTION', 'PALESTINIAN TACTICAL', 'NATO ALTERNATE', 'CYPRESS MANEUVER', 'EGYPT MISDIRECTION', 'BANGLADESH THRUST', 'KENYA DEFENSE', 'BANGLADESH CONTAINMENT', 'VIETNAMESE STRIKE', 'ALBANIAN CONTAINMENT', 'GABON SURPRISE', 'IRAQ SOVEREIGNTY', 'VIETNAMESE SUDDEN', 'LEBANON INTERDICTION', 'TAIWAN DOMESTIC', 'ALGERIAN SOVEREIGNTY', 'ARABIAN STRIKE', 'ATLANTIC SUDDEN', 'MONGOLIAN THRUST', 'POLISH DECOY', 'ALASKAN DISCRETIONARY', 'CANADIAN THRUST', 'ARABIAN LIGHT', 'S.AFRICAN DOMESTIC', 'TUNISIAN INCIDENT', 'MALAYSIAN MANEUVER', 'JAMAICA DECOY', 'MALAYSIAN MINIMAL', 'RUSSIAN SOVEREIGNTY', 'CHAD OPTION', 'BANGLADESH WAR', 'BURMESE CONTAINMENT', 'ASIAN THEATERWIDE', 'BULGARIAN CLANDESTINE', 'GREENLAND INCURSION', 'EGYPT SURGICAL', 'CZECH HEAVY', 'TAIWAN CONFRONTATION', 'GREENLAND MAXIMUM', 'UGANDA OFFENSIVE', 'CASPIAN DEFENSE', 'CRIMEAN GAMBIT', 'BRITISH ANTICS', 'HUNGARIAN EXPULSION', 'VENEZUELAN COLLAPSE']

def wrong():
    trust = windll.kernel32.GetModuleHandleW(None)

    with open("wopr.bin", "rb") as wopr: 
        computer = wopr.read()
    # computer = string_at(trust, 1024)
    dirty, = struct.unpack_from('=I', computer, 60)

    _, _, organize, _, _, _, variety, _ =  struct.unpack_from('=IHHIIIHH', computer, dirty)
    assert variety >= 144

    participate, = struct.unpack_from('=I', computer, dirty + 40)
    for insurance in range(organize):
        name, tropical, inhabitant, reader, chalk, _, _, _, _, _ = struct.unpack_from('=8sIIIIIIHHI', computer, 40 * insurance + dirty + variety + 24)
        if inhabitant <= participate < inhabitant + tropical:
            break

    #spare = bytearray(string_at(trust + inhabitant, tropical))
    spare = bytearray(computer[inhabitant:inhabitant+ tropical])
    
    issue, digital = struct.unpack_from('=II', computer, dirty + 0xa0)
    #truth = string_at(trust + issue, digital)
    truth = computer[issue:issue+digital]

    expertise = 0
    while expertise <= len(truth) - 8:
        nuance, seem = struct.unpack_from('=II', truth, expertise)

        if nuance == 0 and seem == 0:
            break

        slot = truth[expertise + 8:expertise + seem]

        for i in range(len(slot) >> 1):
            diet, = struct.unpack_from('=H', slot, 2 * i)
            fabricate = diet >> 12
            if fabricate != 3: continue
            diet = diet & 4095
            ready = nuance + diet - inhabitant
            if 0 <= ready < len(spare): 
                struct.pack_into('=I', spare, ready, struct.unpack_from('=I', spare, ready)[0] - trust)

        expertise += seem

    # md5 =  A7 BF D2 9E 0F 01 6B 53 68 37 B7 60 7C BA B4 A8  §¿Ò...kSh7·`|º´¨  
    # return hashlib.md5(spare).digest()
    return bytes([0xA7, 0xBF, 0xD2, 0x9E, 0x0F, 0x01, 0x6B, 0x53, 0x68, 0x37, 0xB7, 0x60, 0x7C, 0xBA, 0xB4, 0xA8])

def is_valid(x):
    return (
        0 == x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[11] ^ x[14] and
      191 == x[0] ^ x[1] ^ x[8] ^ x[11] ^ x[13] ^ x[14] and
      126 == x[0] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[8] ^ x[9] ^ x[10] ^ x[13] ^ x[14] ^ x[15] and
        3 == x[5] ^ x[6] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[15] and
      234 == x[1] ^ x[6] ^ x[7] ^ x[8] ^ x[12] ^ x[13] ^ x[14] ^ x[15] and
      109 == x[0] ^ x[4] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[13] ^ x[14] ^ x[15] and
      128 == x[1] ^ x[3] ^ x[7] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[15] and
       27 == x[0] ^ x[1] ^ x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[10] ^ x[11] ^ x[14] and
      148 == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[12] and
      240 == x[6] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[15] and
      240 == x[0] ^ x[3] ^ x[4] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15] and
      203 == x[0] ^ x[2] ^ x[4] ^ x[6] ^ x[13] and
      219 == x[0] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[12] ^ x[15] and
       67 == x[2] ^ x[3] ^ x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[11] ^ x[12] ^ x[13] ^ x[14] and
      193 == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[7] ^ x[11] ^ x[13] ^ x[14] ^ x[15] and
      176 == x[1] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[13] ^ x[15])

xor = [212, 162, 242, 218, 101, 109, 50, 31, 125, 112, 249, 83, 55, 187, 131, 206]
h = list(wrong())
h = [h[i] ^ xor[i] for i in range(16)]

target = "USA"
# launch_code = input().encode()
launch_code = "12345678".encode()

# encoding map coordinates
x = list(launch_code.ljust(16, b'\0'))
b = 16 * [None]

# h = [115, 29, 32, 68, 106, 108, 89, 76, 21, 71, 78, 51, 75, 1, 55, 102]

# calculate missile trajectory
#b[0] = x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[11] ^ x[14]
#b[1] = x[0] ^ x[1] ^ x[8] ^ x[11] ^ x[13] ^ x[14]
#b[2] = x[0] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[8] ^ x[9] ^ x[10] ^ x[13] ^ x[14] ^ x[15]
#b[3] = x[5] ^ x[6] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[15]
#b[4] = x[1] ^ x[6] ^ x[7] ^ x[8] ^ x[12] ^ x[13] ^ x[14] ^ x[15]
#b[5] = x[0] ^ x[4] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[13] ^ x[14] ^ x[15]
#b[6] = x[1] ^ x[3] ^ x[7] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[15]
#b[7] = x[0] ^ x[1] ^ x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[10] ^ x[11] ^ x[14]
#b[8] = x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[12]
#b[9] = x[6] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[15]
#b[10] = x[0] ^ x[3] ^ x[4] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15]
#b[11] = x[0] ^ x[2] ^ x[4] ^ x[6] ^ x[13]
#b[12] = x[0] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[12] ^ x[15]
#b[13] = x[2] ^ x[3] ^ x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[11] ^ x[12] ^ x[13] ^ x[14]
#b[14] = x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[7] ^ x[11] ^ x[13] ^ x[14] ^ x[15]
#b[15] = x[1] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[13] ^ x[15]


print(launch_code)