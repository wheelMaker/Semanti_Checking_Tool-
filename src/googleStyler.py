class GoogleStyler(object):

    __selections = []

    def __init__(self, file='', styler_selections=[]):

        if not styler_selections:
            pass
        else:
            self.__selections = styler_selections

    def styler_single_line_max_characters(self):
        max_characters = 80
        pass
