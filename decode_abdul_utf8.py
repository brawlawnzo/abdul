#! py3
'''make abdul transliterated again'''
import os
from unidecode import unidecode

SUFFIX = "_transl"

"""
Transliterating *.mtl files
"""

EXTENSION = ".mtl"

dirpath = os.getcwd()
for file in os.listdir(dirpath):
    if file.endswith(EXTENSION) and not file.endswith(SUFFIX + EXTENSION):
        INPUT_FILE_PATH = os.path.join(dirpath, file)
        OBJ_NAME = file[:file.rfind(".")]

OUTPUT_FILE_PATH = INPUT_FILE_PATH[:INPUT_FILE_PATH.rfind(".")] + SUFFIX + INPUT_FILE_PATH[INPUT_FILE_PATH.rfind("."):]

with open(INPUT_FILE_PATH, encoding="utf_8") as ifd:
    with open(OUTPUT_FILE_PATH, 'w') as ofd:
        for string in ifd:
            ofd.write(unidecode(string))


"""
Transliterating *.obj files
"""

EXTENSION = ".obj"

dirpath = os.getcwd()
for file in os.listdir(dirpath):
    if file.endswith(EXTENSION) and not file.endswith(SUFFIX + EXTENSION):
        INPUT_FILE_PATH = os.path.join(dirpath, file)
        OBJ_NAME = file[:file.rfind(".")]

OUTPUT_FILE_PATH = INPUT_FILE_PATH[:INPUT_FILE_PATH.rfind(".")] + SUFFIX + INPUT_FILE_PATH[INPUT_FILE_PATH.rfind("."):]

with open(INPUT_FILE_PATH, encoding="utf_8", errors="replace") as ifd:
    with open(OUTPUT_FILE_PATH, 'w') as ofd:
        for string in ifd:
            ofd.write(unidecode(string))


"""
Transliterating texture files' names
"""

TEX_FOLDER = dirpath + "\\" + OBJ_NAME
if not os.path.isdir(TEX_FOLDER + "_Texture") and os.path.isdir(TEX_FOLDER + "_Текстура"):
    os.rename(TEX_FOLDER + "_Текстура", TEX_FOLDER + "_Texture")
TEX_FOLDER = TEX_FOLDER + "_Texture"

for file in os.listdir(TEX_FOLDER):
    os.rename(os.path.join(TEX_FOLDER, file), os.path.join(TEX_FOLDER, unidecode(file)))
