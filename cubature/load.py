""" Load dxf to postgresql """
import sys

import ezdxf



try:
    doc = ezdxf.readfile("../data/plan-masse.dxf")
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file")

msp = doc.modelspace()
mnt = msp.query('TEXT[layer=="z value TN"]')
for val in mnt:
    x = str(val.dxf.insert.x)
    y = str(val.dxf.insert.y)
    z = str(val.dxf.text)
    print(z)





