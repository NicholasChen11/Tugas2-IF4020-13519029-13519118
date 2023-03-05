from utils import permutate, XOR, stringToBinary, binaryToHex, hexToBinary, binaryToString
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
    ]

    self.f = FeistelModified()

  def encrypt(self, plaintext, key):
    plaintext = stringToBinary(plaintext)
    
    half_block_length = int(len(plaintext) / 2)
    left_block = plaintext[:half_block_length]
    right_block = plaintext[half_block_length:]
    
    permutate_result = permutate(left_block, self.ip) + permutate(right_block, self.ip_inverse)
    
    block_l = permutate_result[:half_block_length]
    block_r = permutate_result[half_block_length:]

    for i in range(16):
      feistel = self.f.encrypt(block_r, key[i], 4)
      permutated_feistel = permutate(feistel, self.permutate_box)

      # temp is used for swapping
      temp = block_l
      block_l = block_r
      block_r = XOR(temp, permutated_feistel)

    # last permutation to get the result
    final_result = permutate(block_l, self.ip_inverse) + permutate(block_r, self.ip)

    return binaryToHex(final_result)

  def decrypt(self, ciphertext, key):
    ciphertext = hexToBinary(ciphertext)

    half_block_length = int(len(ciphertext) / 2)
    left_block = ciphertext[:half_block_length]
    right_block = ciphertext[half_block_length:]

    permutate_result = permutate(left_block, self.ip) + permutate(right_block, self.ip_inverse)
    
    block_l = permutate_result[:half_block_length]
    block_r = permutate_result[half_block_length:]

    for i in range(16):
      feistel = self.f.encrypt(block_l, key[i], 4)
      permutated_feistel = permutate(feistel, self.permutate_box)
      
      # temp is used for swapping
      temp = block_r
      block_r = block_l
      block_l = XOR(temp, permutated_feistel)
    
    # last permutation to get the result
    final_result = permutate(block_l, self.ip_inverse) + permutate(block_r, self.ip)
    return binaryToString(final_result)

d = DESModified()
key = KeyExpansion("abcdefghijklmnop").internalKeys
e = d.encrypt("123456ABCD132536", key)
print(e)
print()
print(d.decrypt(e, key[::-1]))