'''
Each styler in this class means a checking rule for GCS.
Styler function must start with string "styler_" and end with its functionality
GCSChecker.check() will invoke this class' stylers one by one for every single source file.
Decorator should be added for all stylers!
'''

import re


class GoogleStyler(object):

    __selections = []
    __functions = []
    __result = ''
    __report = None

    def __init__(self, styler_selections=[], report=None):
        # currently, all sylers selected and no parameter needed in this func
        # self.__selections = styler_selections
        self.find_all_styler_functions()
        self.__report = report

    def __call__(self, *args, **kwargs):
        pass

    def functions(self):
        return self.__functions

    def find_all_styler_functions(self):
        func_list = dir(GoogleStyler)
        for f in func_list:
            if re.search("^styler_", f) is not None:
                self.__functions.append(f)

    def run_stylers(self, content):
        for f in self.functions():
            getattr(self, f)(content)

    def styler_single_line_max_characters(self, content=''):
        code = content.split('\n')
        max_characters = 80
        line_number = 1
        for string in code:
            l = len(string)
            if l > max_characters:
                output = 'GCS Error exceed max characters ' + str(max_characters) + \
                         ' in line ' + str(line_number) + ' ' + str(l) + '\n'
                self.__result += output
            line_number += 1
        self.__report.write_to_file(self.__result)
        self.__result = ''

