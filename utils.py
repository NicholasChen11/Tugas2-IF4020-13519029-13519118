def permutate(array, permutationMatrix):
    result = []

    for i in range(len(permutationMatrix)):
      # there is -1 because index in permutation matrix start from 1, not 0.
      result.append(array[permutationMatrix[i] - 1])

    return result

def XOR(stringA, stringB):
  result = [chr(ord(a) ^ ord(b)) for a,b in zip(stringA, stringB)]

  return result

def leftShift(array, totalShift):
  firstPart = array[:totalShift]
  secondPart = array[totalShift:]

  return secondPart + firstPart