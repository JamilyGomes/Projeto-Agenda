# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow,
    QRadioButton, QSizePolicy, QWidget)
import img

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 783)
        self.frame_principalForm = QFrame(Form)
        self.frame_principalForm.setObjectName(u"frame_principalForm")
        self.frame_principalForm.setGeometry(QRect(20, 10, 501, 761))
        self.frame_principalForm.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame_principalForm.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_principalForm.setFrameShadow(QFrame.Shadow.Raised)
        self.formulrio = QFrame(self.frame_principalForm)
        self.formulrio.setObjectName(u"formulrio")
        self.formulrio.setGeometry(QRect(150, 10, 191, 61))
        self.formulrio.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.formulrio.setFrameShape(QFrame.Shape.StyledPanel)
        self.formulrio.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.formulrio)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Formulrio = QLabel(self.formulrio)
        self.Formulrio.setObjectName(u"Formulrio")
        self.Formulrio.setStyleSheet(u"font: 700 italic 40pt \"Script\";\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: italic 24pt \"Segoe UI\";\n"
"")

        self.horizontalLayout.addWidget(self.Formulrio)

        self.frame_CPF = QFrame(self.frame_principalForm)
        self.frame_CPF.setObjectName(u"frame_CPF")
        self.frame_CPF.setGeometry(QRect(10, 150, 481, 64))
        self.frame_CPF.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_CPF.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_CPF.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_CPF)
        self.formLayout.setObjectName(u"formLayout")
        self.CPF = QLabel(self.frame_CPF)
        self.CPF.setObjectName(u"CPF")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.CPF)

        self.line_cpf = QLineEdit(self.frame_CPF)
        self.line_cpf.setObjectName(u"line_cpf")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.line_cpf)

        self.frame_Telefone = QFrame(self.frame_principalForm)
        self.frame_Telefone.setObjectName(u"frame_Telefone")
        self.frame_Telefone.setGeometry(QRect(10, 220, 481, 64))
        self.frame_Telefone.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_Telefone.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Telefone.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frame_Telefone)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.Tel = QLabel(self.frame_Telefone)
        self.Tel.setObjectName(u"Tel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Tel)

        self.line_tel = QLineEdit(self.frame_Telefone)
        self.line_tel.setObjectName(u"line_tel")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.line_tel)

        self.frame_Email = QFrame(self.frame_principalForm)
        self.frame_Email.setObjectName(u"frame_Email")
        self.frame_Email.setGeometry(QRect(10, 290, 481, 64))
        self.frame_Email.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_Email.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Email.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frame_Email)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.Email = QLabel(self.frame_Email)
        self.Email.setObjectName(u"Email")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.Email)

        self.line_Email = QLineEdit(self.frame_Email)
        self.line_Email.setObjectName(u"line_Email")

        self.formLayout_5.setWidget(1, QFormLayout.SpanningRole, self.line_Email)

        self.frame_6 = QFrame(self.frame_principalForm)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 360, 481, 64))
        self.frame_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_6 = QFormLayout(self.frame_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.End = QLabel(self.frame_6)
        self.End.setObjectName(u"End")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.End)

        self.line_End = QLineEdit(self.frame_6)
        self.line_End.setObjectName(u"line_End")

        self.formLayout_6.setWidget(1, QFormLayout.SpanningRole, self.line_End)

        self.pushButton = QPushButton(self.frame_principalForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 710, 75, 24))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 80, 236);")
        self.frame_Nome = QFrame(self.frame_principalForm)
        self.frame_Nome.setObjectName(u"frame_Nome")
        self.frame_Nome.setGeometry(QRect(10, 80, 481, 64))
        self.frame_Nome.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_Nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Nome.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_Nome)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.Nome = QLabel(self.frame_Nome)
        self.Nome.setObjectName(u"Nome")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Nome)

        self.line_nome = QLineEdit(self.frame_Nome)
        self.line_nome.setObjectName(u"line_nome")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.line_nome)

        self.frame_Sexo = QFrame(self.frame_principalForm)
        self.frame_Sexo.setObjectName(u"frame_Sexo")
        self.frame_Sexo.setGeometry(QRect(20, 550, 78, 114))
        self.frame_Sexo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_Sexo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Sexo.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frame_Sexo)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.Sexo = QLabel(self.frame_Sexo)
        self.Sexo.setObjectName(u"Sexo")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.Sexo)

        self.btn_Masc = QRadioButton(self.frame_Sexo)
        self.btn_Masc.setObjectName(u"btn_Masc")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.btn_Masc)

        self.btn_Femin = QRadioButton(self.frame_Sexo)
        self.btn_Femin.setObjectName(u"btn_Femin")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.btn_Femin)

        self.btn_outros = QRadioButton(self.frame_Sexo)
        self.btn_outros.setObjectName(u"btn_outros")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.btn_outros)

        self.label = QLabel(self.frame_principalForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 10, 501, 751))
        self.label.setPixmap(QPixmap(u":/icon/img.jpg"))
        self.label.setScaledContents(True)
        self.Data_nasc = QLabel(self.frame_principalForm)
        self.Data_nasc.setObjectName(u"Data_nasc")
        self.Data_nasc.setGeometry(QRect(20, 470, 121, 16))
        self.Data_nasc.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.dateEdit = QDateEdit(self.frame_principalForm)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 490, 181, 22))
        self.label.raise_()
        self.formulrio.raise_()
        self.frame_CPF.raise_()
        self.frame_Telefone.raise_()
        self.frame_Email.raise_()
        self.frame_6.raise_()
        self.pushButton.raise_()
        self.frame_Nome.raise_()
        self.frame_Sexo.raise_()
        self.Data_nasc.raise_()
        self.dateEdit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Formulrio.setText(QCoreApplication.translate("Form", u"Formul\u00e1rio", None))
        self.CPF.setText(QCoreApplication.translate("Form", u"CPF", None))
        self.Tel.setText(QCoreApplication.translate("Form", u"Tel", None))
        self.Email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.End.setText(QCoreApplication.translate("Form", u"End", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ENVIAR", None))
        self.Nome.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.Sexo.setText(QCoreApplication.translate("Form", u"Sexo", None))
        self.btn_Masc.setText(QCoreApplication.translate("Form", u"Masc", None))
        self.btn_Femin.setText(QCoreApplication.translate("Form", u"Femin", None))
        self.btn_outros.setText(QCoreApplication.translate("Form", u"outros", None))
        self.label.setText("")
        self.Data_nasc.setText(QCoreApplication.translate("Form", u"Data de Nascimento", None))
    # retranslateUi

import Form, sys
from Form import Ui_Form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)  
    MainWindow.show()       
    sys.exit(app.exec())