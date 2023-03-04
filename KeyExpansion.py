from utils import stringToBinary, permutate, XOR, leftShift

class KeyExpansion:
  def __init__(self, externalKey):
    self.externalKey = stringToBinary(externalKey)
    self.totalTurn = 16
    self.permutedMatrix = {
      1: [
        118, 45, 25, 72, 102, 22, 18, 46, 76, 33, 98, 88, 34, 96, 2,
        35, 106, 24, 50, 56, 63, 121, 51, 103, 53, 57, 58, 37, 64, 90,
        128, 89, 61, 105, 26, 95, 28, 62, 107, 123, 32, 92, 100, 113, 111,
        68, 114, 42, 6, 23, 49, 9, 48, 11, 80, 78, 16, 116, 66, 85,
        39, 93, 77, 59, 120, 86, 5, 30, 17, 19, 119, 36, 47, 15, 99,
        12, 10, 38, 29, 69, 14, 108, 7, 54, 73, 81, 71, 109, 126, 21,
        8, 79, 112, 3, 117, 104, 1, 20, 55, 84, 97, 31, 125, 127, 52,
        82, 41, 4, 91, 13, 87, 94, 75, 40, 65, 101, 110, 124, 43, 67,
        70, 44, 27, 115, 60, 122, 74, 83
      ],
      2: [
        77, 74, 102, 45, 16, 118, 29, 99, 32, 53, 17, 65, 57, 75, 64,
        6, 103, 50, 49, 94, 8, 2, 13, 40, 24, 106, 10, 76, 31, 63, 
        35, 1, 96, 114, 62, 78, 14, 61, 104, 124, 95, 30, 100, 46, 56,
        39, 97, 70, 82, 93, 47, 18, 15, 66, 122, 126, 123, 125, 34, 27,
        23, 25, 105, 79, 73, 101, 88, 67, 60, 52, 59, 127, 109, 7, 110,
        121, 4, 87, 72, 90, 54, 12, 108, 115, 98, 43, 36, 113, 85, 20,
        68, 44, 112, 38, 21, 69, 26, 33, 117, 19, 91, 111, 84, 41, 120,
        128, 116, 28, 11, 51, 37, 92, 5, 83, 80, 81, 86, 119, 55, 42,
        48, 107, 3, 22, 71, 89, 9, 58
      ],
    }
    self.internalKeys = self.expandExternalKey()

  def expandExternalKey(self):
    internalKeys = []

    # First Permutation
    firstPermutation = permutate(self.externalKey, self.permutedMatrix[1])
    A, B, C, D = firstPermutation[:32], firstPermutation[32:64], firstPermutation[64:96], firstPermutation[96:128]

    for currentTurnNumber in range(1, self.totalTurn + 1):
      # XOR Operations 
      A = XOR(A, B)
      B = XOR(B, C)
      C = XOR(C, D)
      D = XOR(D, A)

      # Left Shift Operations
      multiplier = currentTurnNumber % 2
      A = leftShift(A, 1 * multiplier)
      B = leftShift(B, 2 * multiplier)
      C = leftShift(C, 3 * multiplier)
      D = leftShift(D, 4 * multiplier)

      # Second Permutation
      internalKey = permutate(A + B + C + D, self.permutedMatrix[2])

      # XOR firstHalf and secondHalf
      firstHalf = internalKey[:64]
      secondHalf = internalKey[64:]
      internalKey = XOR(''.join(firstHalf), ''.join(secondHalf))

      # Add new internal key to array
      internalKeys.append(internalKey)

      # Left Shift Batch Operation
      temp = A
      A = B
      B = C
      C = D
      D = temp
    
    return internalKeys
  
  def __str__(self):
    print("internalKeys:")
    print(self.internalKeys)
    print("total internalKey: ")
    print(len(self.internalKeys))
    print("one internalKey length:")
    print(len(self.internalKeys[0]))

externalKeyTest = 'abcdefghijklmnop'
keyExpansion = KeyExpansion(externalKeyTest)