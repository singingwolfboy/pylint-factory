"""Transforms."""
import os
import re
from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes



def _add_transform(package_name, *class_names):
    """Transform package's classes."""
    transforms_dir = os.path.join(os.path.dirname(__file__), 'transforms')
    fake_module_path = os.path.join(transforms_dir, '%s.py' % re.sub(r'\.', '_', package_name))

    with open(fake_module_path) as modulefile:
        fake_module = modulefile.read()

    fake = AstroidBuilder(MANAGER).string_build(fake_module)

    def set_fake_locals(module):
        """Set fake locals for package."""
        if module.name != package_name:
            return
        for class_name in class_names:
            # This changed from locals to _locals between astroid 1.3 and 1.4
            if hasattr(module, '_locals'):
                module._locals[class_name].extend(fake._locals[class_name])  # pylint: disable=protected-access
            else:
                module.locals[class_name].extend(fake.locals[class_name])

    MANAGER.register_transform(nodes.Module, set_fake_locals)


_add_transform('factory', 'Factory')
