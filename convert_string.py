BASE64_TABLE = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]


def get_base64_string_from(binary_string):
    if isinstance(binary_string, str) and set(binary_string).issubset({'0', '1'}):
        num_of_padded_zero = len(binary_string) % 6
        binary_string = '{0:06b}'.format(num_of_padded_zero) + binary_string + (num_of_padded_zero * '0')

        base64_string = ''
        for i in range(0, len(binary_string), 6):
            index = int(binary_string[i:i + 6], 2)
            base64_string += BASE64_TABLE[index]

        return base64_string


def get_bin_string_from(base64_string):
    if isinstance(base64_string, str) and set(base64_string).issubset(set(BASE64_TABLE)):
        bin_string = ''
        for char in base64_string:
            index = BASE64_TABLE.index(char)
            bin_string += '{0:06b}'.format(index)

        num_of_padded_zero = int(bin_string[0:6], 2)
        bin_string = bin_string[6:] if num_of_padded_zero == 0 else bin_string[6:(-1)*num_of_padded_zero]

        return bin_string


def main():
    test_string = '000001'
    base64_string = get_base64_string_from(test_string)
    print(base64_string)
    binary_string = get_bin_string_from(base64_string)
    print(binary_string)


if __name__ == "__main__":
    main()
