#! /usr/bin/env python
#
#   h52a - export a line from HDF5 to an ASCII (or binary) file
#
#
#

import sys, getopt, os.path, StringIO
from irlib import ExtractLine
import pdb

def print_syntax():
    print """
    SYNTAX: h52a infile Nline|all [options] > file

    h52a - export a line from HDF5 to an ASCII (or binary) file

        Instead of Nline, all may be specified to extract all lines.
        In this case, [-f] is assumed.

    Options:
        -b          write to binary instead (32-bit float)
        -f          automatically name the output file
        --clobber   overwrite existing files
    """

def arr2ascii(f, arr):
    """ Write a numpy array arr as an ascii grid to file f. """
    for row in arr:
        f.write(str(row).strip('[').strip(']').replace('\n','') + '\n')

optlist, args = getopt.gnu_getopt(sys.argv[1:], 'bf', ['clobber'])
optdict = dict(optlist)

# Test the syntax - display error if it doesn't make sense
if len(args) != 2:
    print_syntax()
    sys.exit(1)
else:
    infile = args[0]
    line = int(args[1])

try:
    line_data = ExtractLine(infile, line)
except:
    sys.stderr.write("h52a: error extracting line data\n")
    sys.exit(1)

# Determine the proper dilimiter for ASCII vs binary output
if '-b' in optdict.keys():
    sep = ''
    optdict['-f'] = ''
    fext = '.bin'
else:
    sep = '\t'
    fext = '.txt'

# Write to a file or to stdout
if '-f' in optdict.keys():
    outfile = infile.rsplit('.',1)[0] + '_line{0}{1}'.format(line, fext)
    if not os.path.isfile(outfile):
        with open(outfile, 'w') as f:
            if sep != '':
                arr2ascii(f, line_data)
            else:
                line_data.tofile(f)

    else:
        if '--clobber' in dict(optlist).keys():
            with open(outfile, 'w') as f:
                if sep != '':
                    arr2ascii(f, line_data)
                else:
                    line_data.tofile(f)
        else:
            sys.stderr.write("h52a: {fnm} already exists\n".format(
                    fnm=os.path.basename(outfile)))
else:
    sys.stderr.write("h52a: for now this only works with the -f tag.\n")
