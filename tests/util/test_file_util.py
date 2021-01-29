import pathlib
import shutil
import unittest

from util.file_util import FileUtil


class TestFileUtil(unittest.TestCase):

    def setUp(self) -> None:
        self.filename1 = "sample.txt"
        self.filename2 = "test_folder/sample.txt"
        self.dir1 = "test_folder/test_folder"

    def test_is_exist_False(self):
        self.assertFalse(FileUtil.is_exists(self.filename1))

    def test_is_exist_True(self):
        FileUtil.save_file(self.filename1)
        self.assertTrue(FileUtil.is_exists(self.filename1))

    def test_save_file_and_make_dir(self):
        FileUtil.save_file(self.filename2)
        self.assertTrue(FileUtil.is_exists(self.filename2))

    def test_make_dir(self):
        FileUtil.make_dirs(self.dir1)
        self.assertTrue(FileUtil.is_exists(self.dir1))

    def test_delete_not_exist_file(self):
        FileUtil.delete(self.filename1)
        FileUtil.delete(self.filename2)

    def test_delete(self):
        FileUtil.save_file(self.filename1)
        self.assertTrue(FileUtil.is_exists(self.filename1))
        FileUtil.delete(self.filename1)
        self.assertFalse(FileUtil.is_exists(self.filename1))

    def test_delete_dir(self):
        FileUtil.make_dirs(self.dir1)
        self.assertTrue(FileUtil.is_exists(self.dir1))
        FileUtil.delete(self.dir1)
        self.assertFalse(FileUtil.is_exists(self.dir1))

    def tearDown(self) -> None:
        try:
            pathlib.Path(self.filename1).unlink(missing_ok=True)
            shutil.rmtree(pathlib.Path("test_folder"))
        except IOError:
            pass
