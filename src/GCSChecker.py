import re
import GCSException as GE


class GCSChecker(object):

    current_file_name = ''
    current_line = 0
    checker_logger = None

    def __init__(self, cFName = '', clogger = None):

        self.checker_logger = clogger
        if not self.checker_logger:
            raise GE.GCSException("No proper logger initiated!!")
        self.current_file = cFName
        print "GCSChecker created!"

    # def lambda_check(self):


    @staticmethod
    def get_checker_type(code_file, report):
        res = re.search(r"\.\w*$", code_file[0])
        print res.group()


class RoGCSChecker(GCSChecker):
    def __init__(self):
        print "Robot GCS Checker created!"


class PyGCSChecker(GCSChecker):

    def __init__(self):
        print "Py GCS Checker created!"


code_types = {
    "py": PyGCSChecker,
    "robot": RoGCSChecker,
    }