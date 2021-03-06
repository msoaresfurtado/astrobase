# v0.2.7

## Fixes

- checkplot: use axes_grid1 because axes_grid is deprecated apparently
- features.all_nonperiodic_features: add back magsarefluxes kwarg
- lcmath: add (optional for now) iterative sigclip to sigclip_magseries
- lcmodels.eclipses: fixes to docstring
- lcmodels.eclipses, lcfit: implemented invgauss_eclipses model & fit fns
- lcproc.plot_variability_thresholds: yscale -> log
- lcproc: stetson_threshold -> variability_threshold, now per mag-bin
- lcproc: stupid bug fix
- lcproc.variability_threshold: get and plot LC RMS as well
- recoverysim: added make_fakelc_collection
- recoverysim: fixed up make_fakelc, make_fakelc_collection
- recoverysim: now two separate modules: fakelcgen and fakelcrecovery
- varbase.features: some more measures added
- varbase.lcfit: fix confusing fourierorder, fourierparams kwargs. GH PR #27
- varbase.signals: fixes for GH PR #25 and #29
- varbase/signals: fix long-broken gls_prewhiten iterative prewhiten function
- checkplot.twolsp_checkplot.png: Wrapped LOGWARNING in `if verbose:` statement


## Work that may be in progress

- [WIP] moved various LC models into lcmodels, TODO: finish these
- [WIP] recoverysim: redo make_fakelc, now gets mag-rms from previous results
- [WIP] setting up the varclass package
- [WIP] various implementation notes
- [WIP] working on recoverysim

# v0.2.6

## Fixes

- lcfit: fix error handling
- lcfit: implement traptransit_fit_magseries, to be tested
- lcfit: tested/fixed traptransit_fit_magseries, seems to work OK
- lcfit.traptransit_fit_magseries: get formal 1-sig errs for final params
- lcfit.traptransit_fit_magseries: get formal 1-sig errs for fit as well
- lcproc/checkplot: use full lcfpath in makelclist, getlclist, nbr procs
- lcproc, features: fix broken beyond1std, add bestmagcol to results
- lcproc.makelclist: add maxlcs kwarg
- lcproc.makelclist: fixing bugs
- lcproc, periodbase: update period-finder registry dicts
- periodbase: fix falsealarmprob for PDM
- periodbase.make_combined_periodogram: addmethods kwarg
- README: added zenodo DOI badge
- smav: bump up default nharmonics to 6 from 4
- smav: use correct dot product function (np.vdot not np.dot)

# v0.2.5

## Fixes

- checkplot: add neighbor stuff to checkplot png as well
- checkplot.checkplot_pickle_to_png: actually fix mistaken pkl outfile ext
- checkplot: fix handling of no neighbors case
- checkplot: get neighbors of target, their radecs, xys, and lcfpaths
- checkplotlist: added some TODOs for multi-checkplot-per-object stuff
- checkplotlist: more notes on planned features
- finally added coding: utf-8 to everything
- glsp: remove because all moved to zgls.py
- lcmath: added a fill_magseries_gaps function
- lcmath, autocorr: add some guards against weirdness
- lcmath.fill_magseries_gaps: fix normalization of fluxes
- lcmath.fill_magseries_gaps: use 0.0 to fill gaps instead of noiselevel by default
- lcmath.fill_magseries_gaps: use scipy's perfectly cromulent mode fn
- lcmath.fill_magseries_gaps: use scipy's perfectly cromulent mode fn instead
- lcproc: added update_checkplotdict_nbrlcs to get neighbor LCs
- lcproc: add neighbor stuff to parallel_cp workers and driver
- lcproc: add serial_varfeatures
- lcproc: better kwargs for xmatchexternal
- lcproc: fix default fileglobs for HAT and HPX LCs
- lcproc.makelclist: do concurrent (threaded) info collection instead
- lcproc.makelclist: do parallel info collection instead
- lcproc.makelclist: get actual ndets per magnitude column
- lcproc.makelclist: remove useless fileglob from tasklist
- lcproc.parallel_cp_lcdir: make output directory if it's doesn't exist
- lcproc.parallel_varfeatures: use ProcessPoolExecutor instead of mp.Pool
- lcproc.runpf: bugfix
- lcproc.runpf: make BLS SNR optional because it takes forever
- lcproc.runpf/runcp: allow any of the period-finders from periodbase
- lcproc: simplify parallel task list for makelclist
- macf: added macf_period_find; seems to work, TODO: more testing
- macf: added plot_acf_results to see smoothed/unsmoothed ACF and peaks
- macf: fixed, tested; reproduces McQuillian+ (2014) results on KeplerLCs
- macf: fix handling of kwargs
- macf: fix peak detection
- macf: search interval for ACF peaks now depends on smoothing
- macf: some more docstring work
- macf: update docstrings
- periodbase: add a make_combined_periodogram fn
- periodbase: add macf to base namespace
- periodbase.macf: initial bits for McQuillian+ (2013a, 2014) period-finder
- plotbase: get the FITS header for the cutout for WCS purposes later
- README: updated for some new stuff
- README, various: add links to ADS for period-finders, fix spelling of names
- smav: bugs fixed, seems to be working OK
- smav: implemented aovhm_periodfind, to be tested
- smav: initial bits
- smav: some more progress
- varbase.autocorr: actually return acf as np.array
- varbase.autocorr: autocorr_magseries fn using lcmath.fill_magseries_gaps
- varbase.autocorr: fix _autocorr_func3 and set as default
- varbase.autocorr: return acf as np.array
- varbase.autocorr: use 0.0 to fill gaps instead of noiselevel by default
- varbase.features: fix annoyingly subtle bug causing np.polyfit crashes
- varbase.features: np.nonzero -> npnonzero
- zgls, lcfit: guard against zero errors here too
- zgls: move the glsp functions into here

