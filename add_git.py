import os
from git import Repo

def initialize_repo(remote_url):
    """
    Initializes an empty repository in the provided folder
    """
    empty_repo = git.Repo.init(os.path.join(os.getcwd(), 'empty'))
    origin = empty_repo.create_remote('origin', remote_url)
    assert origin.exists()