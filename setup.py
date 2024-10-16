from setuptools import setup, find_packages

setup(
    name="datawave",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'datawave=main:main',
        ],
    },
)
