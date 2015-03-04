# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserViewerUI.ui'
#
# Created: Tue Mar  3 02:35:22 2015
# by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog_main(object):
    def setupUi(self, Dialog_main):
        self.x = 360
        Dialog_main.setObjectName(_fromUtf8("Dialog_main"))
        Dialog_main.resize(1076+self.x, 656+self.x)
        self.graphicsView = QtGui.QGraphicsView(Dialog_main)
        self.graphicsView.setGeometry(QtCore.QRect(12, 24, 1068+self.x, 548+self.x))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton_threshold = QtGui.QPushButton(Dialog_main)
        self.pushButton_threshold.setGeometry(QtCore.QRect(372, 576+ self.x, 100, 32))
        self.pushButton_threshold.setObjectName(_fromUtf8("pushButton_threshold"))
        self.pushButton_frequency = QtGui.QPushButton(Dialog_main)
        self.pushButton_frequency.setGeometry(QtCore.QRect(372, 616+ self.x, 100, 32))
        self.pushButton_frequency.setObjectName(_fromUtf8("pushButton_frequency"))
        self.lineEdit_threshold = QtGui.QLineEdit(Dialog_main)
        self.lineEdit_threshold.setGeometry(QtCore.QRect(152, 580+ self.x, 144, 28))
        self.lineEdit_threshold.setObjectName(_fromUtf8("lineEdit_threshold"))
        self.lineEdit_frequency = QtGui.QLineEdit(Dialog_main)
        self.lineEdit_frequency.setGeometry(QtCore.QRect(152, 620+ self.x, 144, 28))
        self.lineEdit_frequency.setObjectName(_fromUtf8("lineEdit_frequency"))
        self.label = QtGui.QLabel(Dialog_main)
        self.label.setGeometry(QtCore.QRect(300, 580+ self.x, 68, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_main)
        self.label_2.setGeometry(QtCore.QRect(300, 624+ self.x, 68, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog_main)
        self.label_3.setGeometry(QtCore.QRect(60, 580+ self.x, 68, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog_main)
        self.label_4.setGeometry(QtCore.QRect(60, 620+ self.x, 68, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.graphicsView_screen = QtGui.QGraphicsView(Dialog_main)
        self.graphicsView_screen.setGeometry(QtCore.QRect(32, 24, 1048+ self.x, 528+ self.x))
        self.graphicsView_screen.setObjectName(_fromUtf8("graphicsView_screen"))

        self.retranslateUi(Dialog_main)
        QtCore.QMetaObject.connectSlotsByName(Dialog_main)

    def retranslateUi(self, Dialog_main):
        Dialog_main.setWindowTitle(_translate("Dialog_main", "Laser Viewer", None))
        self.pushButton_threshold.setText(_translate("Dialog_main", "set", None))
        self.pushButton_frequency.setText(_translate("Dialog_main", "set", None))
        self.lineEdit_threshold.setText(_translate("Dialog_main", "700", None))
        self.lineEdit_frequency.setText(_translate("Dialog_main", "500", None))
        self.label.setText(_translate("Dialog_main", "mm", None))
        self.label_2.setText(_translate("Dialog_main", "ms", None))
        self.label_3.setText(_translate("Dialog_main", "Threshold", None))
        self.label_4.setText(_translate("Dialog_main", "Frequency", None))

    def resize(self, px, py, x, y):
        pass

