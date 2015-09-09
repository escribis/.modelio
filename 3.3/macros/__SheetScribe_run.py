# Do not put some encoding here
DEBUG = True
import os

execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile",
                 "startup.py"))
from pymodelio.core.env import PyModelioEnv
modules = []
# PyModelioEnv.execute(
#    'sheetscribe.tests.test_poi.macro_poi_test',[],DEBUG)
# PyModelioEnv.execute(
#    'sheetscribe.tests.test_googlesheet.macro_googlesheet',[],DEBUG)
modules = ('sheetscribe.ooss', 'sheetscribe.snapshot', 'sheetscribe.tables',
    'sheetscribe.uml')
PyModelioEnv.execute(
    'sheetscribe.uml2ooss.macro_uml2ooss',modules,DEBUG)
