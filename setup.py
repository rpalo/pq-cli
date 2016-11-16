from setuptools import setup

setup(
    name='pqcli',
    version='0.1',
    py_modules=['pqcli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pqcli=pqcli:pqcli
    ''',
)