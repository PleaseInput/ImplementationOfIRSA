from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_crypto:
    """
    AES mode is always .CBC currently.
    """

    def __init__(self, key, iv):
        try:
            self.key = key.encode()
            self.iv = iv.encode()
        except:
            print('initialization failed')
            return
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)

        text = self.add_padding(text)
        # if not isinstance(text, (bytes, bytearray, memoryview)):
        #     text = text.encode()
        try:
            text = text.encode()
        except:
            print('text type error')
            return
        return cryptor.encrypt(text)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        try:
            text = cryptor.decrypt(text)
            text = text.decode()
            return self.remove_padding(text)
        except:
            print('decrypt failed')
            return
        
    def add_padding(self, text):
        try:
            num_of_need_to_pad = (16 - len(text) % 16)
            if num_of_need_to_pad == 0:
                text += '0' * 16
            elif num_of_need_to_pad <= 9:
                text += '0' * (num_of_need_to_pad - 1) + str(num_of_need_to_pad)
            elif num_of_need_to_pad > 9:
                text += '0' * (num_of_need_to_pad - 2) + str(num_of_need_to_pad)
            else:
                assert(False)
            return text
        except:
            print('Only support string at present.')

    def remove_padding(self, text):
        try:
            num_of_need_to_pad = int(text[-2:])
            if num_of_need_to_pad == 0:
                return text[:-16]
            else:
                return text[:-num_of_need_to_pad]
        except:
            print('remove padding fail')

test = AES_crypto(key = 'keys' * 4, iv = 'keys' * 4)
t0 = test.encrypt('hello' * 4)
print(t0)
t1 = test.decrypt(t0)
print(t1)