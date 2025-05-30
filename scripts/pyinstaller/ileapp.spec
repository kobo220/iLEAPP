# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['..\\..\\ileapp.py'],
             pathex=['..\\scripts\\artifacts'],
             binaries=[],
             datas=[('..\\', '.\\scripts')],
             hiddenimports=[
                'astc_decomp_faster',
                'bencoding',
                'blackboxprotobuf',
                'Crypto.Cipher.AES',
                'ijson',
                'lib2to3.refactor',
                'liblzfse',
                'mdplist',
                'mmh3',
                'nska_deserialize',
                'pandas',
                'pgpy',
                'pillow_heif',
                'xml.etree.ElementTree',
                ],
             hookspath=['./'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ileapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          version='ileapp-file_version_info.txt',
          console=True )
