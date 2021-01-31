# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendance_record.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AttendanceRecordDialog(object):
    def setupUi(self, AttendanceRecordDialog):
        if not AttendanceRecordDialog.objectName():
            AttendanceRecordDialog.setObjectName(u"AttendanceRecordDialog")
        AttendanceRecordDialog.resize(1002, 522)
        self.layoutWidget2 = QWidget(AttendanceRecordDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 40, 881, 364))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonSelectSaveDirectory = QPushButton(self.layoutWidget2)
        self.ButtonSelectSaveDirectory.setObjectName(u"ButtonSelectSaveDirectory")
        self.ButtonSelectSaveDirectory.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonSelectSaveDirectory.sizePolicy().hasHeightForWidth())
        self.ButtonSelectSaveDirectory.setSizePolicy(sizePolicy)
        self.ButtonSelectSaveDirectory.setMinimumSize(QSize(30, 30))
        self.ButtonSelectSaveDirectory.setMaximumSize(QSize(200, 50))
        self.ButtonSelectSaveDirectory.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.ButtonSelectSaveDirectory)

        self.LabelSaveDirectory = QLabel(self.layoutWidget2)
        self.LabelSaveDirectory.setObjectName(u"LabelSaveDirectory")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelSaveDirectory.sizePolicy().hasHeightForWidth())
        self.LabelSaveDirectory.setSizePolicy(sizePolicy1)
        self.LabelSaveDirectory.setMaximumSize(QSize(1000, 50))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LabelSaveDirectory)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LabelUserName = QLabel(self.layoutWidget2)
        self.LabelUserName.setObjectName(u"LabelUserName")
        self.LabelUserName.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_3.addWidget(self.LabelUserName)

        self.LineEditUserName = QLineEdit(self.layoutWidget2)
        self.LineEditUserName.setObjectName(u"LineEditUserName")

        self.horizontalLayout_3.addWidget(self.LineEditUserName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LabelAttendanceTime = QLabel(self.layoutWidget2)
        self.LabelAttendanceTime.setObjectName(u"LabelAttendanceTime")
        self.LabelAttendanceTime.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_4.addWidget(self.LabelAttendanceTime)

        self.TimeEditAttendanceTime = QTimeEdit(self.layoutWidget2)
        self.TimeEditAttendanceTime.setObjectName(u"TimeEditAttendanceTime")

        self.horizontalLayout_4.addWidget(self.TimeEditAttendanceTime)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LabelLeaveTime = QLabel(self.layoutWidget2)
        self.LabelLeaveTime.setObjectName(u"LabelLeaveTime")
        self.LabelLeaveTime.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_5.addWidget(self.LabelLeaveTime)

        self.TimeEditLeaveTime = QTimeEdit(self.layoutWidget2)
        self.TimeEditLeaveTime.setObjectName(u"TimeEditLeaveTime")

        self.horizontalLayout_5.addWidget(self.TimeEditLeaveTime)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LabelBreakTime = QLabel(self.layoutWidget2)
        self.LabelBreakTime.setObjectName(u"LabelBreakTime")
        self.LabelBreakTime.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_6.addWidget(self.LabelBreakTime)

        self.TimeEditBreakTime = QTimeEdit(self.layoutWidget2)
        self.TimeEditBreakTime.setObjectName(u"TimeEditBreakTime")

        self.horizontalLayout_6.addWidget(self.TimeEditBreakTime)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DateEditStartDate = QDateEdit(self.layoutWidget2)
        self.DateEditStartDate.setObjectName(u"DateEditStartDate")
        self.DateEditStartDate.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.DateEditStartDate)

        self.LabelInside = QLabel(self.layoutWidget2)
        self.LabelInside.setObjectName(u"LabelInside")
        self.LabelInside.setMaximumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.LabelInside)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DateEditEndDate = QDateEdit(self.layoutWidget2)
        self.DateEditEndDate.setObjectName(u"DateEditEndDate")
        self.DateEditEndDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.DateEditEndDate)

        self.LabelOutSide = QLabel(self.layoutWidget2)
        self.LabelOutSide.setObjectName(u"LabelOutSide")
        self.LabelOutSide.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_2.addWidget(self.LabelOutSide)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.LavelErrorMessage = QLabel(self.layoutWidget2)
        self.LavelErrorMessage.setObjectName(u"LavelErrorMessage")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LavelErrorMessage.setFont(font)
        self.LavelErrorMessage.setStyleSheet(u"QLabel { color : red; }")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.LavelErrorMessage)

        self.layoutWidget = QWidget(AttendanceRecordDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(720, 430, 195, 30))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ButtonAccept = QPushButton(self.layoutWidget)
        self.ButtonAccept.setObjectName(u"ButtonAccept")

        self.horizontalLayout_7.addWidget(self.ButtonAccept)

        self.ButtonCancel = QPushButton(self.layoutWidget)
        self.ButtonCancel.setObjectName(u"ButtonCancel")

        self.horizontalLayout_7.addWidget(self.ButtonCancel)


        self.retranslateUi(AttendanceRecordDialog)

        QMetaObject.connectSlotsByName(AttendanceRecordDialog)
    # setupUi

    def retranslateUi(self, AttendanceRecordDialog):
        AttendanceRecordDialog.setWindowTitle(QCoreApplication.translate("AttendanceRecordDialog", u"Dialog", None))
        self.ButtonSelectSaveDirectory.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u4fdd\u5b58\u5148\u30c7\u30a3\u30ec\u30af\u30c8\u30ea\u3092\u9078\u629e", None))
        self.LabelSaveDirectory.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u30c7\u30a3\u30ec\u30af\u30c8\u30ea\u304c\u9078\u629e\u3055\u308c\u3066\u3044\u307e\u305b\u3093", None))
        self.LabelUserName.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u304a\u540d\u524d", None))
        self.LineEditUserName.setText("")
        self.LineEditUserName.setPlaceholderText(QCoreApplication.translate("AttendanceRecordDialog", u"\u7a7a\u6b04\u3067\u3082\u53ef", None))
        self.LabelAttendanceTime.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u51fa\u52e4\u6642\u523b", None))
        self.LabelLeaveTime.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u9000\u52e4\u6642\u523b", None))
        self.LabelBreakTime.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u4f11\u61a9\u6642\u9593", None))
        self.DateEditStartDate.setDisplayFormat(QCoreApplication.translate("AttendanceRecordDialog", u"yyyy/MM", None))
        self.LabelInside.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u304b\u3089", None))
        self.DateEditEndDate.setDisplayFormat(QCoreApplication.translate("AttendanceRecordDialog", u"yyyy/MM", None))
        self.LabelOutSide.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u307e\u3067\u306e\u52e4\u52d9\u8868\u3092\u4f5c\u6210\u3059\u308b", None))
        self.LavelErrorMessage.setText("")
        self.ButtonAccept.setText(QCoreApplication.translate("AttendanceRecordDialog", u"OK", None))
        self.ButtonCancel.setText(QCoreApplication.translate("AttendanceRecordDialog", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
    # retranslateUi

