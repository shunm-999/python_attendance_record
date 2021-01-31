import calendar

from const.alignmentconst import AlignmentConst
from data.user_input_data import UserInputData
from repository.excel_repository_interface import ExcelRepositoryInterface
from usecase.create_attendance_sheet_usecase import CreateAttendanceSheetUseCase
from util.excel_util import ExcelUtil
from util.excelfunction.calculation import SUM
from util.excelfunction.datetime import YEAR, MONTH, DATE
from util.excelfunction.logic import IF, AND, IS_NOT_BLANK, IF_ERROR
from util.excelfunction.statistics import COUNT_IF
from util.excelfunction.string import TEXT, TextFormat


class CreateAttendanceSheetTemplate1Interactor(CreateAttendanceSheetUseCase):

    def __init__(self, excel_repository: ExcelRepositoryInterface):
        super().__init__(excel_repository)
        self.excel_repository = excel_repository
        self.commuting, self.absense, self.holidays, self.substitute_holiday = "出勤", "欠勤", "有給休暇", "代休"
        self.attendance_classfication = [self.commuting, self.absense, self.holidays, self.substitute_holiday]

    def invoke(self, input_data: UserInputData):
        self.modify_row_dimension()
        self.merge_cell()
        self.set_cell_color()
        self.set_cell_border(input_data)
        self.set_text_alignment(input_data)
        self.set_cell_number_format(input_data)
        self.set_header(input_data)
        self.set_data(input_data)
        self.excel_repository.save(input_data.filename)

    def modify_row_dimension(self) -> None:
        """
        セル幅を調整する
        :return: None
        """

        for column in range(1, 16):
            self.excel_repository.set_column_width(column, 12)
        for row in range(1, 200):
            self.excel_repository.set_row_height(row, 15)
        self.excel_repository.set_column_width('A', 6)
        self.excel_repository.set_column_width('B', 6)
        self.excel_repository.set_column_width('L', 4)
        self.excel_repository.set_column_width('M', 20)

    def merge_cell(self) -> None:
        """
        セルを統合する
        :return: None
        """
        # 題名
        self.excel_repository.merge_cells(start_column='A', start_row=2, end_column='E', end_row=3)

        # 所属・名前
        self.excel_repository.merge_cells(start_column='A', start_row=6, end_column='B', end_row=6)
        self.excel_repository.merge_cells(start_column='A', start_row=7, end_column='B', end_row=7)
        self.excel_repository.merge_cells(start_column='C', start_row=6, end_column='D', end_row=6)
        self.excel_repository.merge_cells(start_column='C', start_row=7, end_column='D', end_row=7)

        # 各種項目
        for row_num in range(9, 13):
            self.excel_repository.merge_cells(start_column='A', start_row=row_num, end_column='C', end_row=row_num)
            self.excel_repository.merge_cells(start_column='D', start_row=row_num, end_column='E', end_row=row_num)
            self.excel_repository.merge_cells(start_column='F', start_row=row_num, end_column='G', end_row=row_num)

        # ヘッダー
        self.excel_repository.merge_cells(start_column='A', start_row=14, end_column='B', end_row=14)
        self.excel_repository.merge_cells(start_column='C', start_row=14, end_column='C', end_row=15)
        self.excel_repository.merge_cells(start_column='D', start_row=14, end_column='E', end_row=14)
        self.excel_repository.merge_cells(start_column='F', start_row=14, end_column='I', end_row=14)
        self.excel_repository.merge_cells(start_column='J', start_row=14, end_column='K', end_row=14)

    def set_cell_color(self):
        """
        セルの色を指定する
        :return:
        """
        pattern_type = 'solid'
        color = 'd0e0e3'

        self.excel_repository.set_pattern_fill(start_column='A', start_row=6, end_column='B', pattern_type=pattern_type,
                                               fg_color=color)
        self.excel_repository.set_pattern_fill(start_column='A', start_row=7, end_column='B', pattern_type=pattern_type,
                                               fg_color=color)

        self.excel_repository.set_pattern_fill(start_column='A', start_row=9, end_column='G', pattern_type=pattern_type,
                                               fg_color=color)
        self.excel_repository.set_pattern_fill(start_column='A', start_row=11, end_column='G',
                                               pattern_type=pattern_type,
                                               fg_color=color)

        self.excel_repository.set_pattern_fill(start_column='A', start_row=14, end_column='K', end_row=15,
                                               pattern_type=pattern_type, fg_color=color)

        self.excel_repository.set_pattern_fill(start_column='M', start_row=7, end_row=9,
                                               pattern_type=pattern_type, fg_color=color)

    def set_cell_border(self, input_data: UserInputData):
        """
        枠線を追加
        :param input_data: ユーザーの入力データ
        :return: None
        """
        for column_num in range(1, 6):
            self.excel_repository.set_border(column=column_num, row=3, bottom=True, style='double')
        self.excel_repository.set_ruled_line(start_column='A', start_row=6, end_column='D', end_row=7)
        self.excel_repository.set_ruled_line(start_column='A', start_row=9, end_column='G', end_row=12)

        sheet_date = input_data.sheet_date
        last_day_of_month = calendar.monthrange(sheet_date.year, sheet_date.month)[1]

        self.excel_repository.set_ruled_line(start_column='A', start_row=14, end_column='K',
                                             end_row=15 + last_day_of_month)
        self.excel_repository.set_ruled_line(start_column='M', start_row=7, end_column='N',
                                             end_row=9)
        self.excel_repository.set_ruled_line(start_column='M', start_row=12, end_column='M',
                                             end_row=12 + max(len(self.attendance_classfication) - 1, 0))
        self.excel_repository.set_border(column='N', row=3, bottom=True)

    def set_text_alignment(self, input_data):
        sheet_date = input_data.sheet_date
        last_day_of_month = calendar.monthrange(sheet_date.year, sheet_date.month)[1]
        # 全体のセルを、水平左揃え、縦方向中央揃えに変更する
        self.excel_repository.set_text_alignments(start_column='A', start_row=1, end_column='N',
                                                  end_row=16 + (last_day_of_month - 1),
                                                  horizontal=AlignmentConst.LEFT, vertical=AlignmentConst.CENTER)

        # 題名
        self.excel_repository.set_text_alignment(column='A', row=2,
                                                 horizontal=AlignmentConst.CENTER,
                                                 vertical=AlignmentConst.CENTER)
        # ヘッダー
        self.excel_repository.set_text_alignments(start_column='A', start_row=14, end_column='K', end_row=15,
                                                  horizontal=AlignmentConst.CENTER, vertical=AlignmentConst.CENTER)

        # 日付 / 曜日
        self.excel_repository.set_text_alignments(start_column='A', start_row=16, end_column='B',
                                                  end_row=16 + (last_day_of_month - 1),
                                                  horizontal=AlignmentConst.CENTER, vertical=AlignmentConst.CENTER)

    def set_cell_number_format(self, input_data):
        """
        セルの書式設定
        :return: None
        """
        sheet_date = input_data.sheet_date
        last_day_of_month = calendar.monthrange(sheet_date.year, sheet_date.month)[1]

        self.excel_repository.set_number_format(column='D', row=12, number_format='[h]:mm')
        self.excel_repository.set_number_format(column='F', row=12, number_format='[h]:mm')
        for index in range(0, last_day_of_month):
            self.excel_repository.set_number_format(column='I', row=16 + index, number_format='[h]:mm')
            self.excel_repository.set_number_format(column='J', row=16 + index, number_format='[h]:mm')
            self.excel_repository.set_number_format(column='K', row=16 + index, number_format='[h]:mm')

    def set_header(self, input_data: UserInputData):
        # 題名
        N3 = ExcelUtil.create_cell_string(column='N', row=3, fixed_column=True, fixed_row=True)
        self.excel_repository.set_font(column='A', row=2, bold=True)
        self.excel_repository.put(column='A', row=2, value='=' + f'{YEAR(N3)}&"年"&{MONTH(N3)}&"月 勤務表"')

        # 日付
        sheet_date = input_data.sheet_date
        self.excel_repository.put(column='N', row=3, value=f'{sheet_date.year}/{sheet_date.month}/{sheet_date.day}')

        # 名前
        self.excel_repository.put(column='C', row=7, value=input_data.user_name)

        # 項目
        header = [['A', 6, "所属"],
                  ['A', 7, "名前"],
                  ['A', 9, "出勤日数"],
                  ['D', 9, "欠勤日数"],
                  ['F', 9, "有給取得日数"],
                  ['A', 11, "代休取得日数"],
                  ['D', 11, "総勤務時間"],
                  ['F', 11, "総残業時間"],
                  ['A', 14, "勤務時間"],
                  ['A', 15, "日付"],
                  ['B', 15, "曜日"],
                  ['C', 14, "勤怠区分"],
                  ['D', 14, "予定"],
                  ['D', 15, "出社時刻"],
                  ['E', 15, "退社時刻"],
                  ['F', 14, "実施"],
                  ['F', 15, "出社時刻"],
                  ['G', 15, "退社時刻"],
                  ['H', 15, "休憩時間"],
                  ['I', 15, "残業時間"],
                  ['J', 14, "実施時間"],
                  ['J', 15, "当日"],
                  ['K', 15, "累計"],
                  ['M', 6, "時間設定"],
                  ['M', 7, "就業開始時刻"],
                  ['M', 8, "就業終了時刻"],
                  ['M', 9, "休憩時間"],
                  ['M', 11, "勤怠区分"]]

        for column, row, value in header:
            self.excel_repository.put(column=column, row=row, value=value)

    def set_data(self, input_data: UserInputData):
        """
        データを追加
        :param input_data: ユーザーの入力データ
        :return: None
        """
        sheet_date = input_data.sheet_date
        last_day_of_month = calendar.monthrange(sheet_date.year, sheet_date.month)[1]

        # 日数
        # 出勤日数
        attendance_count_cell_range = ExcelUtil.create_cell_range_string(start_column='C', start_row=16, end_column='C',
                                                                         end_row=16 + (last_day_of_month - 1),
                                                                         fixed_start_column=True, fixed_start_row=True,
                                                                         fixed_end_column=True, fixed_end_row=True)
        self.excel_repository.put(column='A', row=10,
                                  value='=' + COUNT_IF(attendance_count_cell_range, '"=出勤"').to_str())
        # 欠勤日数
        self.excel_repository.put(column='D', row=10,
                                  value='=' + COUNT_IF(attendance_count_cell_range, '"=欠勤"').to_str())
        # 有給取得日数
        self.excel_repository.put(column='F', row=10,
                                  value='=' + COUNT_IF(attendance_count_cell_range, '"=有給休暇"').to_str())
        # 代休取得日数
        self.excel_repository.put(column='A', row=12,
                                  value='=' + COUNT_IF(attendance_count_cell_range, '"=代休"').to_str())
        # 総勤務時間
        working_hour_cell_range = ExcelUtil.create_cell_range_string(start_column='J', start_row=16, end_column='J',
                                                                     end_row=16 + (last_day_of_month - 1),
                                                                     fixed_start_column=True, fixed_start_row=True,
                                                                     fixed_end_column=True, fixed_end_row=True)
        self.excel_repository.put(column='D', row=12, value='=' + SUM(working_hour_cell_range).to_str())

        # 総残業時間
        overtime_working_cell_range = ExcelUtil.create_cell_range_string(start_column='I', start_row=16, end_column='I',
                                                                         end_row=16 + (last_day_of_month - 1),
                                                                         fixed_start_column=True, fixed_start_row=True,
                                                                         fixed_end_column=True, fixed_end_row=True)
        self.excel_repository.put(column='F', row=12, value='=' + SUM(overtime_working_cell_range).to_str())

        # 時間設定
        attendance_time = input_data.attendance_time
        leave_time = input_data.leave_time
        break_time = input_data.break_time
        self.excel_repository.put(column='N', row=7, value=attendance_time.strftime('%H:%M'))
        self.excel_repository.put(column='N', row=8, value=leave_time.strftime('%H:%M'))
        self.excel_repository.put(column='N', row=9, value=break_time.strftime('%H:%M'))

        # 勤怠区分
        for index, classfication in enumerate(self.attendance_classfication):
            self.excel_repository.put(column='M', row=12 + index, value=classfication)

        # 日付列
        for index in range(0, last_day_of_month):
            self.excel_repository.put(column='A', row=16 + index, value=str(1 + index))

        # 曜日列
        for index in range(0, last_day_of_month):
            N3 = ExcelUtil.create_cell_string(column='N', row=3, fixed_row=True, fixed_column=True)
            A_col = ExcelUtil.create_cell_string(column='A', row=16 + index, fixed_column=True)

            day_of_month = "=" + TEXT(
                DATE(YEAR(N3), MONTH(N3), A_col),
                TextFormat.DAY_OF_WEEK_SHORT
            ).to_str()
            self.excel_repository.put(column='B', row=16 + index, value=day_of_month)

        # 勤怠区分列
        classfication_cell_range = ExcelUtil.create_cell_range_string(start_column='M',
                                                                      start_row=12,
                                                                      end_column='M',
                                                                      end_row=12 + max(
                                                                          len(self.attendance_classfication) - 1,
                                                                          0),
                                                                      fixed_start_column=True,
                                                                      fixed_start_row=True,
                                                                      fixed_end_column=True,
                                                                      fixed_end_row=True)
        self.excel_repository.set_data_validation_from_cell_range(start_row=16, end_row=16 + (last_day_of_month - 1),
                                                                  column='C', cell_range=classfication_cell_range)

        # 予定（出社時刻・退社時刻）
        for index in range(0, last_day_of_month):
            C_col = ExcelUtil.create_cell_string(column='C', row=16 + index, fixed_column=True)
            N7 = ExcelUtil.create_cell_string(column='N', row=7, fixed_column=True, fixed_row=True)
            N8 = ExcelUtil.create_cell_string(column='N', row=8, fixed_column=True, fixed_row=True)

            self.excel_repository.put(column='D', row=16 + index,
                                      value='=' + IF(f'{C_col}="{self.commuting}"', N7, '""').to_str())
            self.excel_repository.put(column='E', row=16 + index,
                                      value='=' + IF(f'{C_col}="{self.commuting}"', N8, '""').to_str())

        # 実施（休憩時間・残業時間）
        for index in range(0, last_day_of_month):
            # 休憩時間
            C_col = ExcelUtil.create_cell_string(column='C', row=16 + index, fixed_column=True)
            N9 = ExcelUtil.create_cell_string(column='N', row=9, fixed_column=True, fixed_row=True)
            self.excel_repository.put(column='H', row=16 + index,
                                      value='=' + IF(f'{C_col}="{self.commuting}"', N9, '""').to_str())

            # 残業時間
            J_col = ExcelUtil.create_cell_string(column='J', row=16 + index, fixed_column=True)
            D_col = ExcelUtil.create_cell_string(column='D', row=16 + index, fixed_column=True)
            E_col = ExcelUtil.create_cell_string(column='E', row=16 + index, fixed_column=True)
            F_col = ExcelUtil.create_cell_string(column='F', row=16 + index, fixed_column=True)
            G_col = ExcelUtil.create_cell_string(column='G', row=16 + index, fixed_column=True)

            overtime = f'({G_col}-{F_col}) - ({E_col} - {D_col})'
            self.excel_repository.put(column='I',
                                      row=16 + index,
                                      value='=' + IF_ERROR(IF(
                                          AND(IS_NOT_BLANK(G_col), IS_NOT_BLANK(F_col), IS_NOT_BLANK(J_col),
                                              f'{C_col}="{self.commuting}"', f'{overtime} > 0'),
                                          overtime, '""'), '""').to_str())
        # 実働時間 （当日・累計）
        for index in range(0, last_day_of_month):
            C_col = ExcelUtil.create_cell_string(column='C', row=16 + index, fixed_column=True)
            F_col = ExcelUtil.create_cell_string(column='F', row=16 + index, fixed_column=True)
            G_col = ExcelUtil.create_cell_string(column='G', row=16 + index, fixed_column=True)
            H_col = ExcelUtil.create_cell_string(column='H', row=16 + index, fixed_column=True)

            # 当日
            working_hours = f'{G_col}-{F_col}-{H_col}'
            self.excel_repository.put(column='J', row=16 + index, value='=' + IF_ERROR(IF(
                AND(IS_NOT_BLANK(G_col), IS_NOT_BLANK(F_col), f'{C_col}="{self.commuting}"', f'{working_hours} > 0'),
                working_hours, '""'), '""').to_str())

            # 累計
            sum_cell_range = ExcelUtil.create_cell_range_string(start_column='J', start_row=16, end_column='J',
                                                                end_row=16 + index, fixed_start_row=True,
                                                                fixed_start_column=True, fixed_end_column=True)
            self.excel_repository.put(column='K', row=16 + index, value='=' + SUM(sum_cell_range).to_str())
