# discord-package/setup.py
from setuptools import setup, find_packages

setup(
    name='discord-package',
    version='0.0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dcp=discord_package.cli:main',
        ],
    },
    install_requires=[
        'discord.py',
        'watchdog',
        'asyncio',
        'datetime',
        'requests',
        'rich',
    ],
    description='A packager to create Discord bots easily',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MrWiki15/discord-package', 
    author='Polaris Web3',
    author_email='universe@polarisweb3.org',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
