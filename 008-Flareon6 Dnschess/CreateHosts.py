enemy_pieces = {
  "g-knight": 0x6,
  "d-pawn": 0xb,
  "e-pawn": 0xc
}

moves = [
  ("pawn", "e2", "e4", "g-knight", "g8", "f6"),
  ("pawn", "d2", "d4", "g-knight", "f6", "g8")
]

def get_dns_query(move):
  return move[0] + "-" + move[1] + "-" + move[2] + ".game-of-thrones.flare-on.com"

def get_ip_result(index, move):
  second = str(index)
  third = (enemy_pieces[move[3]] * 16) | (index & 0xf)
  fourth = (((ord(move[5][0]) - ord('a')) * 0x10) | ((ord(move[5][1]) - ord('0')-1) * 0x2)) | 0x00 # 0x80
  return "127." + second + "." + str(third) + "." + str(fourth)

for move in enumerate(moves):
  print(get_ip_result(move[0], move[1]) + "\t" + get_dns_query(move[1]))