# v0.2.4

## Fixes

- lcproc: add external cross-matching to getlclist
- lcproc.getlclist: also copy matching light curves to requested dir
- lcproc: getlclist, makelclist now have column-filtering and cone-search

# v0.2.3

## Fixes

- lcproc: don't crash runpf if BLS SNR fails

# v0.2.2

## Fixes

- cplist: add 'ne' -> not-equal-to filter operator for --filter arg
- cplist/cpserver: now takes multiple filters to be ANDed together; yet to test
- cplist: fix docstring
- cplist: fixed multiple filter keyword arguments
- cplist: fix incorrect filtering
- cplist: fixing multiple filter args

# v0.2.0

## Fixes

- checkplot: add check for overwritten pkl when converting to png
- checkplot: added kwarg for findercachedir to checkplot fns
- checkplot: added verbose kwarg
- checkplot: add in extra BLS info if available
- checkplot: add in markeredgewidth for older matplotlibs
- checkplot: astroquery_skyview_stamp -> internal_skyview_stamp
- checkplot: calculate varfeatures, add other keys required by cpserver tools
- checkplot.checkplot_pickle: can now overplot external LC fit fn
- checkplot: direct return mode for _pkl_phased_magseries_plot
- checkplot: docstring fixes
- checkplot: handle case of no explicitly provided lspmethod
- checkplotlist: added chunked output if too many checkplots
- checkplotlist: add optional prefixes to output JSON filelists
- checkplotlist: auto-add output JSON prefix if sortby is provided
- checkplotlist: better messaging if more than 1 output JSON
- checkplotlist: can now index into arrays when sorting on cpd properties
- checkplotlist: can now specify sortkey/sortorder when making the pkl list
- checkplotlist: faster custom sorting with mp.Pool
- checkplotlist: fix docstring
- checkplotlist: guard against missing sortkey items
- checkplotlist: remove non-finite vals from filters
- checkplotlist: use argparse instead of hacked together cmdline parsing
- checkplot: make varfeatures optional
- checkplot, plotbase: astroquery_skyview_stamp -> skyview_stamp
- checkplot: pyplot.scatter -> pyplot.plot for speed, also use rasterized=True
- checkplot: return lcfit per phased LC, not just the last one
- checkplot: slightly smaller marker size for binned mag series
- checkplot: turn off bestperiodhighlight by default
- checkplot.twolsp_checkplot_png: don't break if bestperiodhighlight is None
- cplist: added filtering options for checkplotserver input JSON
- cplist: fix incorrect filtering because we didn't take sort order into account
- cpserver: add check for checkplot-filelist-00.json as default
- cpserver: added sortorder/sortkey UI elem in sidebar list
- cpserver/cplist: add support for filtered list JSONs
- cpserver: enable gzip
- cpserver.js: fix case where observing stations aren't strings
- cpserver: slightly better display of sortkey/sortorder
- cpserver: turn off cplist sorting since checkplotlist handles it
- cpserver UI: add a filter control to the reviewed checkplot sidebar list
- cpserver UI: disable bokeh; will use server-side plotting for now
- hplc: added HPX binned LC reader functions
- hplc: added parallel LC concatenator
- hplc: added pklc_fovcatalog_objectinfo to fill in objectinfo
- hplc: fix station names
- hplc: use gzipped fovcatalogs if available
- imageutils: added frame_radecbox_to_jpeg function
- imageutils: handle weird input better
- imageutils: various fixes
- kbls: add alternate SNR calculation
- kbls: add support for max number of frequencies to search
- kbls: don't crash if spline fit to find a minimum fails
- lcfit: fourier_fit_magseries now accepts fourierorder as a scalar
- lcfit: initfourierparams -> fourierparams
- lcfit.spline_fit...: maxknots reduced to 30 for better min-finding
- lcmath.time_bin_magseries_with_errs: return jdbins as array
- lcproc: add a LC binning function
- lcproc: added maxobjects to be processed per driver invocation
- lcproc: added pf driver for all LC formats
- lcproc: adding makelclist
- lcproc: adding support for multiple lc types
- lcproc: add overrideable time, mag, err cols for all function drivers
- lcproc: add parallel LC binning functions
- lcproc: add register func for custom LC format
- lcproc: also get objects above stetson threshold across all magcols
- lcproc: bugfixes
- lcproc/checkplot: add in BLS snr if available
- lcproc: dereference columns for different lctypes correctly
- lcproc: fix bug where bls result was replaced instead of updated
- lcproc: more bug fixes
- lcproc: more fixes
- lcproc: use last deferenced mcol val to correctly process astrokep lcs
- plotbase: added internal_skyview_stamp fn to remove astroquery dep
- plotbase: plot the binned plot over the unbinned one
- plotbase.skyview_stamp: add provenance, use sha256 instead of md5
- signals: fix mask_signal
- signals: more fixes
- signals: return a BytesIO/StringIO object as fitplotfile if provided
- signals: whiten_magseries now accepts fourierorder as a scalar
- varbase.lcfit: added verbose kwarg
- varbase.signals: fix gls_prewhiten
- varbase.signals: fix various horrendous problems in prewhiten_magseries


