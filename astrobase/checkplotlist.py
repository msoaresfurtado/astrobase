#!/usr/bin/env python
'''checkplotlist.py - Waqas Bhatti (wbhatti@astro.princeton.edu) - Dec 2016
License: MIT. See LICENSE for full text.

DESCRIPTION
===========

This makes a checkplot file list for use with the checkplot-viewer.html or the
checkplotserver.py webapps. Checkplots are quick-views of object info, finder
charts, light curves, phased light curves, and periodograms used to examine
their stellar variability. These are produced by several functions in the
astrobase.checkplot module:

checkplot.checkplot_png: makes a checkplot PNG for a single period-finding
                         method

checkplot.twolsp_checkplot_png: does the same for two independent period-finding
                                methods

checkplot.checkplot_pickle: makes a checkplot .pkl.gz for any number of
                            independent period-finding methods


USAGE
=====

If you made checkplots in the PNG format (checkplot-*.png)
----------------------------------------------------------

Copy this file along with checkplot-viewer.html and checkplot-viewer.js to the
base directory from where you intend to serve your checkplot images from. Then
invoke it from that directory like so:

$ python checkplotlist.py png subdir/containing/the/checkplots

This will generate a checkplot-filelist.json file containing the file paths to
the checkplots.

You can then run a temporary Python web server from this base directory to
browse through all the checkplots:

$ python -m SimpleHTTPServer # Python 2
$ python3 -m http.server     # Python 3

then browse to http://localhost:8000/checkplot-viewer.html.

If this directory is already in a path served by a web server, then you can just
browse to the checkplot-viewer.html file normally. Note that a file:/// URL
provided to the browser won't necessarily work in some browsers (especially
Google Chrome) because of security precautions.

If you made checkplots in the gzipped pickle format (checkplot-*.pkl.gz)
------------------------------------------------------------------------

Copy this file to where you put your checkplot gzipped pickles. Then invoke it
from that directory like so:

$ python checkplotlist.py pkl subdir/containing/the/checkplots

Then, from that directory, invoke the checkplotserver webapp (make sure the
astrobase virtualenv is active, so the command below is in your path):

$ checkplotserver [list of options, use --help to see these]

The webapp will start up a Tornado web server running on your computer and
listening on a local address (default: http://localhost:5225). This webapp will
read the checkplot-filelist.json file to find the checkplots.

Browse to http://localhost:5225 (or whatever port you set in checkplotserver
options) to look through or update all your checkplots. Any changes will be
written back to the checkplot .pkl.gz files, making this method of browsing more
suited to more serious variability search.

TL;DR
=====

python checkplotlist.py <pkl|png> <subdir/containing/the/checkplots/>

'''

import os
import os.path
import sys
import glob
try:
    import simplejson as json
except:
    import json

if __name__ == '__main__':

    if len(sys.argv) != 3:
        docstring = __doc__
        if docstring:
            print(docstring)
        else:
            print('Usage: %s <pkl|png> <subdir/containing/the/checkplots/> ' %
                  sys.argv[0])
        sys.exit(2)

    checkplotbasedir = sys.argv[2]

    if sys.argv[1] == 'pkl':
        checkplotglob = 'pkl.gz'
    elif sys.argv[1] == 'png':
        checkplotglob = 'png'
    else:
        print("unknown format for checkplots: %s! can't continue!"
              % sys.argv[1])
        sys.exit(1)


    currdir = os.getcwd()
    searchresults = glob.glob(os.path.join(checkplotbasedir,
                                           '*checkplot*.%s' % checkplotglob))

    if searchresults:

        print('found %s checkplot files in %s, '
              'making checkplot-filelist.json...' %
              (len(searchresults), checkplotbasedir))

        outjson = os.path.abspath(
            os.path.join(currdir,'checkplot-filelist.json')
        )

        with open(outjson,'w') as outfd:

            outdict = {'checkplots':sorted(searchresults),
                       'nfiles':len(searchresults)}
            json.dump(outdict,outfd)

        if os.path.exists(outjson):
            print('checkplot file list written to %s' % outjson)
        else:
            print('ERR! writing the checkplot file list failed!')

    else:

        print('ERR! no checkplots found in %s' % checkplotbasedir)