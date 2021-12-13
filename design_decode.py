# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import enscryptions
from PyQt5.QtWidgets import QMessageBox
import re


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
            result = enscryptions.Cesar(self.Input_De_text.toPlainText(), self.steps.value())
            self.Output_De_text.setText(result.decode())

        elif self.Morse_De.isChecked():
            if self.leng_eng.isChecked():
                cyr_let = self.has_cyr(self.Input_De_text.toPlainText())
                if not cyr_let:
                    result = enscryptions.Morse(self.Input_De_text.toPlainText(), self.leng_eng.text())
                    self.Output_De_text.setText(result.decode())
                else:
                    self.msg_wrong_leng()
            elif self.leng_rus.isChecked():
                lat_let = self.has_lat(self.Input_De_text.toPlainText())
                if not lat_let:
                    result = enscryptions.Morse(self.Input_De_text.toPlainText(), self.leng_rus.text())
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
                        result = enscryptions.Visener(self.Input_De_text.toPlainText(), self.Key.text())
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decode = QtWidgets.QMainWindow()
    ui = Ui_Decode()
    ui.setupUi(Decode)
    Decode.show()
    sys.exit(app.exec_())
