# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py',
    ],

    pathex=[
    'arithmetic.py','cal_rouge.py','distributed.py','Huffman_Encoding.py','m_weibo_send_2.py','news_input.py',
    'post_stats.py','preprocess.py','run_stega_optimized.py','train.py','train_abstractive.py',
    'train_extractive.py','utils.py','weibo.py','weibo_2.py',
    'C:\\Users\\dell\\.virtualenvs\\newpp-BE-8tpyx\\Lib\\site-packages',

    'F:\\game\\xinandasai',

    'F:\\game\\xinandasai\\models',
   
    'F:\\game\\xinandasai\\others',
  
    'F:\\game\\xinandasai\\prepro',
   
    'F:\\game\\xinandasai\\translate',

    'F:\\game\\xinandasai\\clip'
   
    ],
    binaries=[],
    datas=[
    ('bert-base-uncased','bert-base-uncased'),
    ('bit_stream','bit_stream'),
    ('c_text','c_text'),
    ('crawler','crawler'),
    ('images','images'),
    ('input_data','input_data'),
    ('input_image','input_image'),
    ('json_data','json_data'),
    ('presumm_model','presumm_model'),
    ('pretrained_models','pretrained_models'),
    ('raw_data','raw_data'),
    ('results','results'),
    ('urls','urls'),
    ('read.txt','read.txt'),
    ('logs','logs'),
    ],
    hiddenimports=[
    'C:\\Users\\dell\\.virtualenvs\\newpp-BE-8tpyx\\Lib\\site-packages\\transformers',
     'C:\\Users\\dell\\.virtualenvs\\newpp-BE-8tpyx\\Lib\\site-packages\\huggingface_hub',
     ''
    ],
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
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
