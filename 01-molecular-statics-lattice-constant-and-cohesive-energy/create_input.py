#!/usr/bin/env python3

# This file serves to create an fcc input file for LAMMPS. We use ASE,
# which can be found at <https://wiki.fysik.dtu.dk/ase/>.
#
# We choose a lattice constant that is a bit off, in order to have
# something to do for the minimization algorithm.

import ase.io
from ase.lattice.cubic import FaceCenteredCubic

box = FaceCenteredCubic("Cu", latticeconstant=4.0,
                        directions=[[1,0,0], [0,1,0], [0,0,1]],
                        size=(10,10,10))

ase.io.write("Cu-fcc.data.gz", box, format="lammps-data")
