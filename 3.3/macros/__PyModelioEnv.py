# Do not put some encoding here
import os

try:
    import pymodelioprofile.settings
    assert(pymodelioprofile.settings.DEBUG_PYMODELIO_CORE)
except:
    pass
else:
    try:
        del PYMODELIO_INITIALIZED
    except:
        pass
    try:
        PyModelioEnv.reboot()
    except Exception as e:
        print e


execfile(
    os.path.join(os.path.expanduser("~"), ".modelio", "pymodelioprofile",
                 "startup.py"))
