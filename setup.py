from setuptools import setup

setup(
    name='pqcli',
    version='0.1.2',
    py_modules=['pqcli_main',
                'util',
                'test_pqcli_main',
                'test_util'],
    install_requires=[
        'Click',
    ],
    package_data={'':[
                        'config_test.json',
                        'LICENSE.md',
                        'README.md',
                        'requirements.txt',
                        'config.json',
                    ]},
    entry_points='''
        [console_scripts]
        pqcli=pqcli_main:pqcli
    ''',
)