import re
import GCSException as GE
import googleStyler


class GCSChecker(object):

    current_file_name = []
    code_files = []
    checker_logger = None
    styler = googleStyler.GoogleStyler()

    def __init__(self, cfiles=[], clogger=None):

        self.checker_logger = clogger
        if not self.checker_logger:
            raise GE.GCSException("No proper logger initiated!!")
        self.code_files = cfiles
        if not self.code_files:
            raise GE.GCSException("No code file to be checked!!")
        print "GCSChecker created!"

    @staticmethod
    def get_checker_type(code_file, report):
        res = re.search(r"\.\w*$", code_file[0])
        print res.group()

    def check(self):
        for code in self.code_files:
            self.current_file_name = code
            self.checker_logger.info('File in checking: ' + self.current_file_name)
            # self.styler(self.current_file_name)
        pass


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