import os
import unittest
from pylint.testutils import make_tests, LintTestUsingFile, cb_test_gen, linter


HERE = os.path.dirname(os.path.abspath(__file__))


linter.load_plugin_modules(['pylint_factory'])


def tests(input_dir, messages_dir):
    callbacks = [cb_test_gen(LintTestUsingFile)]

    input_dir = os.path.join(HERE, input_dir)
    messages_dir = os.path.join(HERE, messages_dir)

    return make_tests(input_dir, messages_dir, None, callbacks)


def suite():
    test_list = tests('input', 'messages')

    return unittest.TestSuite([unittest.makeSuite(test, suiteClass=unittest.TestSuite)
                               for test in test_list])

if __name__=='__main__':
    unittest.main(defaultTest='suite')
