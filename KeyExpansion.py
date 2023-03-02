class KeyExpansion:
  def __init__(self, externalKey):
    self.externalKey = externalKey
    self.totalTurn = 16
    self.permutedCompressionMatrix = {
      1: [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
      ],
      2: [
        14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
      ],
    }
    self.shiftPerTurn = {
      1: 1,
      2: 1,
      3: 2,
      4: 2,
      5: 2,
      6: 2,
      7: 2,
      8: 2,
      9: 1,
      10: 2,
      11: 2,
      12: 2,
      13: 2,
      14: 2,
      15: 2,
      16: 1,
    }
    self.internalKeys = self.expandExternalKey()
    print(self.internalKeys)
    print(len(self.internalKeys))
    print(len(self.internalKeys[0]))

  def permutate(self, array, permutedCompressionMatrixNumber):
    matrix = self.permutedCompressionMatrix[permutedCompressionMatrixNumber]
    matrixLen = len(matrix)
    result = []

    for i in range(matrixLen):
      # there is -1 because index in matrix start from 1, not 0.
      result.append(array[matrix[i] - 1])

    C = result[:matrixLen//2]
    D = result[matrixLen//2:]

    return C, D

  def leftShift(self, array, currentTurnNumber):
    totalShift = self.shiftPerTurn[currentTurnNumber]
    
    firstPart = array[:totalShift]
    secondPart = array[totalShift:]

    return secondPart + firstPart

  def expandExternalKey(self):
    C, D = self.permutate(self.externalKey, 1)
    internalKeys = []

    for currentTurnNumber in range(1, self.totalTurn + 1):
      C = self.leftShift(C, currentTurnNumber)
      D = self.leftShift(D, currentTurnNumber)

      firstHalfKey, secondHalfKey = self.permutate(C + D, 2)
      internalKeys.append(firstHalfKey + secondHalfKey)
    
    return internalKeys

externalKey = 'abcdefghijklmnopqrstuvwxyz123456789abcdefghijklmnopqrstuvwxyz123'
keyExpansion = KeyExpansion(externalKey)