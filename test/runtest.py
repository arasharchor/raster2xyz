# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015-2016.
#  cayetano.benavent@geographica.gs
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from raster2xyz.raster2xyz import Raster2xyz

def runtest():
    # input_raster = "./data/input_raster.tif"
    input_raster = "./data/h10_1005_3-2/h10_1005_3-2.tif"
    out_csv = "/tmp/out_xyz_2.csv"

    rtxyz = Raster2xyz()
    rtxyz.translate(input_raster, out_csv)

if __name__ == "__main__":
    runtest()
