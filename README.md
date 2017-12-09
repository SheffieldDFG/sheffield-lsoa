# sheffield-lsoa

LSOA boundaries for Sheffield

Downloaded shapefile from
[Lower Layer Super Output Areas (December 2011) Generalised
Clipped Boundaries in England and
Wales](http://geoportal.statistics.gov.uk/datasets/lower-layer-super-output-areas-december-2011-generalised-clipped-boundaries-in-england-and-wales).

Then converted it to CSV using
[shpit](https://github.com/SheffieldDFG/shpit).

Then extracted just the Sheffield part using `sed` to make the
file

    Lower_Layer_Super_Output_Areas_December_2011_Generalised_Clipped__Boundaries_in_Sheffield.csv

That file has coordinates in British National Grid;
the Python program `bin/convertWGS84.py`
transforms them to WGS 84 (suitable for web)
using [pyproj](https://github.com/jswhit/pyproj).
It creates the file

    Lower_Layer_Super_Output_Areas_December_2011_Generalised_Clipped__Boundaries_in_SheffieldWGS84.csv

That file has two additional, final, columns, called `lon` and `lat`
(for longitude and latitude).
