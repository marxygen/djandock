import os

def create_directory(dir, raiseFileExists=False):
    try:
        os.mkdir(dir)
    except FileExistsError:
        if raiseFileExists:
            raise
    except OSError:
        raise