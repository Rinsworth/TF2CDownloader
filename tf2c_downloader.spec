# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import os
from platform import system
import glob

def data_generator():
	datas = []
	if system() == 'Windows':
		datas.append(('Binaries/*', '.'))
	
	for p in glob.iglob("locale/**/*.mo", recursive=True):
		datas.append((p,os.path.dirname(p)))
	
	return datas

a = Analysis(
    ['tf2c_downloader.py'],
    pathex=[],
    binaries=[],
    datas=data_generator(),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='tf2c_downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='tf2c.ico',
)
