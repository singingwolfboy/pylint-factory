"""Augmentations."""
#  pylint: disable=invalid-name
from pylint.checkers.base import DocStringChecker
from pylint.checkers.design_analysis import MisdesignChecker
from pylint.checkers.classes import ClassChecker
from pylint.checkers.newstyle import NewStyleConflictChecker
from pylint_factory.compat import ClassDef
from pylint_factory.utils import node_is_subclass
from pylint.__pkginfo__ import numversion as PYLINT_VERSION
from pylint_plugin_utils import suppress_message


def is_model_meta_subclass(node):
    """Checks that node is derivative of Meta class."""
    if node.name != 'Meta' or not isinstance(node.parent, ClassDef):
        return False

    parents = (
        '.Factory',  # for the transformed version used here
        'factory.Factory',
    )
    import pdb; pdb.set_trace()
    result = node_is_subclass(node.parent, *parents)
    return result


def _visit_class(checker):
    return getattr(checker, 'visit_classdef' if PYLINT_VERSION >= (1, 5) else 'visit_class')


def _leave_class(checker):
    return getattr(checker, 'leave_classdef' if PYLINT_VERSION >= (1, 5) else 'leave_class')


def apply_augmentations(linter):
    """Apply augmentation and suppression rules."""
    suppress_message(linter, _visit_class(DocStringChecker), 'missing-docstring', is_model_meta_subclass)
    suppress_message(linter, _visit_class(NewStyleConflictChecker), 'old-style-class', is_model_meta_subclass)
    suppress_message(linter, _visit_class(ClassChecker), 'no-init', is_model_meta_subclass)
    suppress_message(linter, _leave_class(MisdesignChecker), 'too-few-public-methods', is_model_meta_subclass)
