import unittest

from util.excel_util import ExcelUtil
from util.excelfunction.calculation import SUM


class TestCalculation(unittest.TestCase):

    def test_sum(self):
        expected = 'SUM(C4:C16)'

        cell_range = ExcelUtil.create_cell_range_string(start_row=4, start_column='C', end_row=16, end_column='C')
        actual = SUM(cell_range).to_str()
        self.assertEqual(expected, actual)

    def test_sum_two_argument(self):
        expected = 'SUM($D$16:$D$30, 1)'
        cell_range = ExcelUtil.create_cell_range_string(start_row=16, start_column='D', end_row=30, end_column='D',
                                                        fixed_start_column=True, fixed_start_row=True, fixed_end_row=True,
                                                        fixed_end_column=True)
        actual = SUM(cell_range, 1).to_str()
        self.assertEqual(expected, actual)

    def test_sum_three_argument(self):
        expected = 'SUM($D$16:$D$30, 1, 10)'
        cell_range = ExcelUtil.create_cell_range_string(start_row=16, start_column='D', end_row=30, end_column='D',
                                                        fixed_start_column=True, fixed_start_row=True, fixed_end_row=True,
                                                        fixed_end_column=True)
        actual = SUM(cell_range, 1, 10).to_str()
        self.assertEqual(expected, actual)
