import argparse
from datetime import datetime as dt
from misc import create_directory
from virtenv import create_virtual_env
from add_git import initialize_repo
from django_proj import create_django_project
from docker_files import wrap

if __name__ != '__main__':
    print('This file is to be executed directly')
    raise SystemExit

parser = argparse.ArgumentParser(description="Creates a Django project with virtual environment, Git repository and Docker container")
parser.add_argument('name', type=str, help="Name of your project")
parser.add_argument('-r', '--repository', type=str, help="Link to the repository")
args = parser.parse_args()

print(f'[{dt.now()}] Initializing "{args.name}"...')
create_directory(args.name) # Create directory
print('\tProject folder created')
create_virtual_env(args.name) # Create a virtual environment in this directory
print('\tVirtual environment created')
create_django_project(args.name)
print('\tDjango project created')
wrap(args.name) # Create Dockerfile and docker-compose.yml file
print('\tWrapped in Docker')
# if args.repository:
#     initialize_repo(args.repository)
#     print('Git repository initialized')




