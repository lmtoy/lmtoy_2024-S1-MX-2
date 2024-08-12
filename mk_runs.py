#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-2"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["G1.7+3.7-234_01_of_04"]   =  [ 117345,  120317, 120409, ]
on["G1.7+3.7-234_02_of_04"]   =  [ 117349,  120319,]
on["G1.7+3.7-234_03_of_04"]   =  [ 112524,  120323,]
on["G1.7+3.7-234_04_of_04"]   =  [ 112532,  120325, 120407, ]


# 110053  110049  110041  are also the G1 source, in 2023-S1-UM-16


on["G358.7+3.7+179_01_of_04"] =  [ 112139, 112292, 112296, 120057, 120061, 120214,]
on["G358.7+3.7+179_02_of_04"] =  [ 112518, 112788, 117039,]
on["G358.7+3.7+179_03_of_04"] =  [ 113027, 113137, 117043,]
on["G358.7+3.7+179_04_of_04"] =  [ 113029, 113139, 117047,]

# the next two "mos" sources are a combined repeat to make a combined spatial mosaic, this only works if they share them same center RA,DEC

on["G1-mos"]   = on["G1.7+3.7-234_01_of_04"]   + on["G1.7+3.7-234_02_of_04"]   + on["G1.7+3.7-234_03_of_04"]   + on["G1.7+3.7-234_04_of_04"]
on["G358-mos"] = on["G358.7+3.7+179_01_of_04"] + on["G358.7+3.7+179_02_of_04"] + on["G358.7+3.7+179_03_of_04"] + on["G358.7+3.7+179_04_of_04"]

 

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["G1.7+3.7-234_01_of_04"]   = "pix_list=-15 extent=500 b_order=3 dv=30 dw=30 vlsr=-234"
pars1["G1.7+3.7-234_02_of_04"]   = "pix_list=-15 extent=500 b_order=3 dv=30 dw=30 vlsr=-234"
pars1["G1.7+3.7-234_03_of_04"]   = "pix_list=-15 extent=500 b_order=3 dv=30 dw=30 vlsr=-234"
pars1["G1.7+3.7-234_04_of_04"]   = "pix_list=-15 extent=500 b_order=3 dv=30 dw=30 vlsr=-234"
pars1["G1-mos"]                  = "skip=1"     # comment out if no mosaic desired

# M Heyer  04/17./2024 -- vlsr =179 and pix_list=-13  (not 13,14,15)  dv=20 dw=50
pars1["G358.7+3.7+179_01_of_04"] = "pix_list=-15 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_02_of_04"] = "pix_list=-15 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_03_of_04"] = "pix_list=-15 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358.7+3.7+179_04_of_04"] = "pix_list=-15 extent=500 b_order=1 dv=20 dw=50 vlsr=179"
pars1["G358-mos"]                = "skip=1"     # comment out if no mosaic desired

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["G1.7+3.7-234_01_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G1.7+3.7-234_02_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G1.7+3.7-234_03_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G1.7+3.7-234_04_of_04"]   = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G358.7+3.7+179_01_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G358.7+3.7+179_02_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G358.7+3.7+179_03_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"
pars2["G358.7+3.7+179_04_of_04"] = "bank=0 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13"


pars3 = {}
pars3["G1.7+3.7-234_01_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G1.7+3.7-234_02_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G1.7+3.7-234_03_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G1.7+3.7-234_04_of_04"]   = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G358.7+3.7+179_01_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G358.7+3.7+179_02_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G358.7+3.7+179_03_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"
pars3["G358.7+3.7+179_04_of_04"] = "bank=1 birdies=1021,1024,1027,1637,2045,2048,2051 pix_list=-13,14,15"



if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
