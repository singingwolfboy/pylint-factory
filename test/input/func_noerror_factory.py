"""
Checks that Pylint does not complain about a fairly standard factory
"""
import factory

class UserFactory(factory.Factory):
    class Meta:
        pass

    firstname = "John"
    lastname = "Doe"
