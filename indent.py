def indentation(string, indent, count):
    """Indents a string.

    Keyword arguments:
    string -- The string you want to indent.
    indent -- The string to use for the indent.
    count -- How many times you want indent repeated.
    """
    # Type check for string and indent
    if type(string) is not str or type(indent) is not str:
        raise TypeError("Should be string")
    else:
        pass
    # Type check for count
    if type(count) is not int:
        raise TypeError("count should be Integer")
    else:
        pass
    if count == 0:
        return string


print(indentation('Uni\nRain', 'd', 0))
