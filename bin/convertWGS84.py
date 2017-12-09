#!/usr/bin/env python3

import csv
import sys

# https://github.com/jswhit/pyproj
import pyproj

INP = "Lower_Layer_Super_Output_Areas_December_2011_Generalised_Clipped__Boundaries_in_Sheffield.csv"


def main(argv=None):
    if argv is None:
        argv = sys.argv


    # http://spatialreference.org/ref/epsg/osgb-1936-british-national-grid/
    os_proj = pyproj.Proj(init='epsg:27700')
    # http://spatialreference.org/ref/epsg/wgs-84/
    wgs_proj = pyproj.Proj(init='epsg:4326')

    OUT = INP.replace('.csv', 'WGS84.csv')
    out = csv.writer(open(OUT, 'w'))

    rows = csv.reader(open(INP))
    header = next(rows)
    header += ['lon','lat']
    out.writerow(header)
    for row in rows:
        x, y = row[3:5]
        lon, lat = pyproj.transform(os_proj, wgs_proj, x, y)
        row += [lon, lat]
        out.writerow(row)
    

if __name__ == '__main__':
    main()
