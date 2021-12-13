# python -m PyQt5.uic.pyuic -x [].ui -o [].py
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox

from design_encode import Ui_Encode
from design_decode import Ui_Decode

Form, Window = uic.loadUiType("design.ui")


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