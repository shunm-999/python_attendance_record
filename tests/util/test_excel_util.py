import unittest

from util.excel_util import ExcelUtil


class TestExcelUtil(unittest.TestCase):

    def test_create_range_string_from_number(self):
        expected = 'C1:D16'
        actual = ExcelUtil.create_cell_range_string(start_row=1, start_column=3, end_row=16, end_column=4)
        self.assertEqual(expected, actual)

    def test_create_range_string_from_letter(self):
        expected = 'C1:D16'
        actual = ExcelUtil.create_cell_range_string(start_row=1, start_column='C', end_row=16, end_column='D')
        self.assertEqual(expected, actual)

    def test_create_range_string_fixed(self):
        expected = '$C$1:$D$16'
        actual = ExcelUtil.create_cell_range_string(start_row=1, start_column='C', end_row=16, end_column='D',
                                                    fixed_start_row=True, fixed_start_column=True, fixed_end_row=True,
                                                    fixed_end_column=True)
        self.assertEqual(expected, actual)
