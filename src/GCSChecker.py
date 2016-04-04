import re
import GCSException as GE
import googleStyler


class GCSChecker(object):

    current_file_name = []
    current_file_content = ''
    code_files = []
    checker_logger = None
    styler = None

    def __init__(self, cfiles=[], clogger=None):

        self.checker_logger = clogger
        if not self.checker_logger:
            raise GE.GCSException("No proper logger initiated!!")
        self.code_files = cfiles
        if not self.code_files:
            raise GE.GCSException("No code file to be checked!!")
        self.styler = googleStyler.GoogleStyler()
        self.checker_logger.info(self.styler.functions())
        self.checker_logger.info("GCSChecker created!")

    @staticmethod
    def get_checker_type(code_file, report):
        res = re.search(r"\.\w*$", code_file[0])
        print res.group()

    def check(self):

        '''
        This function actually does the real GCS check.
        Now for the first release, simple check on the code files would be implemented.
        It means:
            1. No file content pre-checking
            2. Load whole file content into the memory
            3. Init only one thread(process) for it.
            4. Only implement the most basic google stylers, code checking will be line by line.
            5. Any checking mechanism re-factory should be within this method.

        For the very start version, code will be really stupid.
        I feel sad for this...
        '''

        for code in self.code_files:
            self.current_file_name = code
            self.checker_logger.info('File in checking: ' + self.current_file_name)
            self.styler.run_stylers()


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

if __name__ == "__main__":
    c = GCSChecker()
    c.check()
