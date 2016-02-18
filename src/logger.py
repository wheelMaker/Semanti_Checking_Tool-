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
    _name = 'GCS_Checker.log'
    _log_instance = ''

    def __init__(self, log_path='~', log_level='ERROR', log_module='LOGGER'):
        self.set_level(log_level)
        self.set_module(log_module)
        self.set_path(log_path)
        self._log_instance = fIO.PyFileIO(self._name)
        print "creating log file ...", self._log_instance._file_name
        self._log_instance.open_file()

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
        return self._name

    def set_path(self, path='~'):
        pass

    def get_level(self):
        return self._log_level

    def get_module(self):
        return self._log_module

    def create_log_file(self):
        pass

    def log_exception(self, msg='', module_name=''):
        pass

