from setuptools import find_packages, setup
import pkutils
import pathlib
import os
root = pathlib.Path(__file__).parent
os.chdir(str(root))

tag_name = os.environ.get('GITHUB_REF', '')

def get_version(tag_name):
    version = tag_name.replace('refs/tags/v', '')
    return version

setup(
    name='salary_prediction',
    packages=find_packages(include=['salary_prediction']),
    version=get_version(tag_name),
    # version='0.2.1',
    description='Feature salary prediction',
    author='sai keerthi',
    license='MIT',
    install_requires=list(pkutils.parse_requirements('requirements.txt')),
    # To be added when tests are implemented
    #setup_requires=['pytest-runner'],
    #tests_require=['pytest==4.4.1'],
    #test_suite='tests',
)