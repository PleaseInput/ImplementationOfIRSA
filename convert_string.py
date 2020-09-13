BASE64_TABLE = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]


def get_base64_string_from(binString):
    if isinstance(binString, str) and set(binString).issubset({'0', '1'}):
        numberOfPaddedZero = len(binString) % 6
        binString = '{0:06b}'.format(numberOfPaddedZero) + binString + (numberOfPaddedZero * '0')

        base64String = ''
        for i in range(0, len(binString), 6):
            index = int(binString[i:i+6], 2)
            base64String += BASE64_TABLE[index]

        return base64String

def getBinStringFrom(base64String):
    if isinstance(base64String, str) and set(base64String).issubset(set(BASE64_TABLE)):
        binString = ''
        for char in base64String:
            index = BASE64_TABLE.index(char)
            binString += '{0:06b}'.format(index)

        numberOfPaddedZero = int(binString[0:6], 2)
        binString = binString[6:] if numberOfPaddedZero==0 else binString[6:(-1)*numberOfPaddedZero]

        return binString

if __name__ == "__main__":
    testString = '000001'
    afStr = get_base64_string_from(testString)
    print(afStr)
    bfStr = getBinStringFrom(afStr)
    print(bfStr)
