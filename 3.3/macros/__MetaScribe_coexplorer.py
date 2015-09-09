# Do not put some encoding here
DEBUG=True
import os

execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile",
                 "startup.py"))
modules=[
   'metascribe.explorer',
   'metascribe.onlinepyscript',
   'metascribe.virtual',
   'metascribe.webdoc',
   'metascribe.webpublisher',
   'metascribe.images',
   'metascribe.introspection',
   'metascribe.explorer']
from pymodelio.core.env import PyModelioEnv
PyModelioEnv.execute('metascribe.macro_coexplorer',modules,DEBUG)
from metascribe.explorer import explore,exp,show

    



