"""
xmobar_wttr - tests.prototype

@author: phdenzel

Test-driven development mantra: Guilty until proven innocent!
"""
import unittest
import logging
import pprint


class UnitTestPrototype(unittest.TestCase):
    OKAY = u'\033[92m'+u'\u2713'+u'\x1b[0m'
    FAIL = u'\033[91m'+u'\u2717'+u'\x1b[0m'
    top_separator = "="*80
    separator = "-"*80
    prefix = "<"*3
    logging.basicConfig(
        level=logging.INFO,
        format='{prefix} %(message)s'.format(prefix=prefix))

    @classmethod
    def setUpClass(cls):
        classname = cls.__name__.replace("Test", "").upper()
        test_descr = "# " + classname
        test_intro = "\n".join([cls.top_separator, test_descr, cls.separator])
        print("")
        print(test_intro)

    @classmethod
    def tearDownClass(cls):
        classname = cls.__name__.replace("Test", "").upper()
        test_descr = "# " + "End test of " + classname
        test_intro = "\n".join([cls.top_separator, test_descr, cls.separator])
        print("")
        print(test_intro)

    @classmethod
    def main(cls, **kwargs):
        v = kwargs.pop('verbosity', 1)
        unittest.main(verbosity=v, **kwargs)

    @staticmethod
    def printf(arg):
        msg = pprint.pformat(arg)
        for line in msg.splitlines():
            logging.info(line.rstrip())

    @staticmethod
    def printout(arg):
        msg = pprint.pformat(arg)
        for line in msg.splitlines():
            print(line.rstrip())

    


class SequentialTestLoader(unittest.TestLoader):
    def __init__(self):
        super(SequentialTestLoader, self).__init__()
        self.suites = []

    def getTestCaseNames(self, testCaseClass):
        test_names = super(SequentialTestLoader, self).getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names

    def proto_load(self, testcase):
        tests = self.loadTestsFromTestCase(testcase)
        self.suites.append(tests)

    def run_suites(self, verbosity=1):
        suite = unittest.TestSuite(self.suites)
        unittest.TextTestRunner(verbosity=verbosity).run(suite)
