from config import MorseCode_cyr, MorseCode_lat, MorseCode_reverse_cyr, MorseCode_reverse_lat
from config import Morse_Unacceptable_symbols
import re

from config import alphabet_ru, alphabet_eng

from config import uni_lat
# МОРЗЭ


class Morse:
    def __init__(self, code, leng):
        self.code = code
        self.leng = leng
        self.Unacceptable_symbol = []

    def decode(self):
        tmp = []
        code_list = self.code.split(' ')  # делим код посимвольно
        if self.leng == 'Английский':
            for elem in code_list:

                if re.match('^[\n·.− -]+$', elem):
                    if elem in MorseCode_reverse_lat:
                        tmp.append(MorseCode_reverse_lat[elem])  # записываем все значения в массив перебором
                    else:
                        return "Ошибка!\nСмените язык!"
                else:
                    return 'Ошибка!\nПроверьте Текст на наличие символов только "·", ".", "−", "-"'

            return ''.join(tmp)  # выводим массив
        elif self.leng == 'Русский':
            for elem in code_list:
                if re.match('^[\n·.− -]+$', elem):
                    if elem in MorseCode_reverse_cyr:
                        tmp.append(MorseCode_reverse_cyr[elem])  # записываем все значения в массив перебором
                    else:
                        return "Ошибка!\nСмените язык!"
                else:
                    return 'Ошибка!\nПроверьте Текст на наличие символов только "·", ".", "−", "-"'

            return ''.join(tmp)  # выводим массив

    def encode(self):
        total = []
        if self.leng == 'Английский':
            for i in range(len(self.code)):
                if self.code[i] in Morse_Unacceptable_symbols:
                    print(f'Недопустимый символ "{self.code[i]}"')
                    self.Unacceptable_symbol.append(self.code[i])
                    break
                else:
                    total.append(MorseCode_lat[self.code[i].upper()])  # Добавляем в список закодированые символы

            if len(self.Unacceptable_symbol) == 1:
                return 'Проверьте Текст на наличие символов "#", "$", "№", "%", "^", "&", "*", "|", "\\", "<", ">"'

            return " ".join(total)  # Возвращаем из функции соединённый список
        elif self.leng == 'Русский':
            for i in range(len(self.code)):
                if self.code[i] in Morse_Unacceptable_symbols:
                    print(f'Недопустимый символ "{self.code[i]}"')
                    self.Unacceptable_symbol.append(self.code[i])
                    break
                else:
                    total.append(MorseCode_cyr[self.code[i].upper()])  # Добавляем в список закодированые символы

            if len(self.Unacceptable_symbol) >= 1:
                return 'Проверьте Текст на наличие символов "#", "$", "№", "%", "^", "&", "*", "|", "\\", "<", ">"'

            return " ".join(total)  # Возвращаем из функции соединённый список


#Цезарь
class Cesar:
    def __init__(self, text, step):
        self.step = step
        self.text = text

    def encode(self):
        result = ''
        for item in self.text:
            if item.upper() in alphabet_ru:
                if item.isupper():
                    locate = alphabet_ru.find(item)
                    new_locate = locate + self.step
                    result += alphabet_ru[new_locate]
                else:
                    locate = alphabet_ru.find(item.upper())
                    new_locate = locate + self.step
                    result += alphabet_ru[new_locate].lower()
            elif item.upper() in alphabet_eng:
                if item.isupper():
                    locate = alphabet_eng.find(item)
                    new_locate = locate + self.step
                    result += alphabet_eng[new_locate]
                else:
                    locate = alphabet_eng.find(item.upper())
                    new_locate = locate + self.step
                    result += alphabet_eng[new_locate].lower()
            else:
                result += item
        return result

    def decode(self):
        result = ''
        for item in self.text:
            if item.upper() in alphabet_ru:
                if item.isupper():
                    locate = alphabet_ru.find(item)
                    new_locate = locate - self.step
                    result += alphabet_ru[new_locate]
                else:
                    locate = alphabet_ru.find(item.upper())
                    new_locate = locate - self.step
                    result += alphabet_ru[new_locate].lower()
            elif item.upper() in alphabet_eng:
                if item.isupper():
                    locate = alphabet_eng.find(item)
                    new_locate = locate - self.step
                    result += alphabet_eng[new_locate]
                else:
                    locate = alphabet_eng.find(item.upper())
                    new_locate = locate - self.step
                    result += alphabet_eng[new_locate].lower()
            else:
                result += item
        return result


# ВИЖЕНЕР
class Visener:
    def __init__(self, word, key):
        self.word = word
        self.key = key

    def encode(self):
        key_encoded = self.encode_val(self.key)
        value_encoded = self.encode_val(self.word)
        shifre = self.full_encode(value_encoded, key_encoded)
        return ''.join(self.decode_val(shifre))

    def decode(self):
        key_encoded = self.encode_val(self.key)
        value_encoded = self.encode_val(self.word)
        decoded = self.full_decode(value_encoded, key_encoded)
        decode_word_list = self.decode_val(decoded)
        return ''.join(decode_word_list)


    def encode_val(self, word):
        list_code = []
        lent = len(word)
        d = uni_lat

        for w in range(lent):
            for value in d:
                if word[w] == d[value]:
                   list_code.append(value)
        return list_code

    def comparator(self, value, key):
        len_key = len(key)
        dic = {}
        iter = 0
        full = 0

        for i in value:
            dic[full] = [i,key[iter]]
            full = full + 1
            iter = iter +1
            if (iter >= len_key):
                iter = 0
        return dic

    def full_encode(self, value, key):
        dic = self.comparator(value, key)
        lis = []
        d = uni_lat

        for v in dic:
            go = (dic[v][0]+dic[v][1]) % len(d)
            lis.append(go)
        return lis

    def decode_val(self, list_in):
        list_code = []
        lent = len(list_in)
        d = uni_lat

        for i in range(lent):
            for value in d:
                if list_in[i] == value:
                   list_code.append(d[value])
        return list_code

    def full_decode(self, value, key):
        dic = self.comparator(value, key)
        d = uni_lat
        lis =[]

        for v in dic:
            go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
            lis.append(go)
        return lis


# проверка функций
def test_Morse():

    test = Morse("Hello, world!:) \n"
                 "(-.,:;'/?!@)", "Английский")
    print(test.encode())
    code_lat = test.encode()
    test = Morse(code_lat, 'Английский')
    print(test.decode())

    print()

    test = Morse("Привет, мир!:) \n"
                 "(-.,:;'/?!)", 'Русский')
    print(test.encode())
    code_cyr = test.encode()
    test = Morse(code_cyr, "Русский")
    print(test.decode())


def test_Cesar():
    test = Cesar("Привет \nGleb", -79)
    print(test.encode())
    code = test.encode()
    # 92 -79
    print()

    test = Cesar(code, -79)
    print(test.decode())


def test_Visener():
    word = 'hello world'
    key = 'junly'
    test = Visener(word, key)
    print(test.encode())

    print()

    test = Visener('S[[Yim^_fO', key)
    print(test.decode())


# test_Visener()
# test_Morse()
# test_Cesar()
