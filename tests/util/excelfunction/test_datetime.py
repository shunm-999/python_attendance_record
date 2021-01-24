import unittest

from util.excel_util import ExcelUtil
from util.excelfunction.datetime import DATE, YEAR, MONTH, DAY


class TestDate(unittest.TestCase):

    def test_date_from_number(self):
        expected = 'DATE(2020, 7, 1)'
        actual = DATE(2020, 7, 1).to_str()
        self.assertEqual(expected, actual)

    def test_date_from_cell(self):
        expected = 'DATE(C16, C17, C18)'
        C16 = ExcelUtil.create_cell_string(column='C', row=16)
        C17 = ExcelUtil.create_cell_string(column='C', row=17)
        C18 = ExcelUtil.create_cell_string(column='C', row=18)
        actual = DATE(C16, C17, C18).to_str()
        self.assertEqual(expected, actual)

    def test_date_from_fixed_cell(self):
        expected = 'DATE($C$16, $C$17, $C$18)'
        C16 = ExcelUtil.create_cell_string(column='C', row=16, fixed_column=True, fixed_row=True)
        C17 = ExcelUtil.create_cell_string(column='C', row=17, fixed_column=True, fixed_row=True)
        C18 = ExcelUtil.create_cell_string(column='C', row=18, fixed_column=True, fixed_row=True)
        actual = DATE(C16, C17, C18).to_str()
        self.assertEqual(expected, actual)


class TestYear(unittest.TestCase):
    def test_year_from_string(self):
        expected = 'YEAR("2020/7/1")'
        actual = YEAR('"2020/7/1"').to_str()
        self.assertEqual(expected, actual)

    def test_year_from_cell(self):
        expected = 'YEAR(C1)'
        C1 = ExcelUtil.create_cell_string(column='C', row=1)
        actual = YEAR(C1).to_str()
        self.assertEqual(expected, actual)


class TestMonth(unittest.TestCase):
    def test_year_from_string(self):
        expected = 'MONTH("2020/7/1")'
        actual = MONTH('"2020/7/1"').to_str()
        self.assertEqual(expected, actual)

    def test_year_from_cell(self):
        expected = 'MONTH(C1)'
        C1 = ExcelUtil.create_cell_string(column='C', row=1)
        actual = MONTH(C1).to_str()
        self.assertEqual(expected, actual)


class TestDay(unittest.TestCase):
    def test_year_from_string(self):
        expected = 'DAY("2020/7/1")'
        actual = DAY('"2020/7/1"').to_str()
        self.assertEqual(expected, actual)

    def test_year_from_cell(self):
        expected = 'DAY(C1)'
        C1 = ExcelUtil.create_cell_string(column='C', row=1)
        actual = DAY(C1).to_str()
        self.assertEqual(expected, actual)
