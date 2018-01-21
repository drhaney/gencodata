REQUIRES
========

- Python 2.7 or later
- pip installation utility



Gencodata may be installed on a Linux system from either the **wheel**
file or the **.tar.gz** archive::

    gencodata-0.1.dev1-py2.py3-none-any.whl
    gencodata-0.1.dev1.tar.gz

The wheel distribution file is installed locally with the commands::

    cd location_of_gencodata_wheel_file
    pip2 install --user gencodata-0.1.dev1-py2.py3-none-any.whl


Installing from tar.gz archive file requires that you decompress it
and enter the new directory::

    tar xzf gencodata-0.1.dev1.tar.gz
    cd gencodata-0.1.dev1

then::

    pip2 install --user .
 or
    python2 setup.py install


**Comments:**

- pip requires the wheel package's full name.

- many installations default to a version 2.x PYTHONPATH.  

- pip2 installs the module in a Python2 site-package directory.

- The --user flag performs a local installation without needing root privileges.

- The local destination directory is typically::

    /$HOME/     (i.e., /home/username)
      .local/
	lib/
	  python2.7/
	    site-packages/
	      gencodata/

! If your system uses Python3.x by default and you anticipate no problems,
! use pip or python without the '2' postpended.

----------


Copyright 2017, Daniel R. Haney

