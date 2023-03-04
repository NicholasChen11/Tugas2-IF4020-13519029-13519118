def stringToBinary(string):
  hex = ''
  for c in string:
    hex += format(ord(c), '08b')

  return hex

def binaryToString(bin):
  return chr(int(bin, 2))

def permutate(string, permutationMatrix):
  result = ''
  for i in range(len(permutationMatrix)):
    # there is -1 because index in permutation matrix start from 1, not 0.
    result += string[permutationMatrix[i] - 1]

  return result

def inversePermutate(string, permutationMatrix):
  result = [''] * len(string)

  for i in range(len(permutationMatrix)):
    # there is -1 because index in permutation matrix start from 1, not 0.
    result[permutationMatrix[i] - 1] = string[i]

  return ''.join(result)

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

def binaryToNumber(binary):
  return int(str(binary), 2)

def numberToBinary(num):
  return f'{num:08b}'

def hexToBinary(hex):
  map = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
  }

  bin = ""
  for i in range(len(hex)):
    bin = bin + map[hex[i]]

  return bin

def binaryToHex(bin):
  map = {
    "0000": '0',
    "0001": '1',
    "0010": '2',
    "0011": '3',
    "0100": '4',
    "0101": '5',
    "0110": '6',
    "0111": '7',
    "1000": '8',
    "1001": '9',
    "1010": 'A',
    "1011": 'B',
    "1100": 'C',
    "1101": 'D',
    "1110": 'E',
    "1111": 'F'
  }
  
  hex = ""
  for i in range(0, len(bin), 4):
    ch = ""
    ch = ch + bin[i]
    ch = ch + bin[i + 1]
    ch = ch + bin[i + 2]
    ch = ch + bin[i + 3]
    hex = hex + map[ch]

  return hex