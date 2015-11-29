from setuptools import setup

setup(
    name='str_prathibha',
    description='The Test Program',
    version='0.0.1',
    packages=['str_prathibha', 'strtest'],
    install_requires=[
        'django==1.4.18',
        'nose',
        'mock',
    ]
)