## Work that may be in progress

- [WIP] added lcproc.py to drive large HAT LC processing jobs
- [WIP] cpserver: added some TODOs
- [WIP] cpserver, checkplot: some plot fixes
- [WIP] cpserver: continuing work
- [WIP] cpserver: finishing up backend work, to be tested
- [WIP] cpserver: fix async err handling, some lctools now working
- [WIP] cpserver: fixed various lctool bugs after testing
- [WIP] cpserver: fix parsing of argument types
- [WIP] cpserver: fix saving to tempfpath, fix circular ref in var-varfeatures
- [WIP] cpserver: implemented lctools: phasedlc-newplot, var-varfeatures
- [WIP] cpserver.js: added skeleton for cptools
- [WIP] cpserver lctools: added a reset function and a lcfit subtract function
- [WIP] cpserver: more fixes
- [WIP] cpserver: more work on UI
- [WIP] cpserver: screenshot updated with near-final UI for v0.2
- [WIP] cpserver: some notes for stuff
- [WIP] cpserver: still WIP
- [WIP] cpserver: still working on LC tools backend
- [WIP] cpserver UI: added period-search, variability-tools, lcfit tabs
- [WIP] cpserver UI: added some phased LC plot options
- [WIP] cpserver UI: adding controls to JS, working on periodsearch
- [WIP] cpserver UI: phasedlc-newplot, var-varfeatures, work queues
- [WIP] cpserver UI: still working on JS for lctools
- [WIP] cpserver UI: various CSS fixes
- [WIP] cpserver: various fixes to JSON decoding and checkplot loading
- [WIP] cpserver: various fixes to UI
- [WIP] cpserver: various UI fixes
- [WIP] cpserver: working on hooking up signal and fitting functions
- [WIP] cpserver: working on LC tools handlers
- [WIP] cpserver: write tool results to temp pkl, keep orig pkl load fast
- [WIP] lcfit: add a simple trapezoid function for eclipses

# v0.1.22

## Fixes

- checkplot.checkplot_pickle_to_png: fix breakage if pickle has no objectinfo

# v0.1.21

## Fixes

