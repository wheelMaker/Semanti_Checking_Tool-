import re


class GCSChecker(object):

    def __init__(self):
        print "GCSChecker created!"

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