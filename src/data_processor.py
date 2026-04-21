def load_file(path):
    # Missing try-except in case of error
    f = open(path, 'r')
    return f.read()
