#!/usr/bin/python

import logger

_file_io_logger = logger.Logger(log_level='ERROR', log_module='FILEIO')


class FileIOException(Exception):
    _error_message = ''
    def __init__(self, msg=""):
        self._error_message = msg
        print self._error_message
        #_file_io_logger.log_exception(msg, module_name='FILEIO')


class PyFileIO(object):
    _file_name = ''
    _file = ''
    _mode = 'r'

    def __init__(self, file_name=''):
        if '' == file_name:
            raise FileIOException('File name is null!!!')
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def set_file_name(self, file_name):
        if '' == file_name:
            raise FileIOException('File name is null!!!')
        else:
            self._file_name = file_name

    def open_file(self, mode='r'):
        self._mode = mode
        self._file = open(self._file_name, self._mode)

    def close_file(self):
        self._file.close()
