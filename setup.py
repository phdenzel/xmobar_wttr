import os
from setuptools import setup
from setuptools import find_packages

ld = {}
if os.path.exists("README.md"):
    ld['filename'] = "README.md"
    ld['content_type'] = "text/markdown"
elif os.path.exists("readme_src.org"):
    ld['filename'] = "readme_src.org"
    ld['content_type'] = "text/plain"

with open(file=ld['filename'], mode="r") as readme_f:
    ld['data'] = readme_f.read()

setup(
    # Metadata
    name="xmobar_wttr",
    author="Philipp Denzel",
    author_email="phdenzel@gmail.com",
    version="0.0.dev1",
    description=("An external xmobar plugin for customizable weather info!"),
    long_description=ld['data'],
    long_description_content_type=ld['content_type'],
    license='GNU General Public License v3.0',
    url="https://github.com/phdenzel/xmobar_wttr",
    # keywords="",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # Package
    install_requires=['requests', 'pyyaml'],
    package_dir={"": "xmobar_wttr"},
    packages=find_packages(where='xmobar_wttr'),
    py_modules=['xmobar_wttr'],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'xmobar_wttr = xmobar_wttr.__main__:main',
        ],
    },

)