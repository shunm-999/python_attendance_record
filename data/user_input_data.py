from datetime import datetime, timedelta


class UserInputData:
    def __init__(self, username: str,
                 sheet_date: datetime,
                 attendance_time: datetime,
                 leave_time: datetime,
                 break_time: datetime):
        """
        :param username: ユーザー名
        :param sheet_date: 勤務表の日付
        :param attendance_time: 就業開始時刻
        :param leave_time: 就業終了時刻
        :param break_time: 休憩時間
        :param attendance_classfication: 勤怠区分
        """
        self.__username = username
        self.__sheet_date = sheet_date
        self.__attendance_time = attendance_time
        self.__leave_time = leave_time
        self.__break_time = break_time

    def get_username(self) -> str:
        return self.__username

    username = property(get_username)

    def get_sheet_date(self) -> datetime:
        return self.__sheet_date

    sheet_date = property(get_sheet_date)

    def get_attendance_time(self) -> datetime:
        return self.__attendance_time

    attendance_time = property(get_attendance_time)

    def get_leave_time(self) -> datetime:
        return self.__leave_time

    leave_time = property(get_leave_time)

    def get_break_time(self) -> datetime:
        return self.__break_time

    break_time = property(get_break_time)
