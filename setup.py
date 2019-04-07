from setuptools import setup

setup(
    name='screenshot',
    version='0.1.0',
    description='A Python 2 terminal app that takes screenshots of all eligible pages of a website.',
    author='Joseph Bernadas',
    author_email='jb@webdesign8.com',
    packages=['screenshot'],
    install_requires=['Util', 'PIL', 'Selenium', 'ChromeDriver']
)