try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The Damn Setup',
    'author': 'Surajit Kar',
    'url': 'http://www.surajitsprojectskeleton.com',
    'authors_email': 'skar-2274@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'Surajit\'s First Project Skeleton'
}

setup(**config)
