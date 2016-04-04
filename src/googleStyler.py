'''
Each styler in this class means a checking rule for GCS.
Styler function must start with string "styler_" and end with its functionality
GCSChecker.check will invoke this class' stylers one by one for every single source file.
'''

import re


class GoogleStyler(object):

    __selections = []
    __file = ''
    __functions = []

    def __init__(self, styler_selections=[]):
        # currently, all sylers selected and no parameter needed in this func
        # self.__selections = styler_selections
        self.find_all_styler_functions()

    def __call__(self, *args, **kwargs):
        pass

    def functions(self):
        return self.__functions

    def find_all_styler_functions(self):
        func_list = dir(GoogleStyler)
        for f in func_list:
            if re.search("^styler_", f) is not None:
                self.__functions.append(f)

    def run_stylers(self):
        for f in self.functions():
            getattr(self, f)()

    def styler_single_line_max_characters(self):
        max_characters = 80
        print "haha"
        pass
