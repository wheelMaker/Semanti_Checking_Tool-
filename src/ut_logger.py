"""
    logger ut file
"""

__auther__ = 'wyatt wang'

import logger
import os
import file_IO as fIO

default_log_file = "GCS_Checker.log"

# case 1 for logger __init__ function

print "Logger ut case 1 for __init__ function..."
if os.path.isfile(default_log_file):
    os.remove(default_log_file)
logger_instance = logger.Logger()
if os.path.isfile(logger_instance.get_name()):
    pass
else:
    raise fIO.FileIOException("open file error!")
print "logger level is: ", logger_instance.get_level()
print "logger module is: ", logger_instance.get_module()

os.remove(default_log_file)