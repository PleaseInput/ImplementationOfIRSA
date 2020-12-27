from Crypto.Cipher import AES


class AESCrypto:
    """
    AES mode is always .CBC currently.
    """

    def __init__(self, key, iv):
        self.key = key.encode()
        self.iv = iv.encode()
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)

        text = self.add_padding(text)
        # if not isinstance(text, (bytes, bytearray, memoryview)):
        #     text = text.encode()

        text = text.encode()
        return cryptor.encrypt(text)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        text = cryptor.decrypt(text)
        text = text.decode()
        return self.remove_padding(text)

    @staticmethod
    def add_padding(text):
        num_of_need_to_pad = (16 - len(text) % 16)
        if num_of_need_to_pad == 0:
            text += '0' * 16
        elif num_of_need_to_pad <= 9:
            text += '0' * (num_of_need_to_pad - 1) + str(num_of_need_to_pad)
        elif num_of_need_to_pad > 9:
            text += '0' * (num_of_need_to_pad - 2) + str(num_of_need_to_pad)
        else:
            assert False
        return text

    @staticmethod
    def remove_padding(text):
        num_of_need_to_pad = int(text[-2:])
        if num_of_need_to_pad == 0:
            return text[:-16]
        else:
            return text[:-num_of_need_to_pad]


def main():
    test = AESCrypto(key='keys' * 4, iv='keys' * 4)
    t0 = test.encrypt('hello' * 4)
    print(t0)
    t1 = test.decrypt(t0)
    print(t1)


if __name__ == '__main__':
    main()
