#!/usr/bin/env python
"""
xmobar_wttr - test

@author: phdenzel
"""
import xmobar_wttr
from tests.prototype import SequentialTestLoader
from tests.utils_test import UtilsModuleTest


def main():

    loader = SequentialTestLoader()

    loader.proto_load(UtilsModuleTest)

    loader.run_suites(verbosity=1)


if __name__ == "__main__":

    main()

    
