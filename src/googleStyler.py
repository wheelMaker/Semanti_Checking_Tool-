'''
Each styler in this class means a checking rule for GCS.
Styler function must start with string "styler_" and end with its functionality
GCSChecker.check() will invoke this class' stylers one by one for every single source file.
'''

import re


class GoogleStyler(object):

    __selections = []
    __functions = []
    __result = ''
    __report = None
    __content = ''
    __code = ''

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
        self.__content = content
        self.__code = self.__content.split('\n')
        for f in self.functions():
            getattr(self, f)()

    # def styler_single_line(self):
    #     line_number = 1
    #     for string in self.__code:
    #         l = len(string)
    #         if l > max_characters:
    #             output = 'GCS Error exceed max characters ' + str(max_characters) + \
    #                      ' in line ' + str(line_number) + ' ' + str(l) + '\n'
    #             self.__result += output
    #         line_number += 1
    #     self.__report.write_to_file(self.__result)
    #     self.__result = ''

    def styler_single_line_max_characters(self):
        max_characters = 80
        line_number = 1
        for string in self.__code:
            l = len(string)
            if l > max_characters:
                output = 'GCS Error exceed max characters ' + str(max_characters) + \
                         ' in line ' + str(line_number) + ' ' + str(l) + '\n'
                self.__result += output
            line_number += 1
        self.__report.write_to_file(self.__result)
        self.__result = ''

    def styler_exception_format(self):
        # 1. exception with no description string
        # 2. exception with 2 argutments
        # 3. raise a string based exception "raise 'too long !!!'"
        # 4. never catch all kinds of exceptions
        # 5. use finally clause to do something after the exception
        # 6. when catching an exception, use as rather than a comma
        tmp_code = (self.__content.replace('\\\n', ' ')).split('\n')
        for string in tmp_code:
            if -1 == string.rfind('raise'):
                print 'oh yeah!'
            else:
                pass
            # line_number += 1
        # self.__report.write_to_file(self.__result)
        # self.__result = ''
        # pass

