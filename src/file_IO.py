#!/usr/bin/python

import logger

_file_io_logger = logger.Logger(log_level='ERROR', log_module='FILEIO')


class FileIOException(Exception):
    def __init__(self, msg=""):
        _file_io_logger.log_exception(msg, module_name='FILEIO')


class PyFileIO(object):
    _file = ''

    def __init__(self, file_name=''):
        if '' == file_name:
            raise FileIOException('File name is null!!!')
        _file = file_name

    def open_file(self, file_name='', mode='r'):
        pass

    def close_file(self, file_name=''):
        pass
