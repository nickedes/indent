def indentation(string, indent, count=1):
    """Indents a string.

    Keyword arguments:
    string -- The string you want to indent.
    indent -- The string to use for the indent.
    count -- How many times you want indent repeated.
    """
    # Type check for string and indent
    if type(string) is not str or type(indent) is not str:
        raise TypeError("Should be string")
    # Type check for count
    if type(count) is not int or count is None:
        raise TypeError("count should be Integer")
    if count == 0:
        return string

    splitted = string.split('\n')
    for i in range(len(splitted)):
        splitted[i] = count*indent + splitted[i]

    return '\n'.join(splitted)
