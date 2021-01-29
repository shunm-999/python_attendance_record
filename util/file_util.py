import os
import pathlib
import shutil


class FileUtil:

    @staticmethod
    def is_exists(path: str) -> bool:
        return pathlib.Path(path).exists()

    @staticmethod
    def save_file(filename, file_content="", mode='w'):
        FileUtil.save_file_at_dir(dir_path=pathlib.Path.cwd(), filename=filename, file_content=file_content, mode=mode)

    @staticmethod
    def save_file_at_dir(dir_path, filename, file_content, mode='w'):
        plb = pathlib.Path(os.path.join(dir_path, filename))
        FileUtil.make_dirs(path=plb.parent)
        with open(plb, mode) as f:
            f.write(file_content)

    @staticmethod
    def make_dirs(path: str, parents=True, exist_ok=True) -> None:
        try:
            pathlib.Path(path).mkdir(parents=parents, exist_ok=exist_ok)
        except FileNotFoundError:
            pass

    @staticmethod
    def delete(path: str):
        try:
            plb = pathlib.Path(path)
            if not plb.exists():
                return

            if plb.is_file():
                plb.unlink(missing_ok=True)
            elif plb.is_dir():
                shutil.rmtree(plb)
        except IOError:
            pass
