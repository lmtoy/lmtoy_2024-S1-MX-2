# 2024-S1-MX-2

Two sources, taken in quadrants.  We can safely use one source name?  Use G358 and G1 ?

G358.7+3.7+179 (_01_of_04 etc.)
G1.7+3.7-234   (_01_of_04 etc.)    [see also 2 fields in 2023-S1-UM-16]

These data are huge, we needed 32GB memory for processing, 16GB was not enough.

vlsr=0 given, but that's for local CO (clearly detected in both 12CO and 13CO),
whereas the HVC is at +179 and -234 km/s resp.

For the latter, a small dv,dw and appropriate vlsr= will be needed. A lot of beams are
very erratic. Minus the usual 13 for bank=0 and 13,14,15 for bank=1.

Also, extent= does not work for mosaiced fields like this.

Mosaicking the 4 fields will be interesting challenge. calibration scale. effect of the ramps
The 12CO looks harder to match, the 13CO looks more clean (for G358)

Also: since the OFF position is in nearby CO, the spectra have negative components,
almost like a frequency switching method. Certainly fields 1 and 2 have different
OFF positions, the 4 fields do not share some absolute oFF that's always the same.

plenty birdies here: birdies=1021,1024,1027,1637,2045,2048,2051

odd is that 1637 is narrow birdie, whereas 1024 and 2048 have those MHz wings
they are at +/- 3 channels, but weaker wings at +/- 6 channels

