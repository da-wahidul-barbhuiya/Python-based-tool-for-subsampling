from setuptools import setup,find_packages

setup(
    name='package',
    version='1.0',
    packages=['package'],
    entry_points={
        'console_scripts': [
            'subsample = package.subsample:main'
        ]
    }
)
