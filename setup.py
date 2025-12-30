from setuptools import setup

setup(
    name='pew',
    version='0.1.0',
    description='Pew CLI tool',
    py_modules=['pew'],
    entry_points={
        'console_scripts': [
            'pew=pew:main',
        ],
    },
    python_requires='>=3.6',
)
