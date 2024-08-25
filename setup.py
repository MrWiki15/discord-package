# discord-package/setup.py
from setuptools import setup, find_packages

setup(
    name='discord-package',
    version='0.0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dcp=discord_package.cli:main',
        ],
    },
    install_requires=[
        'discord.py',  # Añade aquí cualquier otra dependencia necesaria
    ],
    description='Un empaquetador para crear bots de Discord fácilmente',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MrWiki15/discord-package',  # Cambia esto a la URL de tu repositorio
    author='Polaris Web3',
    author_email='universe@polarisweb3.org',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
