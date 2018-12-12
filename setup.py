from setuptools import setup

from pytreelib import __version__


def read(file_name):
    with open(file_name) as f:
        return f.read()

setup(name='pytreelib',
      version=__version__,
      description='Simple Binary Tree Data Structure Implementation',
      url='https://github.com/akashbw/pytreelib',
      author='Akash Jain',
      author_email='akashjain0108@gmail.com',
      long_description=read('readme.rst')+read('updates.rst'),
      license='MIT',
      packages=['pytreelib'],
      keywords=['data structure', 'tree', 'binary tree'],
      zip_safe=False)
