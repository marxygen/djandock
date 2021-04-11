import os

def create_directory(dir):
    try:
        os.mkdir(dir)
    except OSError:
        raise