# -*- mode: python -*-

import os
import sys
sys.modules['FixTk'] = None

import subprocess
import shutil
import glob
import json

try:
    from PyInstaller.utils.hooks import collect_data_files, remove_prefix
except ImportError:
    from PyInstaller.hooks.hookutils import collect_data_files, remove_prefix

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/travis/build/Podshot/Travis-Ci-OSX-Testing'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=['Tkinter', 'tkinter', '_tkinter', 'Tcl', 'tcl', 'Tk', 'tk', 'wx', 'FixTk'],
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
#          a.binaries,
#          a.zipfiles,
#          a.datas,
          exclude_binaries=True,
          name='mcedit_unified',
          debug=True,
          strip=None,
          upx=False,
          runtime_tmpdir=None,
          console=True,
          icon='mcedit.icns')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='mcedit_unified')

app = BUNDLE(coll,
             name='mcedit-unified.app',
             icon='mcedit.icns',
             bundle_identifier='net.mcedit-unified.mcedit-unified')