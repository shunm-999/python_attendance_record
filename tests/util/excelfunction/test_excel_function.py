import unittest

from util.excel_util import ExcelUtil
from util.excelfunction.datetime import DATE, YEAR, MONTH
from util.excelfunction.logic import IF, IS_BLANK, AND, IS_NOT_BLANK
from util.excelfunction.string import TEXT, TextFormat


class TestExcelFunction(unittest.TestCase):

    def test_attendance_name(self):
        expected = 'YEAR(N3)&"年"&MONTH(N3)&"月 勤務表"'
        n3 = ExcelUtil.create_cell_string(row=3, column='N')
        actual = f'{YEAR(n3)}&"年"&{MONTH(n3)}&"月 勤務表"'
        self.assertEqual(expected, actual)

    def test_text_from_datetime(self):
        expected = 'TEXT(DATE(YEAR($N$3), MONTH($N$3), $A16), "ddd")'

        n3 = ExcelUtil.create_cell_string(row=3, column='N', fixed_row=True, fixed_column=True)
        a16 = ExcelUtil.create_cell_string(row=16, column='A', fixed_column=True)

        actual = TEXT(
            DATE(YEAR(n3), MONTH(n3), a16),
            TextFormat.DAY_OF_WEEK_ENGLISH
        ).to_str()
        self.assertEqual(expected, actual)

    def test_attendance_time(self):
        expected = 'IF(ISBLANK($C16), "", $N$7)'

        c16 = ExcelUtil.create_cell_string(row=16, column='C', fixed_column=True)
        n7 = ExcelUtil.create_cell_string(row=7, column='N', fixed_row=True, fixed_column=True)

        actual = IF(IS_BLANK(c16), '""', n7).to_str()
        self.assertEqual(expected, actual)

    def test_overtime_hours(self):
        expected = 'IF(AND(NOT(ISBLANK($J16)), ($G16-$F16) - ($E16 - $D16) > 0), ($G16-$F16) - ($E16 - $D16), "")'
        J16 = ExcelUtil.create_cell_string(row=16, column='J', fixed_column=True)

        D16 = ExcelUtil.create_cell_string(row=16, column='D', fixed_column=True)
        E16 = ExcelUtil.create_cell_string(row=16, column='E', fixed_column=True)
        F16 = ExcelUtil.create_cell_string(row=16, column='F', fixed_column=True)
        G16 = ExcelUtil.create_cell_string(row=16, column='G', fixed_column=True)

        overtime = f'({G16}-{F16}) - ({E16} - {D16})'
        actual = IF(AND(IS_NOT_BLANK(J16), f'{overtime} > 0'), overtime, '""').to_str()
        self.assertEqual(expected, actual)

    def test_working_hours(self):
        expected = 'IF(AND(NOT(ISBLANK($G16)), NOT(ISBLANK($F16)), $G16-$F16-$H16 > 0), $G16-$F16-$H16, "")'

        F16 = ExcelUtil.create_cell_string(row=16, column='F', fixed_column=True)
        G16 = ExcelUtil.create_cell_string(row=16, column='G', fixed_column=True)
        H16 = ExcelUtil.create_cell_string(row=16, column='H', fixed_column=True)

        working_hours = f'{G16}-{F16}-{H16}'
        actual = IF(AND(IS_NOT_BLANK(G16), IS_NOT_BLANK(F16), f'{working_hours} > 0'), working_hours, '""').to_str()
        self.assertEqual(expected, actual)
