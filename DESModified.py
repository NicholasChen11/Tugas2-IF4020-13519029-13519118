from utils import permutate, XOR, stringToBinary, binaryToString, binaryToHex, hexToBinary
from KeyExpansion import KeyExpansion
from FeistelModified import FeistelModified

class DESModified:
  def __init__(self, key_text, plaintext):
    self.key = KeyExpansion(key_text).internalKeys
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
    self.plaintext = stringToBinary(plaintext)

  def encrypt(self):
    permutate_result = permutate(self.plaintext, self.ip)
    
    half_block_length = int(len(permutate_result) / 2)
    block_l = permutate_result[0:half_block_length]
    block_r = permutate_result[half_block_length:]

    f = FeistelModified(block_l, block_r, self.key[0])

    for _ in range(16):
      feistel = f.encrypt()
      permutated_feistel = permutate(feistel, self.permutate_box)
      temp = f.block_l
      f.block_l = block_r
      f.block_r = XOR(temp, permutated_feistel)
    
    # last permutation to get the result
    final_result = permutate((str(f.block_l) + str(f.block_r)), self.ip_inverse)
    return binaryToHex(final_result)

d = DESModified("abcdefghijklmnop", "123456ABCD132536")