# python -m PyQt5.uic.pyuic -x [].ui -o [].py
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import re


# МОРЗЕ АЛФАВИТЫ

MorseCode_lat = \
    {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '·−−−−', '2': '··−−−',
        '3': '···−−', '4': '····−', '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·',
        '0': '−−−−−', '.': '......', ',': '.-.-.-', ':': '---...', ';': '-.-.-.', '(': '-.--.',
        ')': '-.--.-', '`': '.----.', '"': '.-..-.', "'": '.-..-.', '-': '-....-', '/': '-..-.',
        '_': '..--.-', '?': '..--..', '!': '-.-.--', '+': '.-.-.', ' ': '-...-', '@': '.--.-.', '\n': "\n",
        '{': '-.--.', '[': '-.--.', ']': '-.--.-', '}': '-.--.-'
    }  # словарь с ключами - обычными символами(латинница)

MorseCode_reverse_lat =\
    {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '·−−−−': '1', '··−−−': '2', '···−−': '3', '····−': '4', '·····': '5',
        '−····': '6', '−−···': '7', '−−−··': '8', '−−−−·': '9', '−−−−−': '0', '......': '.', '---...': ':',
        '.-.-.-': ',', '-.-.-.': ';', '-.--.': '(', '-.--.-': ')', '.----.': '`', '.-..-.': "'",
        '-....-': '-', '-..-.': '/', '..--.-': '', '..--..': '?', '-.-.--': '!', '.-.-.': '+',
        '-...-': ' ', '.--.-.': '@', '\n': "\n"
    }  # словарь с ключами - зашифроваными символами(латинница)

MorseCode_cyr = \
    {
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-',
        'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.',
        'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.',
        'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', '1': '·−−−−', '2': '··−−−',
        '3': '···−−', '4': '····−', '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·',
        '0': '−−−−−', '.': '.-.-.-', ',': '--.--', ':': '---...', ';': '-.-.-.', '(': '-.--.',
        ')': '-.--.-', '`': '.----.', '"': '.-..-.', "'": '.-..-.', '-': '-....-', '/': '-..-.',
        '_': '..--.-', '?': '..--..', '!': '-.-.--', '+': '.-.-.', ' ': '-...-', '@': '.--.-.',
        'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '...-...', 'Ю': '..--', 'Я': '.-.-', '\n': "\n", 'Ё': '.',
        '{': '-.--.', '[': '-.--.', ']': '-.--.-', '}': '-.--.-'
    }  # словарь с ключами - обычными символами(кириллица)

MorseCode_reverse_cyr = \
    {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж',
        '--..': 'З', '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н',
        '---': 'О', '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф',
        '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш', '--.-': 'Щ', '·−−−−': '1', '··−−−': '2',
        '···−−': '3', '····−': '4', '·····': '5', '−····': '6', '−−···': '7', '−−−··': '8', '−−−−·': '9',
        '−−−−−': '0', '.-.-.-': '.', '--.--': ',', '---...': ':', '-.-.-.': ';', '-.--.': '(',
        '-.--.-': ')', '.----.': '`', ".-..-.": "'", '-....-': '-', '-..-.': '/',
        '..--.-': '_', '..--..': '?', '-.-.--': '!', '.-.-.': '+', '-...-': ' ',
        '.--.-.': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '...-...': 'Э', '..--': 'Ю', '.-.-': 'Я', '\n': "\n", '@': '.--.-.'
    }  # словарь с ключами - зашифроваными символами(кириллица)

Morse_Unacceptable_symbols = ["#", '$', '№', "%", "^", "&", "*", "|", '\\', "<", ">"]


# Алфавиты
alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
              'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# Алфавиты с индексами по Unicode

