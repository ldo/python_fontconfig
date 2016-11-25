#+
# Distutils script to install python_fontconfig. Invoke from the command line
# in this directory as follows:
#
#     python3 setup.py build
#     sudo python3 setup.py install
#
# Written by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
#-

import distutils.core

distutils.core.setup \
  (
    name = "Fontconfig",
    version = "0.5",
    description =
        "language bindings for the Fontconfig font-matching library, for Python 3.4 or later",
    author = "Lawrence D'Oliveiro",
    author_email = "ldo@geek-central.gen.nz",
    url = "http://github.com/ldo/python_fontconfig",
    py_modules = ["fontconfig"],
  )
