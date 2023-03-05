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

  def initialPermutate(self, text):
    half_block_length = int(len(text) / 2)
    left_block = text[:half_block_length]
    right_block = text[half_block_length:]

    # permutation is done for both left and right because the size needs to be 128 bits
    permutate_result = permutate(left_block, self.ip) + permutate(right_block, self.ip_inverse)

    left_permutate = permutate_result[:half_block_length]
    right_permutate = permutate_result[half_block_length:]

    return left_permutate, right_permutate

  def feistelFunction(self, L, R, key):
    for i in range(16):
      feistel = self.f.encrypt(R, key[i])
      permutated_feistel = permutate(feistel, self.permutate_box)

      # temp is used for swapping
      temp = L
      L = R
      R = XOR(temp, permutated_feistel)

    return L, R

  def lastPermutate(self, L, R):
    # done for both left and right because the size needs to be 128 bits also
    return permutate(L, self.ip_inverse) + permutate(R, self.ip)

  def encrypt(self, plaintext, key):
    plaintext = stringToBinary(plaintext)
    block_l, block_r = self.initialPermutate(plaintext)

    block_l, block_r = self.feistelFunction(block_l, block_r, key)
    
    # last permutation to get the result
    final_result = self.lastPermutate(block_l, block_r)
    return binaryToHex(final_result)

  def decrypt(self, ciphertext, key):
    ciphertext = hexToBinary(ciphertext)
    block_l, block_r = self.initialPermutate(ciphertext)
    
    # block_l and block_r is reversed because decrypt is done from bottom to top
    block_r, block_l = self.feistelFunction(block_r, block_l, key)
    
    # last permutation to get the result
    final_result = self.lastPermutate(block_l, block_r)
    return binaryToString(final_result)

d = DESModified()
key = KeyExpansion("abcdefghijklmnop").internalKeys
e = d.encrypt("123456ABCD132536", key)
print(e)
print()
print(d.decrypt(e, key[::-1]))