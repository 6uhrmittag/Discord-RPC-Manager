from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name="MultiPresenceManager",
    version="1.0.0",
    description="A modular presence manager for multiple applications",
    author="Mari",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'multipresence=presences.unity_presence:main',
        ],
    },
)