- astrokep: add onormalize kwarg to read and consolidate MASTLC fns
- astrokep: add recursive kwarg for glob
- astrokep.consolidate_kepler_fitslc: use recursive glob for speed if Py>3.5
- astrokep: docstring fixes
- astrokep: trying fnmatch
- astrokep: trying recursive glob
- astrokep: use fnmatch instead of glob
- checkplotlist: appending bugs fixed
- checkplotlist: append to an existing list JSON if it exists
- checkplot: make sure it still works with matplotlib < v2.0.0
- checkplot: try hard to get an objectid out of the input kwargs
- hatlc: added normalization fns to docstring, more fixes for sqlitecurve compression
- hatlc: added OS independent sqlite.gz read/write
- hatlc: first crack at normalizing by instrument properties
- hatlc: keep the input sqlitecurves until done with (de)compression
- hatlc: make less talkative
- hatlc: normalize_lcdict_byinst function sort of working
- hatlc.normalize_lcdict_byinst: more fixes
- hatlc.normalize_lcdict_instruments: fixing bugs
- hatlc: warning if gzip < 1.6
- hatpilc: add column defs to lcdict
- hatpilc: added concatenation and pickle writing
- hatpilc: added concat rollup fn
- hatpilc: add recursive kwarg for glob
- hatpilc: bug fixing
- hatpilc.concatenate...: use recursive glob on Py3.5+ for speed
- hatpilc: improved a bit
- hatpilc: make a bit more organized
- hatpilc: reorganization
- hatpilc: use empty ndarrays if no dets
- hplc: added normalization across light curves
- hplc: added pklc reader, breaking out framekeys to elems
- hplc: addeed non-recursive LC search mode
- hplc: concatenation: fix lc index
- hplc: concatenation: fix recursive search to include only specific postfixed files
- hplc: fix docstrings
- hplc: fixing normalization
- hplc: fixing pklc output
- hplc: more fixes for non-recursive LC search
- hplc: return a normalized LC even if there's only one to return
- hplc: sort concatenated light curves by time
- __init__: add a __version__
- varbase.features: added a roll-up function

# v0.1.20

## Fixes

- astrokep: making read_kepler_fitslc work with K2 LCs
- astrokep: more fixes for K2 LC reading
- kbls.bls_snr: add check for rare case when minepoch is an array
- README.md: added k2hat.py and expanded some descriptions
- README.md: some more fixes
- setup.py: require astropy>=1.3 and numpy>=1.4

# v0.1.19

## Fixes

- astrokep: added appendto mode to read_kepler_fitslc
- astrokep: better naming scheme for output pickles
- astrokep.filter_kepler_lcdict: fix timestoignore for new lcdict format
- astrokep: fixing appendto mode
- astrokep: fixing consolidate_kepler_fitslc
- astrokep: implemented consolidate_kepler_fitslc, will test soon
- astrokep: make sklearn dependency optional
- astrokep: pickle export now uses HIGHEST_PROTOCOL, docstring fixes
- astrokep: stitch_lightcurve -> stitch_kepler_lcdict (TBD)

# v0.1.18

## Fixes

- checkplot: added minbinelems kwarg
- varbase/features: implemented CDPP as in Gilliland+ 2011

# v0.1.15

## Fixes

- checkplot: added checkplot_pickle_to_png
- checkplot: added externalplots kwarg to checkplot_pickle
- checkplot: add missing finderconvolve kwarg to [twolsp_]checkplot_png fn
- checkplot: fix extrarows functionality in checkplot_pickle_to_png
- checkplot: parse the variable flag correctly for PNG export
- checkplot_pickle_to_png: fix extra row handling
- checkplot_pickle_to_png: fix extra row handling again
- checkplotserver: some style improvements to PNG export UI
- lcmath: fixed import for datetime
- notebooks: updated lightcurves-and-checkplots for latest checkplot version

# v0.1.13

## Fixes

- checkplot.checkplot_pickle_update: fixed some python 3 vs 2.7 breakage
- checkplotserver: fixed up readonly mode
- cpserver.js: moved readonly alert to end of load cycle
- README.md: add fancy test status icons
- tests: added a case for checkplot_pickle_update

# v0.1.12

## Fixes

- .gitignore: ignore test results
- MANIFEST.in: include tests
- setup.py: fixed testing imports and launch
- test_endtoend.py: fixed various things
- test_endtoend: updated test procedure docstring
- tests: added test_endtoend.py

# v0.1.10

## Fixes

- kbls.py: added bootstrap false-alarm probability and an SNR calculation
- periodbase.bootstrap_falsealarmprob: get kwargs from lspdict
- periodbase: return a dict of results instead
- periodbase: return bootstrap trial values for diagnostics, etc.

# v0.1.9

## Fixes

- checkplot: fix issue with pickles breaking if times, mags, errs are astropy.table.Column objects

# v0.1.8

## Fixes

- periodbase: handle cases where there are no finite periodogram values

# v0.1.7

## Fixes

- checkplot: better random objectid generation
- checkplot: fixed some docstrings

# 0.1.6

## Fixes

- checkplot: handle a missing objectid in checkplot_pickle
- checkplotserver: adding skeletons for LC tool handling endpoints
- timeutils: added jd_to_datetime fn (w/ optional ISO str output)
