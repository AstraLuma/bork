from pathlib import Path
import sys

from . import builder
# from . import github
from . import pypi
from .filesystem import load_setup_cfg, try_delete


def build():
    config = load_setup_cfg()
    if 'bork' in config:
        config = config['bork']

        want_zipapp = config.get('zipapp', 'false').lower() == 'true'
        zipapp_main = config.get('zipapp_main', None)
    else:
        want_zipapp = False

    builder.dist()

    if want_zipapp:
        raise Exception("zipapp builds are broken as hell, sorry. :(")
        # builder.zipapp()


def clean():
    config = load_setup_cfg()
    name = config['metadata']['name']

    try_delete("./build")
    try_delete("./dist")
    try_delete("./{}.egg-info".format(name))


def release(dry_run=False):
    pypi.upload('./dist/*.tar.gz', './dist/*.whl', dry_run=dry_run)

    print('')
    print('')

    # if 'github' in args:
    #     github.upload('./dist/*.pyz', dry_run=dry_run)
