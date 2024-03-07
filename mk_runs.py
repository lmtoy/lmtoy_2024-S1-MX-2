#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-2"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["G358"] = [ 112139,112292, 112296,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['G358']   = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['G358']   = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
