from utils import permutate, XOR, stringToBinary, binaryToHex, hexToBinary, binaryToString, inversePermutate
from KeyExpansion import KeyExpansion
from FeistelModified import FeistelModified

class DESModified:
  def __init__(self):
    self.ip = [
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25,
    ]
    
    self.permutate_box = [
      16, 7, 20, 21, 29, 12, 28, 17,
      1, 15, 23, 26, 5, 8, 31, 10,
      2, 8, 24, 14, 32, 27, 3, 9,
      19, 13, 30, 6, 22, 11, 4, 25,
      40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29
    ]
    
    self.ip_inverse = [
      40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7
    ]

    self.f = FeistelModified()

  def encrypt(self, plaintext, key):
    plaintext = stringToBinary(plaintext)
    # list_binary = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    # print(list_binary, "pt")
    permutate_result = permutate(plaintext, self.ip)
    
    half_block_length = int(len(permutate_result) / 2)
    block_l = permutate_result[0:half_block_length]
    block_r = permutate_result[half_block_length:]

    for i in range(16):
      feistel = self.f.encrypt(block_r, key[i], 4)
      permutated_feistel = permutate(feistel, self.permutate_box)

      # temp is used for swapping
      temp = block_l
      block_l = block_r
      block_r = XOR(temp, permutated_feistel)
    
    # last permutation to get the result
    # print(str(block_l) + str(block_r), "ngeng")
    final_result = permutate((str(block_l) + str(block_r)), self.ip_inverse)
    # print(final_result)
    return binaryToHex(final_result)

  def decrypt(self, ciphertext, key):
    ciphertext = hexToBinary(ciphertext)
    # print(ciphertext)
    permutate_result = inversePermutate(ciphertext, self.ip_inverse)
    # print(permutate_result, "ngeng")
    
    half_block_length = int(len(permutate_result) / 2)
    block_l = permutate_result[0:half_block_length]
    block_r = permutate_result[half_block_length:]

    for i in range(16):
      feistel = self.f.encrypt(block_l, key[i], 8)
      permutated_feistel = inversePermutate(feistel, self.permutate_box)
      
      # temp is used for swapping
      temp = block_r
      block_r = block_l
      block_l = XOR(temp, permutated_feistel)
      # f.block_r = XOR(temp, permutated_feistel)
    
    # last permutation to get the result
    # final_result = inversePermutate((str(block_l) + str(block_r)), self.ip)

    # list_binary = [final_result[i:i+8] for i in range(0, len(final_result), 8)]
    # print(list_binary)
    # text = ""
    # for bin in list_binary:
    #   text += binaryToString(bin)

    # return text
    return 0
    # block_a = [permutate_result[i:i+6] for i in range(0, len(permutate_result), 6)]
    # print(final_result)
    # return binaryToString(final_result)

d = DESModified()
key = KeyExpansion("abcdefghijklmnop").internalKeys
print(d.encrypt("123456ABCD132536", key))
print()
print(d.decrypt("3F79FCFF5B19504603CB77EE854AFF6B", key))