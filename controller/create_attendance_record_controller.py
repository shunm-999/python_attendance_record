import enum
import pathlib
from datetime import datetime
from typing import List

from data.user_input_data import UserInputData
from repository.excel_repository import ExcelRepository
from usecase.create_attendance_sheet_template1_interactor import CreateAttendanceSheetTemplate1Interactor
from usecase.create_attendance_sheet_usecase import CreateAttendanceSheetUseCase
from util.date_util import DateUtil
from util.file_util import FileUtil


class TemplateType(enum.Enum):
    Template1 = 'template1'


class CreateAttendanceRecordController:

    def __init__(self, template_list: List[TemplateType]):
        self.template_list = template_list

    def handle(self,
               parent_dir: str,
               user_name: str,
               attendance_time: datetime,
               leave_time: datetime,
               break_time: datetime,
               start_date: datetime,
               end_date: datetime):
        """
        :param user_name: ユーザー名
        :param parent_dir 親ディレクトリ
        :param attendance_time: 出勤時間
        :param leave_time: 退勤時間
        :param break_time 休憩時間
        :param start_date: シート作成開始日
        :param end_date: シート作成終了日
        :return: None
        """
        for sheet_date in DateUtil.create_date_range_for_month(start_date, end_date):

            # テンプレートごとにファイル作成
            for template in self.template_list:
                temp_parent_dir = parent_dir

                # テンプレートごとにディレクトリを分ける
                if len(self.template_list) > 1:
                    temp_parent_dir = pathlib.Path(temp_parent_dir).joinpath(template.value)

                # 年ごとにディレクトリを分ける
                temp_parent_dir = pathlib.Path(temp_parent_dir).joinpath(f'{sheet_date.year}年')

                # 親ディレクトリ作成
                FileUtil.make_dirs(str(temp_parent_dir))

                # ユーザー名が存在する場合は、末尾に追記
                filename = f"勤務表_{sheet_date.strftime('%Y%m')}.xlsx"
                if user_name:
                    filename = f"勤務表_{sheet_date.strftime('%Y%m')}({user_name}).xlsx"

                file_path = str(temp_parent_dir.joinpath(filename).resolve())

                use_case = self.__create_use_case(template)
                use_case.invoke(UserInputData(
                    user_name=user_name,
                    filename=file_path,
                    sheet_date=sheet_date,
                    attendance_time=attendance_time,
                    leave_time=leave_time,
                    break_time=break_time
                ))

    @staticmethod
    def __create_use_case(template_type: TemplateType) -> CreateAttendanceSheetUseCase:
        # TODO テンプレートが増えたら、if文追加
        return CreateAttendanceSheetTemplate1Interactor(ExcelRepository())
