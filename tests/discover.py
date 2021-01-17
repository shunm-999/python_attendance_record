import sys
import unittest


def suite(directory_name: str):
    test_suite = unittest.TestSuite()
    all_test_suite = unittest.defaultTestLoader.discover(directory_name, pattern='*.py', top_level_dir='.')
    for ts in all_test_suite:
        test_suite.addTest(ts)
    return test_suite


if __name__ == '__main__':
    directory_name = 'tests'

    if len(sys.argv) > 1:
        directory_name = sys.argv[1]

    my_suite = suite(directory_name)
    unittest.TextTestRunner().run(my_suite)
