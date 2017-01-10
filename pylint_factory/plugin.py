from pylint_factory.checkers import register_checkers
from pylint_factory.augmentations import apply_augmentations

# we want to import the transforms to make sure they get added to the astroid manager,
# however we don't actually access them directly, so we'll disable the warning
#from pylint_factory import transforms  # pylint:disable=W0611


def register(linter):
    """Registering additional checkers."""
    # add all of the checkers
    register_checkers(linter)
    # register any checking fiddlers
    apply_augmentations(linter)
