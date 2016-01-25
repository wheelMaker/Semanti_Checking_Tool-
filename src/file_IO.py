#!/usr/bin/python

_logger

class FileIOException(Exception):
    def __init__(self, msg=""):
        logger.exception(msg)

class FileIO(object):
    def __init__(self, file_name = ''):
        if ''==file_name:
            raise FileIOException()