import string

class simple_substitution:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def process(self):
        alphabet = list(string.ascii_lowercase)
        print(alphabet)
        key_list = []
        # 키 중복 제거
        for ch in list(self.key):
            if not ch in key_list:
                key_list.append(ch)

        start_idx = alphabet.index(key_list[-1])
        # 암호판
        for i in range(0 + start_idx, 26 + start_idx):
            if not alphabet[i%26] in key_list:
                key_list.append(alphabet[i%26])

        result = []
        # 암호판에 맞게 암호문 구하기
        for w in self.text:
            try:
                result.append(key_list[alphabet.index(w)])
            except(ValueError):
                result.append(' ')

        return ''.join(result) # 암호문 반환

if __name__ == '__main__':
    s = simple_substitution('assassinator', 'i love you')
    s.process()

