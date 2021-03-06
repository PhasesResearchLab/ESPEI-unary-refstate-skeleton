from setuptools import setup
import os

NAME = 'CustomRefstate2020'

def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=f'espei_refstate_{NAME}'.lower(),
    version='0.1',
    author='<Your name>',
    author_email='you@example.com',
    url='https://your-refstate.example.com',
    description='A reference state plugin for ESPEI',
    license='MIT',
    py_modules=['refstate'],
    long_description=readme('README.md'),
    entry_points={'espei.reference_states': f'{NAME} = refstate'}
)
