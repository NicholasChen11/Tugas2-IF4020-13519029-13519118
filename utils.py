def stringToBinary(string):
  hex = ''
  for c in string:
    hex += format(ord(c), '08b')

  return hex

def permutate(string, permutationMatrix):
  result = ''

  for i in range(len(permutationMatrix)):
    # there is -1 because index in permutation matrix start from 1, not 0.
    result += string[permutationMatrix[i] - 1]

  return result

def XOR(stringA, stringB):
  result = ''

  for i in range(len(stringA)):
    if stringA[i] == stringB[i]:
      result += '0'
    else:
      result += '1'
  # result = [chr(ord(a) ^ ord(b)) for a,b in zip(stringA, stringB)]

  return result

def leftShift(array, totalShift):
  firstPart = array[:totalShift]
  secondPart = array[totalShift:]

  return ''.join(secondPart + firstPart)