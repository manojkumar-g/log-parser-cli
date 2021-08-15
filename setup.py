from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        return req.read().split('\n')


setup(
    name='log_parser',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        log_parser=log_parser.cli:cli
    '''
)
