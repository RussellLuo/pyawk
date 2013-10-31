#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Install or uninstall `pyawk`.

Usage:
    sudo python setup.py install
    sudo python setup.py uninstall
"""

import sys
import os

if not (len(sys.argv) == 2 and
        sys.argv[1] in ('install', 'uninstall')):
    sys.stderr.write(__doc__)
    sys.exit(1)

if sys.argv[1] == 'install':
    cmd = 'chmod +x pyawk &&' + \
          'cp pyawk /usr/bin'
else: # uninstall
    cmd = 'rm /usr/bin/pyawk'

os.system(cmd)
