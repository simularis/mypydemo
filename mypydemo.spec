# -*- mode: python ; coding: utf-8 -*-

import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_icon=os.path.join(gooey_root, 'images', 'program_icon.ico')

a1 = Analysis(
    ['myscript.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
a2 = Analysis(
    ['mygooey1.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy'],
    noarchive=False,
)
a3 = Analysis(
    ['mygooey2.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy'],
    noarchive=False,
)
MERGE(
    (a1,'myscript','myscript'),
    (a2, 'mygooey1','mygooey1'),
    (a3, 'mygooey2','mygooey2')
)

collectables = []

for a,name,console,icon in [
    (a1,'myscript',True, None),
    (a2,'mygooey1',False, gooey_icon),
    (a3,'mygooey2',False, gooey_icon)
    ]:
    pyz = PYZ(a.pure, a.zipped_data)
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=name,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=console,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icon,
    )
    # coll = COLLECT(
    #     exe,
    #     a.binaries,
    #     a.datas,
    #     strip=False,
    #     upx=True,
    #     upx_exclude=[],
    #     name=name,
    # )
    collectables.extend([exe, a.binaries, a.zipfiles, a.datas])

coll = COLLECT(
    *collectables,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mypydemo',
)
