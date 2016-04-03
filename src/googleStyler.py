class GoogleStyler(object):

    __selections = []
    __file = ''
    __functions = []

    def __init__(self, file_name='', styler_selections=[]):

        if not styler_selections:
            pass
        else:
            self.__selections = styler_selections
            self.__file = file_name

    def __call__(self, *args, **kwargs):
        pass

    def get_all_styler_functions(self):
        func_list = dir(GoogleStyler)
        self.__functions = func_list
        print func_list

    def styler_single_line_max_characters(self):
        max_characters = 80
        pass
