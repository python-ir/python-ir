#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import sys
import sys_shelve_importer
import os
import pkgutil

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(sys_shelve_importer.ShelveFinder)
sys.path.insert(0, filename)

import package

readme_path = os.path.join(package.__path__[0], 'README')

#readme = package.__loader__.get_data(readme_path)
readme = pkgutil.get_data('package', 'README')
print readme

foo_path = os.path.join(package.__path__[0], 'foo')
#foo = package.__loader__.get_data(foo_path)
foo = pkgutil.get_data('package', 'foo')
print foo
