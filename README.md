pylint-factory
=============

[![Build Status](https://travis-ci.org/singingwolfboy/pylint-factory.svg?branch=master)](https://travis-ci.org/singingwolfboy/pylint-factory)
[![Coverage Status](https://coveralls.io/repos/singingwolfboy/pylint-factory/badge.svg)](https://coveralls.io/r/singingwolfboy/pylint-factory)

NOTE: THIS IS NOT WORKING YET

# About

`pylint-factory` is a [Pylint](http://pylint.org) plugin for improving code analysis for when analysing code using Factory Boy. The code is based on [`pylint-django`](https://github.com/landscapeio/pylint-django).

## Usage

#### Pylint

Ensure `pylint-factory` is installed and on your path (`pip install pylint-factory`), and then run pylint:

```
pylint --load-plugins pylint_factory [..other options..]
```

# Features

* `Meta` informational classes on factories do not generate errors.


# License

`pylint-factory` is available under the MIT license.
