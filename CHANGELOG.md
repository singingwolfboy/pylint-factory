# Changelog

## Version 0.7.3


## Version 0.7.2
* [#76](https://github.com/landscapeio/pylint-django/pull/76) Better handling of mongoengine querysetmanager
* [#73](https://github.com/landscapeio/pylint-django/pull/73) (#72)[https://github.com/landscapeio/pylint-django/issues/72] Make package zip safe to help fix some path problems
* [#68](https://github.com/landscapeio/pylint-django/pull/68) Suppressed invalid constant warning for "app_name" in urls.py
* [#67](https://github.com/landscapeio/pylint-django/pull/67) Fix view.args and view.kwargs
* [#66](https://github.com/landscapeio/pylint-django/issues/66) accessing _meta no longer causes a protected-access warning as this is a public API as of Django 1.8
* [#65](https://github.com/landscapeio/pylint-django/pull/65) Add support of mongoengine module.
* [#59](https://github.com/landscapeio/pylint-django/pull/59) Silence old-style-class for widget Meta

## Version 0.7.1
* [#52](https://github.com/landscapeio/pylint-django/issues/52) - Fixed stupid mistake when using versioninfo

## Version 0.7
* [#51](https://github.com/landscapeio/pylint-django/issues/51) - Fixed compatibility with pylint 1.5 / astroid 1.4.1

## Version 0.6.1
* [#43](https://github.com/landscapeio/pylint-django/issues/43) - Foreign key ID access (`somefk_id`) does not raise an 'attribute not found' warning
* [#31](https://github.com/landscapeio/pylint-django/issues/31) - Support for custom model managers (thanks [smirolo](https://github.com/smirolo))
* [#48](https://github.com/landscapeio/pylint-django/pull/48) - Added support for django-restframework (thanks [mbertolacci](https://github.com/mbertolacci))

## Version 0.6
* Pylint 1.4 dropped support for Python 2.6, therefore a constraint is added that pylint-django will only work with Python2.6 if pylint<=1.3 is installed
* [#40](https://github.com/landscapeio/pylint-django/issues/40) - pylint 1.4 warned about View and Model classes not having enough public methods; this is suppressed
* [#37](https://github.com/landscapeio/pylint-django/issues/37) - fixed an infinite loop when using astroid 1.3.3+
* [#36](https://github.com/landscapeio/pylint-django/issues/36) - no longer warning about lack of `__unicode__` method on abstract model classes
* [PR #34](https://github.com/landscapeio/pylint-django/pull/34) - prevent warning about use of `super()` on ModelManager classes

## Version 0.5.5
* [PR #27](https://github.com/landscapeio/pylint-django/pull/27) - better `ForeignKey` transforms, which now work when of the form `othermodule.ModelClass`. This also fixes a problem where an inferred type would be `_Yes` and pylint would fail
* [PR #28](https://github.com/landscapeio/pylint-django/pull/28) - better knowledge of `ManyToManyField` classes

## Version 0.5.4
* Improved resiliance to inference failure when Django types cannot be inferred (which can happen if Django is not on the system path

## Version 0.5.3
* [Issue #25](https://github.com/landscapeio/pylint-django/issues/25) Fixing cases where a module defines `get` as a method

## Version 0.5.2
* Fixed a problem where type inference could get into an infinite loop

## Version 0.5.1

* Removed usage of a Django object, as importing it caused Django to try to configure itself and thus throw an ImproperlyConfigured exception.

## Version 0.5

* [Issue #7](https://github.com/landscapeio/pylint-django/issues/7)
Improved handling of Django model fields
* [Issue #10](https://github.com/landscapeio/pylint-django/issues/10)
No warning about missing __unicode__ if the Django python3/2 compatability tools are used
* [Issue #11](https://github.com/landscapeio/pylint-django/issues/11)
Improved handling of Django form fields
* [Issue #12](https://github.com/landscapeio/pylint-django/issues/12)
Improved handling of Django ImageField and FileField objects
* [Issue #14](https://github.com/landscapeio/pylint-django/issues/14)
Models which do not define __unicode__ but whose parents do now have a new error (W5103)
instead of incorrectly warning about no __unicode__ being present.
* [Issue #21](https://github.com/landscapeio/pylint-django/issues/21)
`ForeignKey` and `OneToOneField` fields on models are replaced with instance of the type
they refer to in the AST, which allows pylint to generate correct warnings about attributes
they may or may not have.


## Version 0.3

#### New Features

* Python3 is now supported

#### Bugfixes

* `__unicode__` warning on models does not appear in Python3


## Version 0.2

#### New Features

* Pylint now recognises `BaseForm` as an ancestor of `Form` and subclasses
* Improved `Form` support

#### Bugfixes

* [Issue #2](https://github.com/landscapeio/pylint-django/issues/2) - a subclass of a `Model` or `Form` also has
warnings about a `Meta` class suppressed.
* [Issue #3](https://github.com/landscapeio/pylint-django/issues/3) - `Form` and `ModelForm` subclasses no longer
warn about `Meta` classes.
