# coding=utf-8

from .privatesettings import *

# Installation directory of PyModelio
PYMODELIO_MAIN  = r"C:\DEV\PyModelio"

# For developers. Local directory where plugins are going to be developed.
# If you are not a developer, just comment this line. A 'PyModelioLocal'
# directory will be created for you in your .modelio directory, but to don't
#  have to care about it.
PYMODELIO_LOCAL = r"C:\DEV\PyModelioLocal"

# For experts only. Should be set to False otherwise.
DEBUG_PYMODELIO_CORE = True

# 
ONLINE_PY_SCRIBE_DOCUMENT_URL_PATTERN = 'http://collabedit.com/download?id=%s' 
# ONLINE_PY_SCRIBE_ID value set in privatesettings


#===== TEXT EDITOR ============================================================


#----- notepad++ editor -------------------------------------------------------
EDITOR = r'c:\S\Notepad++\notepad++.exe'
EDITOR_OPEN_FILE = [EDITOR, '{file}']
EDITOR_OPEN_FILE_AT = [EDITOR, '{file}', '-n{line}']

#----- vi editor --------------------------------------------------------------
# EDITOR = r'vi'
# EDITOR_OPEN_FILE = [EDITOR, '{file}']
# EDITOR_OPEN_FILE_AT = [EDITOR, '+{line}', '{file}' ]

#----- eclipse editor ---------------------------------------------------------
# EDITOR = r'eclipse.exe'
# EDITOR_OPEN_FILE = [EDITOR, '--launcher.openFile', '{file}']
# EDITOR_OPEN_FILE_AT = [EDITOR, '{file}']   # not supported

#----- pycharm editor ---------------------------------------------------------
# EDITOR = r'pycharm.bat'
# EDITOR_OPEN_FILE = [EDITOR, '{file}']
# EDITOR_OPEN_FILE_AT = [EDITOR, '-n', '{line}' '{file}']





#===== USE OCL ================================================================
USE_OCL_COMMAND = 'use'



print '@'*160
print 'settings loaded'
