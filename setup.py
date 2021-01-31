import sys
from distutils.core import setup
import py2exe

# TODO 作成されたexeファイルが実行できない
if len(sys.argv) == 1:
    sys.argv.append('py2exe')

option = {
    'compressed': True,
    'optimize': 2,
    'bundle_files': 3,
    'includes': ['PySide2', 'PySide2.QtXml', 'openpyxl'],
}

setup(
    options={
        'py2exe': option,
    },
    windows=[
        {'script': 'main.py'}
    ],
    zipfile="lib/libs.zip"
)
