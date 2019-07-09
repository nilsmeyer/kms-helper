from setuptools import setup

setup(
    name='kms-helper',
    author='Nils Meyer',
    author_email='nils@nm.cx',
    description='Quickly decrypt / encrypt values from KMS',
    version='0.1',
    py_modules=['kms_helper'],
    install_requires=[
        'Click', 'boto3'
    ],
    entry_points='''
        [console_scripts]
        kms-helper=kms_helper:cli
    ''',
)
