# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TemForm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(669, 314)
        self.Name = QTextEdit(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(90, 90, 161, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.Name.setFont(font)
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 170, 151, 21))
        self.label_16.setFont(font)
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(320, 90, 121, 31))
        self.label_15.setFont(font)
        self.HourlyPay = QTextEdit(Dialog)
        self.HourlyPay.setObjectName(u"HourlyPay")
        self.HourlyPay.setGeometry(QRect(450, 80, 161, 41))
        self.HourlyPay.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 71, 21))
        self.label_2.setFont(font)
        self.Hours_worked = QSpinBox(Dialog)
        self.Hours_worked.setObjectName(u"Hours_worked")
        self.Hours_worked.setGeometry(QRect(170, 170, 71, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Hours_worked.setFont(font1)
        self.HireEmployee = QPushButton(Dialog)
        self.HireEmployee.setObjectName(u"HireEmployee")
        self.HireEmployee.setGeometry(QRect(30, 240, 161, 41))
        self.UpdateEmployee = QPushButton(Dialog)
        self.UpdateEmployee.setObjectName(u"UpdateEmployee")
        self.UpdateEmployee.setGeometry(QRect(350, 240, 141, 41))
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(200, 10, 251, 31))
        self.label_17.setFont(font)
        self.MuteEmployee = QPushButton(Dialog)
        self.MuteEmployee.setObjectName(u"MuteEmployee")
        self.MuteEmployee.setGeometry(QRect(500, 240, 141, 41))
        self.DismissEmployee = QPushButton(Dialog)
        self.DismissEmployee.setObjectName(u"DismissEmployee")
        self.DismissEmployee.setGeometry(QRect(200, 240, 141, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Hours Worked:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"hourly pay:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.HireEmployee.setText(QCoreApplication.translate("Dialog", u"Hire Employee", None))
        self.UpdateEmployee.setText(QCoreApplication.translate("Dialog", u"Update Employee", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Temporal Employee Form", None))
        self.MuteEmployee.setText(QCoreApplication.translate("Dialog", u"Mute Employee", None))
        self.DismissEmployee.setText(QCoreApplication.translate("Dialog", u"Dismiss Employee", None))
    # retranslateUi

