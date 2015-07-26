def indentation(string, indent):
    """Indent a string.

    Keyword arguments:
    string -- The string you want to indent.
    indent -- The string to use for the indent.
    """
    if type(string) is str and type(indent) is str:
        pass
    else:
        raise TypeError("Should be string")
