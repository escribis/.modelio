# Do not put some encoding here
DEBUG = True
import os
execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile", "startup.py"))
from pymodelio.core.env import PyModelioEnv
PyModelioEnv.execute(
    'oclscribe.macro_add_invariant',['oclscribe.profile'],DEBUG)
