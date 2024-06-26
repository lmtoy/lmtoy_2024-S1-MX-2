#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-2"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["G1.7+3.7-234_01_of_04"] =  [ 117345,]

on["G1.7+3.7-234_02_of_04"] =  [ 117349,]

on["G1.7+3.7-234_03_of_04"] =  [ 112524,]

on["G1.7+3.7-234_04_of_04"] =  [ 112532,]


on["G358.7+3.7+179_01_of_04"] =  [ 112139, 112292, 112296,]

on["G358.7+3.7+179_02_of_04"] =  [ 112518, 112788, 117039,]

on["G358.7+3.7+179_03_of_04"] =  [ 113027, 113137, 117043,]

on["G358.7+3.7+179_04_of_04"] =  [ 113029, 113139, 117047,]

#on["G1-mos"]  
on["G358-mos"] = on["G358.7+3.7+179_01_of_04"] + on["G358.7+3.7+179_02_of_04"] + on["G358.7+3.7+179_03_of_04"] + on["G358.7+3.7+179_04_of_04"]



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
#pars1["G1.7+3.7-234_03_of_04"]   = "pix_list=-13,14,15 extent=500 b_order=1 dv=20 dw=20"
#pars1["G1.7+3.7-234_04_of_04"]   = "pix_list=-13,14,15 extent=500 b_order=1 dv=20 dw=20"
# M Heyer  04/17./2024 -- vlsr =179 and pix_list=-13  (not 13,14,15)  dv=20 dw=50
pars1["G358.7+3.7+179_01_of_04"] = "pix_list=-13 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_02_of_04"] = "pix_list=-13 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_03_of_04"] = "pix_list=-13 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_04_of_04"] = "pix_list=-13 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358-mos"] = "pix_list=-13 extent=500 b_order=1 dv=20 dw=50 vlsr=179"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
#pars2["G1.7+3.7-234_03_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
#pars2["G1.7+3.7-234_04_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
#pars2["G358.7+3.7+179_01_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13 vlsr=179"
#pars2["G358.7+3.7+179_02_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13 vlsr=179"
#pars2["G358.7+3.7+179_03_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13 vlsr=179"
#pars2["G358.7+3.7+179_04_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13 vlsr=179"
#pars2["G358-mos"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13 vlsr=179"

pars3 = {}
#pars3["G1.7+3.7-234_03_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
#pars3["G1.7+3.7-234_04_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G358.7+3.7+179_01_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15 vlsr=179"
pars3["G358.7+3.7+179_02_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15 vlsr=179"
pars3["G358.7+3.7+179_03_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15 vlsr=179"
pars3["G358.7+3.7+179_04_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15 vlsr=179"
pars3["G358-mos"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15 vlsr=179"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
