import venv, os
from presets import VIRTUALENV_DIR

def create_virtual_env(directory):
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(os.path.join(os.getcwd(), directory, VIRTUALENV_DIR))