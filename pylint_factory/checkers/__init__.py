"""Checkers."""
from pylint_factory.checkers.factory_installed import FactoryBoyInstalledChecker


def register_checkers(linter):
    """Register checkers."""
    linter.register_checker(FactoryBoyInstalledChecker(linter))
