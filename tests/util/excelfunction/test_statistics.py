import unittest

from util.excel_util import ExcelUtil
from util.excelfunction.statistics import COUNT_IF


class TestCountIf(unittest.TestCase):

    def test_count_if(self):
        expected = 'COUNTIF($C$16:$C$46, "=出勤")'
        cell_range = ExcelUtil.create_cell_range_string(start_column='C',
                                                        start_row=16,
                                                        end_column='C',
                                                        end_row=46,
                                                        fixed_start_column=True,
                                                        fixed_start_row=True,
                                                        fixed_end_row=True,
                                                        fixed_end_column=True)
        actual = COUNT_IF(cell_range, '"=出勤"').to_str()
        self.assertEqual(expected, actual)
