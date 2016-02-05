#!/usr/bin/python

import logger

_file_io_logger = logger.Logger(log_level='ERROR', log_module='FILEIO')


class FileIOException(Exception):
    def __init__(self, msg=""):
        _file_io_logger.log_exception(msg, module_name='FILEIO')


class PyFileIO(object):
    _file_name = ''
    _file = ''

    def __init__(self, file_name=''):
        if '' == file_name:
            raise FileIOException('File name is null!!!')
        _file_name = file_name

    def open_file(self, file_name='', mode='r'):
        self._file = open(self._file_name, mode)
        print 'wpf'
        print self.file

    def close_file(self):
        self._file.close()
