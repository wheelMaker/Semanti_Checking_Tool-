import googleStyler


def deco_styler_line_by_line(func):
    def wrapper():
        googleStyler.GoogleStyler.__line_nu = 1
        func()
        googleStyler.GoogleStyler.__line_nu = 1
    return wrapper()