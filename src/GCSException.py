#!/usr/bin/python


class GCSException(Exception):
    _error_message = ''

    def __init__(self, msg=""):
        self._error_message = msg
        print self._error_message
