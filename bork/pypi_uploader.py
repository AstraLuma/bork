from twine.cli import dispatch as twine_upload
from . import file_finder


def upload(*globs):
    files = file_finder.find_files(globs, 'PyPI')
    twine_upload(["upload", *files])
