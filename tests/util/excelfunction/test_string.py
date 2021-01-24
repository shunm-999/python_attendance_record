import unittest

from util.excelfunction.string import TEXT, TextFormat


class TestString(unittest.TestCase):
    def test_text_day_of_week(self):
        expected = 'TEXT("2020/7/1", "aaaa")'
        actual = TEXT('"2020/7/1"', TextFormat.DAY_OF_WEEK).to_str()
        self.assertEqual(expected, actual)

    def test_text_day_of_week_short(self):
        expected = 'TEXT("2020/7/1", "aaa")'
        actual = TEXT('"2020/7/1"', TextFormat.DAY_OF_WEEK_SHORT).to_str()
        self.assertEqual(expected, actual)

    def test_text_day_of_week_english(self):
        expected = 'TEXT("2020/7/1", "ddd")'
        actual = TEXT('"2020/7/1"', TextFormat.DAY_OF_WEEK_ENGLISH).to_str()
        self.assertEqual(expected, actual)
