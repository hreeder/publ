from distutils.core import setup

setup(
    name='publ',
    version='0.1',
    packages=[''],
    url='http://harryreeder.co.uk/',
    license='MIT',
    author='Harry Reeder',
    author_email='harry@harryreeder.co.uk',
    description='Command line micropub client',
    entry_points={
        'console_scripts': [
            'publ = publ:main'
        ]
    }
)
