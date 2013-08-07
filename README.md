*Radar Tools* is a set of libraries and scripts useful for visualizing and
processing data collected from ice-penetrating radar. The tools have been
designed to work the HDF5 datasets generated by [Blue
System](http://www.radar.bluesystem.ca/) IceRadar.

There are two primary ways of using *Radar Tools*. The first is to use the
command-line and graphical tools, listed below. These tools provide an
efficient and simple way to apply established methodologies for analysing radar
data. Pre-written filters and processing routines are called by typing
commands.

![](http://njwilson23.github.com/radar_tools/images/repo_image.png)

The second way is to use the ``irlib`` API directly. This makes it possible to
programmatically analyze radar data from the Python programming language. New
filters and processing routines can be implemented using the API.

There is experimental support for reading other types of datasets using
*Radar Tools*. Right now, it's possible to read CReSIS lines, which makes the
filters in `irlib` available. An example of a helper function to load CReSIS
\*.mat files is in ``itools.py``

Graphical tools:
----------------

- **icepick2**: View radar lines directly and experiment interactively with
  processing filters. Pick reflection arrivals from a radar line, either
  manually or with simple pattern recognition

- **icerate**: Rate reflection quality using **icepick** output

- **irview**: General purpose viewer for radar lines that doubles as a tool for
  marking englacial regions **[DEPRECATED]**

Command-line tools:
-------------------

- **h5_dumpmeta**: Dump metadata from an HDF5 survey into a CSV file
- **h5_add_utm**: Add UTM coordinates to an HDF5 survey file (requires
  [**pyproj**](http://code.google.com/p/pyproj/))
- **h5_replace_gps**: Replace the coordinates in an HDF5 survey with those from
  a GPS eXchange (GPX) file
- **h5_generate_cache**: Generate caches to speed loading radar lines
- **h52a**: Export a line from an HDF5 file to ASCII or binary
- **irtrace**: Plot a radar trace acquired at a single location
- **irline**: Plot a radar section along a line of locations

Dependencies:
-------------

*Radar Tools* should run anywhere Python and the required dependencies work. In
the past, I've managed to get it working under Windows, OS X, and Linux.

1. [*Python*](http://www.python.org) 2.6+ (&lt;3.x): dynamic interpretted
programming language suited for scientific computing

2. [*Numpy*](http://www.scipy.org) numerical array classes for Python

2. [*Scipy*](http://www.scipy.org) science-oriented libraries for Python

2. [*matplotlib*](http://www.matplotlib.org) plotting for Python

2. [*h5py*](https://github.com/h5py/h5py): HDF5 interface for Python

One way to get the first four dependencies above in one package is to install
the [Enthought Python Distribution](http://www.enthought.com/).

Additional useful packages and tools:
-------------------------------------

1. [*Cython*](cython.org) for generating accelerated filters (cython.org)

2. *pywavelet* wrapper for wavelet algorithms (*Torrence and Compo, 1998*)
(included in `external/pywavelet-0.1`)

2. [*pyproj*](code.google.com/p/pyproj) _libproj_ bindings

Documentation:
--------------

In addition to the basic information here, documentation can be found in `doc`.
In order to build the documentation, [Sphinx](http://sphinx-doc.org/) must be
installed, with the ``numpydoc`` extension. The extensions can be installed by

    easy_install numpydoc

Then, type

    make html

If LaTeX is available, the documentation can be compiled into a PDF. Type

    make latexpdf


Changes in irlib version 0.4-dev
--------------------------------

*irlib* 0.4 represents significant refactoring and cleaning of both the library
and application design. Breaking changes in the final version will be kept to a
minimum, however the *stable-0.3* branch is available if necessary.

- remove deprecated `CutSingle`, `CutRegion` methods
- refactor pickable gathers into separate subclasses
- map window
- refactor icepick, irview, icerate into a single codebase, kept in `irlib/app/`
  (all except icerate)
- build *icepick2* based on the refactored `app` codebase
- modular command system, one of the benefits of which is that additional custom
  filters can be added easily at runtime and on a project-basis
- rewrite h5_replace_gps to be more robust, handle timezones, and work over
  multiple days
- some bug fixes and polishing
- project config file (not complete)
- composable line gathers and surveys by overloading arithmetic operators?
- HDF file write?
- PulseEkko data reader?



License:
--------

*Radar Tools* is provided "as is," without any warranty. Some parts of
*Radar Tools* are affected by different licensing terms. See `license.txt` for
detailed information.

