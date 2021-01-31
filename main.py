import sys

from PySide2 import QtWidgets

from ui.attendance_record_dialog import AttendanceRecordDialog

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = AttendanceRecordDialog()
    dialog.resize(1000, 500)
    dialog.show()
    sys.exit(app.exec_())
