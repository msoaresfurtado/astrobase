#!/usr/bin/env python

'''checkplotserver_handlers.py - Waqas Bhatti (wbhatti@astro.princeton.edu) -
                                 Jan 2017

These are Tornado handlers for serving checkplots and operating on them.

'''

####################
## SYSTEM IMPORTS ##
####################

import os
import os.path
import gzip
try:
    import cPickle as pickle
except:
    import pickle
import base64
import hashlib
import logging
from datetime import time

try:
    import simplejson as json
except:
    import json

# get a logger
LOGGER = logging.getLogger(__name__)

#####################
## TORNADO IMPORTS ##
#####################

import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.escape import xhtml_escape, xhtml_unescape, url_unescape

###################
## LOCAL IMPORTS ##
###################

from .checkplot import checkplot_pickle_update, checkplot_pickle_to_png, \
    _read_checkplot_picklefile, _base64_to_file

# FIXME: import these for updating plots due to user input
# from .checkplot import _pkl_finder_objectinfo, _pkl_periodogram, \
#     _pkl_magseries_plot, _pkl_phased_magseries_plot,
# from .periodbase import pgen_lsp, aov_periodfind, \
#     stellingwerf_pdm, bls_parallel_pfind


#######################
## UTILITY FUNCTIONS ##
#######################




#####################
## HANDLER CLASSES ##
#####################


class IndexHandler(tornado.web.RequestHandler):
    '''This handles the index page.

    This page shows the current project, saved projects, and allows people to
    load, save, and delete these projects. The project database is a json file
    stored in $MODULEPATH/data. If a checkplotlist is provided, then we jump
    straight into the current project view.

    '''

    def initialize(self, currentdir, assetpath, allprojects,
                   cplist, cplistfile):
        '''
        handles initial setup.

        '''

        self.currentdir = currentdir
        self.assetpath = assetpath
        self.allprojects = allprojects
        self.currentproject = cplist
        self.cplistfile = cplistfile

        LOGGER.info('working in directory %s' % self.currentdir)
        LOGGER.info('working on checkplot list file %s' % self.cplistfile)



    def get(self):
        '''
        This handles GET requests to the index page.

        '''

        # generate the project's list of checkplots
        project_checkplots = sorted(self.currentproject['checkplots'])

        self.render('cpindex.html',
                    project_checkplots=project_checkplots)





class CheckplotHandler(tornado.web.RequestHandler):
    '''This handles loading and saving checkplots.

    This includes GET requests to get to and load a specific checkplot pickle
    file and POST requests to save the checkplot changes back to the file.

    '''

    def initialize(self, currentdir, assetpath, allprojects,
                   cplist, cplistfile):
        '''
        handles initial setup.

        '''

        self.currentdir = currentdir
        self.assetpath = assetpath
        self.allprojects = allprojects
        self.currentproject = cplist
        self.cplistfile = cplistfile

        LOGGER.info('working in directory %s' % self.currentdir)
        LOGGER.info('working on checkplot list file %s' % self.cplistfile)



    def get(self, checkplotfname):
        '''This handles GET requests.

        This is an AJAX endpoint; returns JSON that gets converted by the
        frontend into things to render.

        '''

        LOGGER.info('provided checkplotfname = %s' % checkplotfname)

        if checkplotfname:

            # do the usual safing
            self.checkplotfname = xhtml_escape(
                base64.b64decode(checkplotfname)
            )

            LOGGER.info('actual checkplot filename: %s' % self.checkplotfname)

            # see if this plot is in the current project
            if self.checkplotfname in self.currentproject['checkplots']:

                LOGGER.info('found %s in current list' % self.checkplotfname)

                # make sure this file exists
                cpfpath = os.path.join(
                    os.path.abspath(os.path.dirname(self.cplistfile)),
                    self.checkplotfname
                )

                LOGGER.info('trying to load %s' % cpfpath)

                if not os.path.exists(cpfpath):

                    msg = "couldn't find checkplot %s" % cpfpath
                    LOGGER.error(msg)
                    resultdict = {'status':'error',
                                  'message':msg,
                                  'result':None}
                    self.write(resultdict)


                # load it if it does exist
                LOGGER.info('reading %s' % cpfpath)
                cpdict = _read_checkplot_picklefile(cpfpath)

                # break out the initial info
                objectid = cpdict['objectid']
                objectinfo = cpdict['objectinfo']
                varinfo = cpdict['varinfo']

                # these are base64 which can be provided directly to JS to
                # generate images (neat!)
                finderchart = cpdict['finderchart'].decode()
                magseries = cpdict['magseries']['plot'].decode()

                cpstatus = cpdict['status']

                resultdict = {
                    'status':'ok',
                    'message':'found checkplot %s' % self.checkplotfname,
                    'result':{'objectid':objectid,
                              'objectinfo':objectinfo,
                              'varinfo':varinfo,
                              'finderchart':finderchart,
                              'magseries':magseries,
                              'cpstatus':cpstatus}
                }

                # now get the other stuff
                for key in ('pdm','aov','bls','gls','sls'):

                    if key in cpdict:
                        resultdict['result'][key] = {
                            'nbestperiods':cpdict[key]['nbestperiods'],
                            'periodogram':cpdict[key]['periodogram'].decode(),
                            'bestperiod':cpdict[key]['bestperiod'],
                            'phasedlc0':{
                                'plot':cpdict[key][0]['plot'].decode(),
                                'period':float(cpdict[key][0]['period']),
                                'epoch':float(cpdict[key][0]['epoch'])
                            },
                            'phasedlc1':{
                                'plot':cpdict[key][1]['plot'].decode(),
                                'period':float(cpdict[key][1]['period']),
                                'epoch':float(cpdict[key][1]['epoch'])
                            },
                            'phasedlc2':{
                                'plot':cpdict[key][2]['plot'].decode(),
                                'period':float(cpdict[key][2]['period']),
                                'epoch':float(cpdict[key][2]['epoch'])
                            },
                        }

                # return this via JSON
                self.write(resultdict)

            else:

                LOGGER.error('could not find %s' % self.checkplotfname)

                resultdict = {'status':'error',
                              'message':"This checkplot doesn't exist.",
                              'result':None}
                self.write(resultdict)


        else:

            resultdict = {'status':'error',
                          'message':'No checkplot provided to load.',
                          'result':None}

            self.write(resultdict)



    def post(self):
        '''
        This handles POST requests.

        Also an AJAX endpoint.

        '''


class OperationsHandler(tornado.web.RequestHandler):
    '''This handles operations for checkplot stuff.

    This includes GET requests to get the components (finder, objectinfo,
    varinfo, magseries plots, for each lspinfo: periodogram + best phased
    magseries plots).

    Also includes POST requests to redo any of these components (e.g. redo a
    phased mag series plot using twice or half the current period).

    '''

    def initialize(self, currentdir, assetpath, allprojects,
                   cplist, cplistfile):
        '''
        handles initial setup.

        '''

        self.currentdir = currentdir
        self.assetpath = assetpath
        self.allprojects = allprojects
        self.currentproject = cplist
        self.cplistfile = cplistfile

        LOGGER.info('working in directory %s' % self.currentdir)
        LOGGER.info('working on checkplot list file %s' % self.cplistfile)



    def get(self):
        '''
        This handles GET requests.

        '''



    def post(self):
        '''
        This handles POST requests.

        '''