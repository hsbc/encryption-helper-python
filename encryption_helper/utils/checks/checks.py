def str_none_or_empty(*argv):
    for arg in argv:
        if arg is None or len(arg.strip()) == 0:
            return True
    return False
