# coding=utf-8

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pymodelio.startup')

#---------- get PYMODELIO_MAIN path -------------------------------------------
import os
import sys
# import importlib



# The import of encodings module is necessary to avoid strange errors
# when loading some modules. This is due to the current version of modelio.
# noinspection PyUnresolvedReferences
import encodings # needed

log.info('Starting pymodelio...')
try:
    # Check if this variable is defined.
    # If yes, the framework has already been initialized.
    # So this file do not do anything.

    # noinspection
    log.debug('  Testing "PYMODELIO_INITIALIZED"')
    PYMODELIO_INITIALIZED
    log.debug('  Pymodelio already initialized')
except:
    log.info( '  Pymodelio has to be initialized')
    PYMODELIO_GLOBALS_SYMBOLS_BEFORE = set(list(globals().keys()))

    # This is the first time this file is executed, or at least it was never
    # executed completely because of errors.

    # Set WITH_MODELIO
    try:
        log.debug('Check if "Modelio" is defined to set WITH_MODELIO')
        Modelio
    except NameError:
        # This will happen for instance if Sphynx is looking at the source
        WITH_MODELIO = False
    else:
        WITH_MODELIO = True
    log.debug('  WITH_MODELIO = %s', WITH_MODELIO)



    #--------------------------------------------------------------------------
    # Try to find and set PYMODELIO_MAIN path variable.
    #--------------------------------------------------------------------------
    USER_MODELIO_DIR = os.path.join(os.path.expanduser('~'), '.modelio')
    log.debug('  USER_MODELIO_DIR = %s', USER_MODELIO_DIR)
    if USER_MODELIO_DIR not in sys.path:
        sys.path.insert(0,USER_MODELIO_DIR)
        log.info('  %s added to sys.path', USER_MODELIO_DIR)
    USER_PROFILE_SETTINGS = os.path.join(
        USER_MODELIO_DIR, 'pymodelioprofile','settings.py')
    try:
        # check if the variable is already defined at the top level
        PYMODELIO_MAIN
        log.info('  PYMODELIO_MAIN = %s', PYMODELIO_MAIN)
    except:
        # PYMODELIO_MAIN not defined. Get it from .modelio/pymodeliopaths.py
        log.info('  import pymodelioprofile.settings to get PYMODELIO_MAIN')
        try:
            import pymodelioprofile.settings
        except Exception as e:
            sys.stderr.write('-' * 80)
            sys.stderr.write('ERROR: cannot import pymodelioprofile.settings')
            sys.stderr.write('       Check the %s file', USER_PROFILE_SETTINGS)
            sys.stderr.write('-' * 80)
            log.exception('Cannot import pymodelioprofile.settings')
            raise
        else:
            log.info('  import done')

    # Check again that the variable is defined at the top level.
    try:
        PYMODELIO_MAIN = pymodelioprofile.settings.PYMODELIO_MAIN
    except Exception as e:
        msg = "The value PYMODELIO_MAIN must be defined in the file %s\n\n"
        log.exception(msg, USER_PROFILE_SETTINGS)
        sys.stderr.write(msg, USER_PROFILE_SETTINGS)
        raise
    else:
        log.info('  PYMODELIO_MAIN = %s', PYMODELIO_MAIN)


    # Here we are sure that PYMODELIO_MAIN is defined (or an exception was
    # raised).

    #--------------------------------------------------------------------------
    # Check that PYMODELIO_MAIN is a directory
    #--------------------------------------------------------------------------

    # Check if the variable PYMODELIO_MAIN is a valid path
    if not os.path.isdir(PYMODELIO_MAIN):
        log.error('  PYMODELIO_MAIN (%s) is not a directory', PYMODELIO_MAIN)
        msg = "In %s, PYMODELIO_MAIN is set to %s, but this is not a directory"
        current_value = PYMODELIO_MAIN  # keep it just to display it below
        del PYMODELIO_MAIN # Fundamental to force reload of settings later
        del pymodelioprofile.settings
        raise Exception( msg % (USER_PROFILE_SETTINGS ,current_value) )



    #--------------------------------------------------------------------------
    # Import the PyModelio environment and create it.
    #--------------------------------------------------------------------------
    framework_commons = os.path.join(PYMODELIO_MAIN,"commons")
    if framework_commons not in sys.path:
        # Add the directory containing the core of the PyModelio framework
        # to the python path

        sys.path.insert(0,framework_commons)
    log.debug('  sys.path = %s', sys.path)
    del framework_commons
    log.info('  importing  pymodelio.core.env')
    import pymodelio.core.env
    log.debug('  PyModelioEnv.start')
    pymodelio.core.env.PyModelioEnv.start()
    pymodelio.core.env.PyModelioEnv._setPythonInterpreterGlobalScope(globals())
    log.debug('  PyModelioEnv._setPythonInterpreterGlobalScope OK')
    pymodelio.core.env.PyModelioEnv._setPythonInterpreterGlobalSymbolsBefore(
        PYMODELIO_GLOBALS_SYMBOLS_BEFORE
    )
    del PYMODELIO_GLOBALS_SYMBOLS_BEFORE

    #--------------------------------------------------------------------------
    # Define global functions that will enable accessing modelio global
    # variable from modules at any time.
    #--------------------------------------------------------------------------

    if WITH_MODELIO:

        from pyalaocl import asSeq
        def getSelectedElements():
            global selectedElements
            return asSeq(selectedElements)
        pymodelio.core.env.PyModelioEnv.addGlobalFunction(getSelectedElements)

        def getModelingSession():
            global modelingSession
            return modelingSession
        pymodelio.core.env.PyModelioEnv.addGlobalFunction(getModelingSession)

        def getSelection():
            global selection
            return asSeq(selection)
        pymodelio.core.env.PyModelioEnv.addGlobalFunction(getModelingSession)


    #--------------------------------------------------------------------------
    # Import modules to inject code and for convenience in the python console
    #--------------------------------------------------------------------------

    log.info('  Importing modules')
    import pymodelio
    from pymodelio.core.env import PyModelioEnv
    # make pyalaocl features available at the top level
    from pyalaocl import *
    # install jython extensions. In particular instrument JDK collections.
    import pyalaocl.jython
    # install modelio extensions. In particular instrument modelio collections.
    from pyalaocl.modelio import *
    # install modelio extensions. In particular instrument modelio collections.
    from pyalaocl.modelio.profiles import *
    from pymodelio.modelio.simple import *

    pymodelio.core.env.PyModelioEnv._setPythonInterpreterGlobalSymbolsAfter(
        list(globals().keys()))

    PYMODELIO_INITIALIZED = True
    log.info( 'PyModelio environment successfully initialized' )
log.info('... PyModelio started')
