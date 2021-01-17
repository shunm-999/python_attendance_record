from datetime import datetime


class UserInputData:
    def __init__(self, username: str, attendance_time: datetime, leave_time: datetime, break_time: datetime):
        self.__username = username
        self.__attendance_time = attendance_time
        self.__leave_time = leave_time
        self.__break_time = break_time

    def get_username(self):
        return self.__username

    username = property(get_username)

    def get_attendance_time(self):
        return self.__attendance_time

    attendance_time = property(get_attendance_time)

    def get_leave_time(self):
        return self.__leave_time

    leave_time = property(get_leave_time)

    def get_break_time(self):
        return self.__break_time

    break_time = property(get_break_time)
