"""
    logger ut file
"""

__auther__ = 'wyatt wang'


import logger
import os
import file_IO as fIO

default_log_file = "GCS_Checker.log"


# case 1 for logger __init__ function

def tc_logger_init():
    print "Logger ut case 1 for __init__ function..."
    if os.path.isfile(default_log_file):
        os.remove(default_log_file)
    logger_instance = logger.Logger(log_path=os.getcwd())
    if os.path.isfile(logger_instance.get_name()):
        print "logger level is: ", logger_instance.get_level()
        print "logger module is: ", logger_instance.get_module()
        logger_instance.close_log_instance_file()
        os.remove(logger_instance.get_name())
    else:
        raise fIO.FileIOException("open file error!")

# case 2 for log format


def tc_gcs_log_format():
    print "Logger ut case 2 for log format..."
    fmt = logger.GCSLogFormat()

tc_gcs_log_format()
tc_logger_init()
