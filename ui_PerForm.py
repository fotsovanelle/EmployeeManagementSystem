# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PerForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(722, 420)
        self.Num_children = QSpinBox(Dialog)
        self.Num_children.setObjectName(u"Num_children")
        self.Num_children.setGeometry(QRect(400, 220, 71, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Num_children.setFont(font)
        self.MonthBonus = QTextEdit(Dialog)
        self.MonthBonus.setObjectName(u"MonthBonus")
        self.MonthBonus.setGeometry(QRect(180, 160, 191, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.MonthBonus.setFont(font1)
        self.label_28 = QLabel(Dialog)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(200, 220, 201, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_28.setFont(font2)
        self.label_29 = QLabel(Dialog)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 160, 151, 21))
        self.label_29.setFont(font2)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 71, 21))
        self.label_2.setFont(font2)
        self.label_27 = QLabel(Dialog)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 220, 101, 31))
        self.label_27.setFont(font2)
        self.Monthly_salary = QTextEdit(Dialog)
        self.Monthly_salary.setObjectName(u"Monthly_salary")
        self.Monthly_salary.setGeometry(QRect(550, 150, 141, 41))
        self.Monthly_salary.setFont(font1)
        self.label_26 = QLabel(Dialog)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(390, 160, 151, 21))
        self.label_26.setFont(font2)
        self.Marital_status = QCheckBox(Dialog)
        self.Marital_status.setObjectName(u"Marital_status")
        self.Marital_status.setGeometry(QRect(140, 220, 16, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Marital_status.sizePolicy().hasHeightForWidth())
        self.Marital_status.setSizePolicy(sizePolicy)
        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(410, 80, 151, 21))
        self.label_25.setFont(font2)
        self.DaysWorked = QSpinBox(Dialog)
        self.DaysWorked.setObjectName(u"DaysWorked")
        self.DaysWorked.setGeometry(QRect(570, 70, 71, 31))
        self.DaysWorked.setFont(font)
        self.Name = QTextEdit(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(110, 70, 251, 41))
        font3 = QFont()
        font3.setPointSize(14)
        self.Name.setFont(font3)
        self.HireEmployee = QPushButton(Dialog)
        self.HireEmployee.setObjectName(u"HireEmployee")
        self.HireEmployee.setGeometry(QRect(70, 330, 141, 41))
        self.UpdateEmployee = QPushButton(Dialog)
        self.UpdateEmployee.setObjectName(u"UpdateEmployee")
        self.UpdateEmployee.setGeometry(QRect(370, 330, 131, 41))
        self.label_30 = QLabel(Dialog)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(240, 10, 221, 31))
        self.label_30.setFont(font2)
        self.DismissEmployee = QPushButton(Dialog)
        self.DismissEmployee.setObjectName(u"DismissEmployee")
        self.DismissEmployee.setGeometry(QRect(220, 330, 141, 41))
        self.MuteEmployee = QPushButton(Dialog)
        self.MuteEmployee.setObjectName(u"MuteEmployee")
        self.MuteEmployee.setGeometry(QRect(510, 330, 141, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Number of children:", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Monthly Bonus:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Married:", None))
        self.Monthly_salary.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Monthly Salary:", None))
        self.Marital_status.setText("")
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Days Worked:", None))
        self.HireEmployee.setText(QCoreApplication.translate("Dialog", u"Hire Permanent Employee", None))
        self.UpdateEmployee.setText(QCoreApplication.translate("Dialog", u"Update Employee", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Permanent Employees", None))
        self.DismissEmployee.setText(QCoreApplication.translate("Dialog", u"Dismiss Employee", None))
        self.MuteEmployee.setText(QCoreApplication.translate("Dialog", u"Mute Employee", None))
    # retranslateUi

