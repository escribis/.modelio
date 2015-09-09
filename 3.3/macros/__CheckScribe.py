# Do not put some encoding here
DEBUG=True
import os

execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile",
                 "startup.py"))
modules=[
   'checkscribe'
]
from pymodelio.core.env import PyModelioEnv
PyModelioEnv.execute('checkscribe.macro_check',modules,DEBUG)
