import unittest

from util.excel_util import ExcelUtil
from util.excelfunction.logic import AND, OR, NOT, IF, IS_BLANK, IS_NOT_BLANK, IF_ERROR


class TestAnd(unittest.TestCase):
    def test_and(self):
        expected = 'AND(A4 >= 10)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = AND(f'{A4} >= 10').to_str()
        self.assertEqual(expected, actual)

    def test_and_multiple_argument(self):
        expected = 'AND(A4 >= 10, A4 <= 20)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = AND(f'{A4} >= 10', f'{A4} <= 20').to_str()
        self.assertEqual(expected, actual)


class TestOr(unittest.TestCase):
    def test_and(self):
        expected = 'OR(A4 >= 10)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = OR(f'{A4} >= 10').to_str()
        self.assertEqual(expected, actual)

    def test_and_multiple_argument(self):
        expected = 'OR(A4 >= 10, A4 <= 20)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = OR(f'{A4} >= 10', f'{A4} <= 20').to_str()
        self.assertEqual(expected, actual)


class TestNot(unittest.TestCase):

    def test_not(self):
        expected = 'NOT(A4 >= 10)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = NOT(f'{A4} >= 10').to_str()
        self.assertEqual(expected, actual)


class TestIf(unittest.TestCase):
    def test_if(self):
        expected = 'IF(A4 >= 50, "合格")'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = IF(f'{A4} >= 50', '"合格"').to_str()
        self.assertEqual(expected, actual)

    def test_if_true_and_false(self):
        expected = 'IF(A4 >= 50, "合格", "不合格")'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = IF(f'{A4} >= 50', '"合格"', '"不合格"').to_str()
        self.assertEqual(expected, actual)


class TestIfError(unittest.TestCase):
    def test_if_error(self):
        expected = 'IFERROR(C3/B3, "--")'
        C3 = ExcelUtil.create_cell_string(column='C', row=3)
        B3 = ExcelUtil.create_cell_string(column='B', row=3)

        actual = IF_ERROR(f'{C3}/{B3}', '"--"').to_str()
        self.assertEqual(expected, actual)


class TestIsBlank(unittest.TestCase):
    def test_is_blank(self):
        expected = 'ISBLANK(A4)'
        A4 = ExcelUtil.create_cell_string(row=4, column='A')
        actual = IS_BLANK(A4).to_str()
        self.assertEqual(expected, actual)


class TestIsNotBlank(unittest.TestCase):
    def test_is_not_blank(self):
        expected = 'NOT(ISBLANK(N3))'
        N3 = ExcelUtil.create_cell_string(row=3, column='N')
        actual = IS_NOT_BLANK(N3).to_str()
        self.assertEqual(expected, actual)
