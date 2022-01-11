"""
xmobar_wttr - tests.utils_test

@author: phdenzel

Test-driven development mantra: Guilty until proven innocent!
"""
import os
import xmobar_wttr.constants as xwc
import xmobar_wttr.utils as xwu
from tests.prototype import UnitTestPrototype
from tests.prototype import SequentialTestLoader


class UtilsModuleTest(UnitTestPrototype):

    def setUp(self):
        # arguments and keywords
        print("")
        print(self.separator)
        print(self.shortDescription())

    def tearDown(self):
        print("")

    def test_get_parmap(self):
        """ # xmobar_wttr.utils.get_parmap """
        parmap = xwu.get_parmap()
        self.printf(None)
        self.assertIsInstance(parmap, dict)
        for k in parmap:
            self.assertTrue('hdr' in parmap[k])
            self.assertTrue('units' in parmap[k])
            self.assertTrue('map' in parmap[k])
        self.assertTrue(parmap, xwc.default_parmap)
        self.printout(parmap)

    # def test_update_parmap(self):
    #     """ #xmobar_wttr.utils.update_parmap """
    #     pass
        


if __name__ == "__main__":
    loader = SequentialTestLoader()
    loader.proto_load(UtilsModuleTest)
    loader.run_suites()
