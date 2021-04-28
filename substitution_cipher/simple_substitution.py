import string

class simple_substitution:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    # 암호문 변환
    def process(self):
        alphabet = list(string.ascii_lowercase)
        print(alphabet)
        self.key_list = []
        # 키 중복 제거
        for ch in list(self.key):
            if not ch in self.key_list:
                self.key_list.append(ch)

        start_idx = alphabet.index(self.key_list[-1])
        # 암호판
        for i in range(0 + start_idx, 26 + start_idx):
            if not alphabet[i%26] in self.key_list:
                self.key_list.append(alphabet[i%26])

        result = []
        # 암호판에 맞게 암호문 구하기
        for w in self.text:
            try:
                result.append(self.key_list[alphabet.index(w)])
            except(ValueError):
                result.append(' ')
        print(''.join(result))
        return ''.join(result) # 암호문 반환


    # 복호문 반환
    def process2(self, ciphertext):
        alphabet = list(string.ascii_lowercase)
        decryption = []
        for w in ciphertext:
            try:
                decryption.append(alphabet[(self.key_list.index(w))])
            except(ValueError):
                decryption.append(' ')
        return ''.join(decryption)


if __name__ == '__main__':
    s = simple_substitution('assassinator', 'i love you')
    s.process2(s.process())

