# Do not put some encoding here
DEBUG=True
import os

execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile",
                 "startup.py"))
execfile(r'C:\DEV\PyModelio\demos\graphs_demos\graph.py')
#PyModelioEnv.execute('sandbox.helloworld.macro_helloworld',[],DEBUG)
#PyModelioEnv.execute('sandbox.textualtree_test.macro_treetester',["pymodelio.misc.textual_tree"],DEBUG)
#PyModelioEnv.execute('sandbox.gui_test.macro_gui',[],DEBUG)
#PyModelioEnv.execute('sandbox.visit_test.macro_visit',[],DEBUG)
#PyModelioEnv.execute('sandbox.pydtest.macro_pydtest',[],DEBUG)
#PyModelioEnv.execute('sandbox.oossmapper.macro_oossmapper',["sandbox.ooss"],DEBUG)

