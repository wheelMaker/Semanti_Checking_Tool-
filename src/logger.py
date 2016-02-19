""" logger class APIs

    Methods:
        Logger.__init__():
        Logger.set_level():
        Logger.set_module():
        Logger.get_level():
        Logger.get_module():
        ...
"""

__auther__ = 'wyatt wang'

import logging
import file_IO as fIO
import os


class LoggerException(Exception):
    _error_message = ''

    def __init__(self, msg='', module_name='LOGGER'):
        self._error_message = msg
        print self._error_message


FORMAT = "[%(asctime)s] - %(name)s - %(levelname)s: %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"


class GCSLogFormat(logging.Formatter):
    def __init__(self, fmt=FORMAT, dfmt=DATEFMT):
        logging.Formatter.__init__(self, fmt, dfmt)
        print self._fmt + '  wpf'

    def set_format(self):
        pass

    def set_date_format(self):
        pass


class Logger(object):
    _types_log_level = ["DEBUG", "INFO", "ALARM", "ERROR"]
    _types_log_module = ["LOGGER", "FILEIO", "GCSCHECKER", "WEBGUI"]
    _log_level = ''
    _log_module = ''
    _log_path = ''
    _log_name = ''
    _log_instance = ''

    def __init__(self, log_name='GCS_Checker.log', log_path='~', log_level='ERROR', log_module='LOGGER'):
        self.set_log_file_name(log_name)
        self.set_level(log_level)
        self.set_module(log_module)
        self.set_path(log_path)
        self._log_instance = fIO.FileIO(self._log_name)
        os.chdir(self._log_path)
        print "creating log file ...", self._log_instance.get_file_name()
        self._log_instance.open_file(mode='w+')

    def set_log_file_name(self, name):
        if '' == name:
            raise LoggerException("null log file name, quit!")
        else:
            self._log_name = name

    def set_level(self, level='DEBUG'):
        if level in self._types_log_level:
            self._log_level = level
            return self._log_level
        else:
            return LoggerException('Wrong log level!!!')

    def set_module(self, module='LOGGER'):
        if module in self._types_log_module:
            self._log_module = module
            return self._log_module
        else:
            return LoggerException('Wrong log module!!!')

    def get_name(self):
        return self._log_name

    def set_path(self, path='~'):
        if '' == path:
            path = os.getcwd()
            print "Try to set log path to null!!! Change it to working dir: ", path
            self._log_path = path
        else:
            print "Setting path to: ", path
            self._log_path = path

    def get_level(self):
        return self._log_level

    def get_module(self):
        return self._log_module

    def create_log_file(self):
        pass

    def log_exception(self, msg='', module_name=''):
        pass

