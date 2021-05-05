import string
class multiple_substitution:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def process(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q/z', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']


        key_list = []
        # 키 중복 제거
        for ch in list(self.key):
            if ch == 'q' or ch == 'z':
                ch = 'q/z'
            if not ch in key_list:
                key_list.append(ch)


        # 암호판
        for i in range(0, 25):
            if not alphabet[i] in key_list:
                key_list.append(alphabet[i])

        key_list1 = [['']*5 for i in range(5)]

        # 1차원 배열에서 2차원 배열 암호판 만들기
        for i in range(5):
            for j in range(5):
                key_list1[i][j] = key_list[5*i+j]

        # text 공백 제거 / 연속된 글자 뒤에 X 넣기
        text = []
        for i in self.text:
            if not i == ' ':
                text.append(i)

        word_list = []
        word = []
        text1 = [text[0]]
        flag = 1

        for i in range(1, len(text)):
            if text[i-1] != text[i]:
                text1.append(text[i])
            elif text[i-1] == text[i] and i % 2 == flag:
                text1.append('x')
                text1.append(text[i])
                flag = (1 + flag) % 2
            else:
                text1.append(text[i])


        if len(text1) % 2 == 1 :
            flag2 = 1
        else:
            flag2 = 0

        for i in range(0, int(len(text1)/2)*2 + flag2, 2):
            word.append(text1[i])
            try:
                word.append(text1[i+1])
            except(IndexError):
                word.append('x')
            word_list.append(word)
            word = []

        return key_list1, word_list

    def pro(self, word_list, key_list):
        word_index = []
        print(word_list)

        for chs in word_list:
            word = []

            # key_list에서 word를 찾아서 인덱스 배열 생성
            for ch in range(2):
                for i in range(len(key_list)):
                    for j in range(len(key_list[i])):
                        if key_list[i][j] == chs[ch]:
                            if ch == 0:
                                word.append([i, j])
                            if ch == 1:
                                word.append([i, j])
                                word_index.append(word)
        result = []

        for i in word_index:
            # 행이 같을 때
            if i[0][0] == i[1][0]:
                result.append(key_list[(i[0][0])][(i[0][1] + 1) % 5])
                result.append(key_list[(i[0][0])][(i[1][1] + 1) % 5])

            # 열이 같을 때
            elif i[0][1] == i[1][1]:
                result.append(key_list[(i[0][0] + 1) % 5][(i[0][1])])
                result.append(key_list[(i[1][0] +1) % 5][(i[1][1])])

            else :
                result.append(key_list[i[1][0]][i[0][1]])
                result.append(key_list[i[0][0]][i[1][1]])

        return (''.join(result))

    # 복호화
    def decryption(self, ciphertext, key_list):
        result = []
        word_list=[]
        word_index = []


        for i in range(0, len(ciphertext), 2):
            word = []
            word.append(ciphertext[i])
            word.append(ciphertext[i+1])
            word_list.append(word)

        for chs in word_list:
            word = []

            # key_list에서 word를 찾아서 인덱스 배열 생성
            for ch in range(2):
                for i in range(len(key_list)):
                    for j in range(len(key_list[i])):
                        if key_list[i][j] == chs[ch]:
                            if ch == 0:
                                word.append([i, j])
                            if ch == 1:
                                word.append([i, j])
                                word_index.append(word)

        for i in word_index:
            # 행이 같을 때
            if i[0][0] == i[1][0]:
                result.append(key_list[(i[0][0])][(i[0][1] - 1)])
                result.append(key_list[(i[0][0])][(i[1][1] - 1)])

            # 열이 같을 때
            elif i[0][1] == i[1][1]:
                result.append(key_list[(i[0][0] - 1)][(i[0][1])])
                result.append(key_list[(i[1][0] - 1)][(i[1][1])])

            else :
                result.append(key_list[i[1][0]][i[0][1]])
                result.append(key_list[i[0][0]][i[1][1]])
        answer = list(result[0])

        for i in range(1, len(result)):
            if result[i] == 'x':
                try:
                    if result[i-1] == result[i+1]:
                        continue
                except(IndexError):
                    continue
            else:
                answer.append(result[i])

        print(answer)
        return ''.join(answer)




            # ciphertext를 두개씩 배열로 나누고 키 리스트와 비교해서 원래의 배열을 찾는다.
            # 만약 x를 제거했을때 두 알파벳이 중복된다면 x를 제거한다.





if __name__ == '__main__':
    #TODO q/z 예외 적용 시켜 주기
    #TODO 맵핑 화면 / 테이블 구현
    m = multiple_substitution('assassinator', 'be careful for assassinator')
    key_list, word_list = m.process()
    cryptogram = m.pro(word_list, key_list)
    m.decryption(cryptogram, key_list)