from __future__ import absolute_import
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint_factory.__pkginfo__ import BASE_ID


class FactoryBoyInstalledChecker(BaseChecker):
    name = 'factory-installed-checker'

    msgs = {
        'F%s01' % BASE_ID: ("Factory Boy is not available on the PYTHONPATH",
                            'factory-not-available',
                            "Factory Boy could not be imported by the pylint-factory plugin, so most Factory Boy related "
                            "improvements to pylint will fail."),

        'W%s99' % BASE_ID: ('Placeholder message to prevent disabling of checker',
                            'factory-not-available-placeholder',
                            'PyLint does not recognise checkers as being enabled unless they have at least'
                            ' one message which is not fatal...')
    }

    @check_messages('factory-not-available')
    def close(self):
        try:
            import factory
        except ImportError:
            self.add_message('F%s01' % BASE_ID)
