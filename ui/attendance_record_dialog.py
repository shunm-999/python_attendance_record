import datetime
import pathlib

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QFile, QDate
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog

from controller.create_attendance_record_controller import CreateAttendanceRecordController, TemplateType


class AttendanceRecordDialog(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.to_save_directory = None

        # ui ファイルを開く
        file = QFile('ui/attendance_record.ui')
        file.open(QFile.ReadOnly)

        # ローダを使って ui ファイルをロードする
        loader = QUiLoader()
        self.ui = loader.load(file)
        self.setCentralWidget(self.ui)

        # 初期のフォーカスを、ディレクトリ選択ボタンに設定
        self.ui.ButtonSelectSaveDirectory.setFocus()
        self.ui.ButtonSelectSaveDirectory.clicked.connect(self.click_browse_directory_button)

        # OKボタン押下時の、設定
        self.ui.ButtonAccept.clicked.connect(self.click_positive_button)
        self.ui.ButtonCancel.clicked.connect(self.close_window)

        # 開始 / 終了日の初期値
        now = datetime.datetime.now()
        now = QDate(now.year, now.month, 1)
        self.ui.DateEditStartDate.setDate(now)
        self.ui.DateEditEndDate.setDate(now)

    def click_browse_directory_button(self):
        self.to_save_directory = QFileDialog.getExistingDirectory(None, '保存先のディレクトリ選択', str(pathlib.Path.home()))
        self.ui.LabelSaveDirectory.setText(self.to_save_directory)

    def click_positive_button(self):

        to_save_directory = self.to_save_directory
        user_name = self.ui.LineEditUserName.text()
        attendance_time = self.ui.TimeEditAttendanceTime.time()
        leave_time = self.ui.TimeEditLeaveTime.time()
        break_time = self.ui.TimeEditBreakTime.time()
        start_date = self.ui.DateEditStartDate.date()
        end_date = self.ui.DateEditEndDate.date()

        attendance_time = datetime.datetime(year=2020, month=1, day=1,
                                            hour=attendance_time.hour(),
                                            minute=attendance_time.minute())
        leave_time = datetime.datetime(year=2020, month=1, day=1,
                                       hour=leave_time.hour(),
                                       minute=leave_time.minute())
        break_time = datetime.datetime(year=2020, month=1, day=1,
                                       hour=break_time.hour(),
                                       minute=break_time.minute())

        start_date = datetime.datetime(year=start_date.year(), month=start_date.month(), day=start_date.day())
        end_date = datetime.datetime(year=end_date.year(), month=end_date.month(), day=end_date.day())

        if not self.validate(to_save_directory=to_save_directory,
                             attendance_time=attendance_time, leave_time=leave_time, break_time=break_time,
                             start_date=start_date, end_date=end_date):
            self.ui.LavelErrorMessage.setText('入力内容に誤りがあります')
            return

        controller = CreateAttendanceRecordController([TemplateType.Template1])
        controller.handle(parent_dir=to_save_directory,
                          user_name=user_name,
                          attendance_time=attendance_time,
                          leave_time=leave_time,
                          break_time=break_time,
                          start_date=start_date,
                          end_date=end_date)

        self.close_window()

    def close_window(self):
        self.window().close()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        super().closeEvent(event)

    def validate(self,
                 to_save_directory: str,
                 attendance_time: datetime,
                 leave_time: datetime,
                 break_time: datetime,
                 start_date: datetime,
                 end_date: datetime) -> bool:

        # 保存先のディレクトリ
        if not to_save_directory:
            return False

        # 出勤時刻
        if attendance_time.hour == 0:
            return False

        # 退勤時刻
        if leave_time.hour == 0:
            return False

        # 休憩時間
        if break_time.hour == 0 and break_time.minute == 0:
            return False

        if attendance_time > leave_time:
            return False

        if (leave_time - attendance_time) < datetime.timedelta(hours=break_time.hour, minutes=break_time.minute):
            return False

        if start_date > end_date:
            return False

        return True