uni_lat = {
    0: '\x00', 1: '\x01', 2: '\x02', 3: '\x03', 4: '\x04', 5: '\x05', 6: '\x06', 7: '\x07', 8: '\x08', 9: '\t',
    10: '\n', 11: '\x0b', 12: '\x0c', 13: '\r', 14: '\x0e', 15: '\x0f', 16: '\x10', 17: '\x11', 18: '\x12',
    19: '\x13', 20: '\x14', 21: '\x15', 22: '\x16', 23: '\x17', 24: '\x18', 25: '\x19', 26: '\x1a',
    27: '\x1b', 28: '\x1c', 29: '\x1d', 30: '\x1e', 31: '\x1f', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$',
    37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/',
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':',
    59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E',
    70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P',
    81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[',
    92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f',
    103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q',
    114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{',
    124: '|', 125: '}', 126: '~'}  # латинница с индексами по Unicode

uni_cyr = {
    1040: 'А', 1041: 'Б', 1042: 'В', 1043: 'Г', 1044: 'Д', 1045: 'Е', 1046: 'Ж', 1047: 'З', 1048: 'И',
    1049: 'Й', 1050: 'К', 1051: 'Л', 1052: 'М', 1053: 'Н', 1054: 'О', 1055: 'П', 1056: 'Р', 1057: 'С',
    1058: 'Т', 1059: 'У', 1060: 'Ф', 1061: 'Х', 1062: 'Ц', 1063: 'Ч', 1064: 'Ш', 1065: 'Щ', 1066: 'Ъ',
    1067: 'Ы', 1068: 'Ь', 1069: 'Э', 1070: 'Ю', 1071: 'Я', 1072: 'а', 1073: 'б', 1074: 'в', 1075: 'г',
    1076: 'д', 1077: 'е', 1078: 'ж', 1079: 'з', 1080: 'и', 1081: 'й', 1082: 'к', 1083: 'л', 1084: 'м',
    1085: 'н', 1086: 'о', 1087: 'п', 1088: 'р', 1089: 'с', 1090: 'т', 1091: 'у', 1092: 'ф', 1093: 'х',
    1094: 'ц', 1095: 'ч', 1096: 'ш', 1097: 'щ', 1098: 'ъ', 1099: 'ы', 1100: 'ь', 1101: 'э', 1102: 'ю',
    1103: 'я'}  # кириллица с индексами по Unicode


# from config import MorseCode_cyr, MorseCode_lat, MorseCode_reverse_cyr, MorseCode_reverse_lat
# from config import Morse_Unacceptable_symbols

# from config import alphabet_ru, alphabet_eng

# from config import uni_lat
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


#Form, Window = uic.loadUiType("design.ui")


class Ui_Decode(object):

    def setupUi(self, Decode):
        Decode.setObjectName("Decode")
        Decode.resize(787, 543)
        Decode.setStyleSheet("background-color: rgb(19, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(Decode)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 470, 401, 71))
        self.frame_2.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Morse_De = QtWidgets.QRadioButton(self.frame_2)
        self.Morse_De.setGeometry(QtCore.QRect(40, 10, 61, 17))
        self.Morse_De.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.Morse_De.setObjectName("Morse_De")
        self.Cesar_De = QtWidgets.QRadioButton(self.frame_2)
        self.Cesar_De.setGeometry(QtCore.QRect(110, 10, 111, 17))
        self.Cesar_De.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.Cesar_De.setObjectName("Cesar_De")
        self.Visener_De = QtWidgets.QRadioButton(self.frame_2)
        self.Visener_De.setGeometry(QtCore.QRect(230, 10, 111, 17))
        self.Visener_De.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                      "color: whitesmoke")
        self.Visener_De.setObjectName("Visener_De")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 731, 401))
        self.frame.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Input_De_text = QtWidgets.QTextEdit(self.frame)
        self.Input_De_text.setGeometry(QtCore.QRect(10, 60, 311, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Input_De_text.setFont(font)
        self.Input_De_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Input_De_text.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                         "color: whitesmoke;\n"
                                         "font: 12pt ;")
        self.Input_De_text.setPlaceholderText("")
        self.Input_De_text.setObjectName("Input_De_text")
        self.Output_De_text = QtWidgets.QTextBrowser(self.frame)
        self.Output_De_text.setGeometry(QtCore.QRect(410, 60, 311, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Output_De_text.setFont(font)
        self.Output_De_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Output_De_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Output_De_text.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                          "color: whitesmoke")
        self.Output_De_text.setObjectName("Output_De_text")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.label_6.setStyleSheet("font: 15pt \"Segoe UI\" bold;\n"
                                   "background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(416, 20, 291, 31))
        self.label_7.setStyleSheet("font: 15pt \"Segoe UI\" bold;\n"
                                   "background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.morph = QtWidgets.QPushButton(self.frame)
        self.morph.setGeometry(QtCore.QRect(334, 200, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.morph.setFont(font)
        self.morph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.morph.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.morph.setObjectName("morph")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(400, 480, 401, 71))
        self.frame_3.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.leng_rus = QtWidgets.QRadioButton(self.frame_3)
        self.leng_rus.setGeometry(QtCore.QRect(190, 0, 82, 17))
        self.leng_rus.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.leng_rus.setObjectName("leng_rus")
        self.leng_eng = QtWidgets.QRadioButton(self.frame_3)
        self.leng_eng.setGeometry(QtCore.QRect(190, 20, 82, 17))
        self.leng_eng.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.leng_eng.setObjectName("leng_eng")
        self.steps = QtWidgets.QSpinBox(self.frame_3)
        self.steps.setGeometry(QtCore.QRect(90, 0, 42, 21))
        self.steps.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.steps.setMinimum(-79)
        self.steps.setMaximum(92)
        self.steps.setObjectName("steps")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(46, 0, 41, 21))
        self.label_5.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Key = QtWidgets.QLineEdit(self.frame_3)
        self.Key.setGeometry(QtCore.QRect(90, 30, 61, 20))
        self.Key.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                               "color: whitesmoke\n"
                               "")
        self.Key.setObjectName("Key")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(46, 30, 41, 21))
        self.label_2.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 10, 241, 61))
        self.label.setStyleSheet("font: 25pt \"Segoe UI\" bold;\n"
                                 "background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Decode.setCentralWidget(self.centralwidget)

        self.retranslateUi(Decode)
        QtCore.QMetaObject.connectSlotsByName(Decode)

    def retranslateUi(self, Decode):
        _translate = QtCore.QCoreApplication.translate
        Decode.setWindowTitle(_translate("Decode", "Decode"))
        self.Morse_De.setText(_translate("Decode", "Морзе"))
        self.Cesar_De.setText(_translate("Decode", "Алфавит Цезаря"))
        self.Visener_De.setText(_translate("Decode", "Шифр Виженера"))
        self.Input_De_text.setHtml(_translate("Decode",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("Decode", "Введите шифр"))
        self.label_7.setText(_translate("Decode", "Текст"))
        self.morph.setText(_translate("Decode", "=>"))
        self.leng_rus.setText(_translate("Decode", "Русский"))
        self.leng_eng.setText(_translate("Decode", "Английский"))
        self.label_5.setText(_translate("Decode", "Шаг"))
        self.label_2.setText(_translate("Decode", "Ключ"))
        self.label.setText(_translate("Decode", "Дешифровка"))

        self.morph.clicked.connect(self.morph_functional)

    def msg_wrong_leng(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        if not self.leng_rus.isChecked() and not self.leng_eng.isChecked():
            msg.setText("Язык не выбран")
        elif self.Visener_De.isChecked() and self.leng_rus.isChecked():
            msg.setText('Для шифра виженера доступен только "Английский" язык')
        else:
            msg.setText("Язык не соответсвует выбранному")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def msg_wrong_key(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def has_cyr(self, text):
            return bool(re.search('[а-яА-Я]', text))

    def has_lat(self, text):
            return bool(re.search('[a-zA-Z]', text))

    def morph_functional(self):

        if self.Cesar_De.isChecked():
            result = Cesar(self.Input_De_text.toPlainText(), self.steps.value())
            self.Output_De_text.setText(result.decode())

        elif self.Morse_De.isChecked():
            if self.leng_eng.isChecked():
                cyr_let = self.has_cyr(self.Input_De_text.toPlainText())
                if not cyr_let:
                    result = Morse(self.Input_De_text.toPlainText(), self.leng_eng.text())
                    self.Output_De_text.setText(result.decode())
                else:
                    self.msg_wrong_leng()
            elif self.leng_rus.isChecked():
                lat_let = self.has_lat(self.Input_De_text.toPlainText())
                if not lat_let:
                    result = Morse(self.Input_De_text.toPlainText(), self.leng_rus.text())
                    self.Output_De_text.setText(result.decode())
                else:
                    self.msg_wrong_leng()
            else:
                self.msg_wrong_leng()

        elif self.Visener_De.isChecked():
            if self.leng_eng.isChecked():
                cyr_let = self.has_cyr(self.Input_De_text.toPlainText())
                if not cyr_let:
                    if len(self.Key.text()) == 0:
                        self.msg_wrong_key("Введите ключ!")
                    elif len(self.Key.text()) == 1:
                        self.msg_wrong_key("Ключ должен состовлять минимум 2 символа")
                    elif self.has_cyr(self.Key.text()):
                        self.msg_wrong_key('Для ключа не поддерживается "Русский" язык')
                    else:
                        result = Visener(self.Input_De_text.toPlainText(), self.Key.text())
                        self.Output_De_text.setText(result.decode())

                else:
                    self.msg_wrong_leng()

            elif self.leng_rus.isChecked():
                self.msg_wrong_leng()
            else:
                self.msg_wrong_leng()


        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Метод не выбран")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()


class Ui_Encode(object):

    def setupUi(self, Encode):
        Encode.setObjectName("Encode")
        Encode.resize(787, 542)
        Encode.setStyleSheet("background-color: rgb(19, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(Encode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 10, 211, 61))
        self.label.setStyleSheet("font: 25pt \"Segoe UI\" bold;\n"
                                 "background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 470, 401, 71))
        self.frame_2.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Morse_En = QtWidgets.QRadioButton(self.frame_2)
        self.Morse_En.setGeometry(QtCore.QRect(40, 10, 61, 17))
        self.Morse_En.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.Morse_En.setObjectName("Morse_En")
        self.Cesar_En = QtWidgets.QRadioButton(self.frame_2)
        self.Cesar_En.setGeometry(QtCore.QRect(110, 10, 111, 17))
        self.Cesar_En.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.Cesar_En.setObjectName("Cesar_En")
        self.Visener_En = QtWidgets.QRadioButton(self.frame_2)
        self.Visener_En.setGeometry(QtCore.QRect(230, 10, 111, 17))
        self.Visener_En.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                      "color: whitesmoke")
        self.Visener_En.setObjectName("Visener_En")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 731, 401))
        self.frame.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Input_En_text = QtWidgets.QTextEdit(self.frame)
        self.Input_En_text.setGeometry(QtCore.QRect(10, 60, 311, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Input_En_text.setFont(font)
        self.Input_En_text.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                         "color: whitesmoke;\n"
                                         "font: 12pt ;")
        self.Input_En_text.setPlaceholderText("")
        self.Input_En_text.setObjectName("Input_En_text")
        self.Output_En_text = QtWidgets.QTextBrowser(self.frame)
        self.Output_En_text.setGeometry(QtCore.QRect(410, 60, 311, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Output_En_text.setFont(font)
        self.Output_En_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Output_En_text.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                          "color: whitesmoke")
        self.Output_En_text.setObjectName("Output_En_text")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.label_6.setStyleSheet("font: 15pt \"Segoe UI\" bold;\n"
                                   "background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(416, 20, 291, 31))
        self.label_7.setStyleSheet("font: 15pt \"Segoe UI\" bold;\n"
                                   "background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.morph = QtWidgets.QPushButton(self.frame)
        self.morph.setGeometry(QtCore.QRect(334, 200, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.morph.setFont(font)
        self.morph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.morph.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.morph.setObjectName("morph")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(390, 480, 401, 71))
        self.frame_3.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.leng_rus = QtWidgets.QRadioButton(self.frame_3)
        self.leng_rus.setGeometry(QtCore.QRect(190, 0, 82, 17))
        self.leng_rus.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.leng_rus.setObjectName("leng_rus")
        self.leng_eng = QtWidgets.QRadioButton(self.frame_3)
        self.leng_eng.setGeometry(QtCore.QRect(190, 20, 82, 17))
        self.leng_eng.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                    "color: whitesmoke")
        self.leng_eng.setObjectName("leng_eng")
        self.steps = QtWidgets.QSpinBox(self.frame_3)
        self.steps.setGeometry(QtCore.QRect(90, 0, 42, 21))
        self.steps.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.steps.setMinimum(-79)
        self.steps.setMaximum(92)
        self.steps.setObjectName("steps")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(46, 0, 41, 21))
        self.label_5.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Key = QtWidgets.QLineEdit(self.frame_3)
        self.Key.setGeometry(QtCore.QRect(90, 30, 61, 20))
        self.Key.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                               "color: whitesmoke\n"
                               "")
        self.Key.setObjectName("Key")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(46, 30, 41, 21))
        self.label_2.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                   "color: whitesmoke\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        Encode.setCentralWidget(self.centralwidget)

        self.retranslateUi(Encode)
        QtCore.QMetaObject.connectSlotsByName(Encode)

    def retranslateUi(self, Encode):
        _translate = QtCore.QCoreApplication.translate
        Encode.setWindowTitle(_translate("Encode", "Encode"))
        self.label.setText(_translate("Encode", "Шифровка"))
        self.Morse_En.setText(_translate("Encode", "Морзе"))
        self.Cesar_En.setText(_translate("Encode", "Алфавит Цезаря"))
        self.Visener_En.setText(_translate("Encode", "Шифр Виженера"))
        self.Input_En_text.setHtml(_translate("Encode",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("Encode", "Введите текст"))
        self.label_7.setText(_translate("Encode", "Шифр"))
        self.morph.setText(_translate("Encode", "=>"))
        self.leng_rus.setText(_translate("Encode", "Русский"))
        self.leng_eng.setText(_translate("Encode", "Английский"))
        self.label_5.setText(_translate("Encode", "Шаг"))
        self.label_2.setText(_translate("Encode", "Ключ"))

        self.morph.clicked.connect(self.morph_functional)

    def msg_wrong_leng(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        if not self.leng_rus.isChecked() and not self.leng_eng.isChecked():
            msg.setText("Язык не выбран")
        else:
            msg.setText("Язык не соответсвует выбранному")
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()

    def msg_wrong_key(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def has_cyr(self, text):
        return bool(re.search('[а-яА-Я]', text))

    def has_lat(self, text):
        return bool(re.search('[a-zA-Z]', text))

    def morph_functional(self):

        if self.Cesar_En.isChecked():
            result = Cesar(self.Input_En_text.toPlainText(), self.steps.value())
            self.Output_En_text.setText(result.encode())

        elif self.Morse_En.isChecked():

            if self.leng_eng.isChecked():
                cyr_let = self.has_cyr(self.Input_En_text.toPlainText())
                if not cyr_let:
                    result = Morse(self.Input_En_text.toPlainText(), self.leng_eng.text())
                    self.Output_En_text.setText(result.encode())
                else:
                    self.msg_wrong_leng()

            elif self.leng_rus.isChecked():
                lat_let = self.has_lat(self.Input_En_text.toPlainText())
                if not lat_let:
                    result = Morse(self.Input_En_text.toPlainText(), self.leng_rus.text())
                    self.Output_En_text.setText(result.encode())
                else:
                    self.msg_wrong_leng()

            else:
                self.msg_wrong_leng()

        elif self.Visener_En.isChecked():

            if self.leng_eng.isChecked():
                cyr_let = self.has_cyr(self.Input_En_text.toPlainText())
                if not cyr_let:

                    if len(self.Key.text()) == 0:
                        self.msg_wrong_key("Введите ключ!")

                    elif len(self.Key.text()) == 1:
                        self.msg_wrong_key("Ключ должен состовлять минимум 2 символа")

                    elif self.has_cyr(self.Key.text()):
                        self.msg_wrong_key('Для ключа не поддерживается "Русский" язык')

                    else:
                        result = Visener(self.Input_En_text.toPlainText(), self.Key.text())
                        self.Output_En_text.setText(result.encode())

                else:
                    self.msg_wrong_leng()

            elif self.leng_rus.isChecked():
                self.msg_wrong_leng()

            else:
                self.msg_wrong_leng()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Метод не выбран")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()


class Ui_Encoder(object):
    def openEncode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Encode()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDecode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Decode()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, encoder):
        encoder.setObjectName("encoder")
        encoder.resize(401, 380)
        encoder.setStyleSheet("background-color: rgb(19, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(encoder)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 400, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI 12")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 25pt \"Segoe UI\" bold;\n"
                                 "background-color: rgb(59, 56, 56);\n"
                                 "color: whitesmoke\n"
                                 "")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(20)
        self.label.setMidLineWidth(10)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 190, 261, 261))
        self.frame.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                 "border-radius: 15px 0 0 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.encode = QtWidgets.QPushButton(self.frame)
        self.encode.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encode.setFont(font)
        self.encode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encode.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                  "color: whitesmoke")
        self.encode.setObjectName("encode")
        self.Decode = QtWidgets.QPushButton(self.frame)
        self.Decode.setGeometry(QtCore.QRect(20, 90, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Decode.setFont(font)
        self.Decode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Decode.setStyleSheet("background-color: rgb(59, 56, 56);\n"
                                  "color: whitesmoke")
        self.Decode.setObjectName("Decode")

        encoder.setCentralWidget(self.centralwidget)
        self.retranslateUi(encoder)
        QtCore.QMetaObject.connectSlotsByName(encoder)

    def retranslateUi(self, encoder):
        _translate = QtCore.QCoreApplication.translate
        encoder.setWindowTitle(_translate("encoder", "encoder"))
        self.label.setText(_translate("encoder", "Encoder"))
        self.encode.setText(_translate("encoder", "Шифровка"))
        self.Decode.setText(_translate("encoder", "Дешифровка"))

        self.encode.clicked.connect(self.openEncode)

        self.Decode.clicked.connect(self.openDecode)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    encoder = QtWidgets.QMainWindow()
    ui = Ui_Encoder()
    ui.setupUi(encoder)
    encoder.show()
    sys.exit(app.exec_())