from setuptools import setup, find_packages

setup(
    name="git-branch-manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-branch-manager=gitutils.main:main',  # Adjusted to the new package structure
        ],
    },
)