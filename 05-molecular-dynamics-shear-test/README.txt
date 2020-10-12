Background
==========

In all previous step, we used orthogonal simulation boxes. We will now
look at sheared systems.

There is not much to it, but you should take note on the limitations
and peculiarities of LAMMPS's simulation cells.

LAMMPS issues
=============

First, LAMMPS does not support sheared cells by default. A cell needs
to be converted to be "triclinic". A lot of details can be found at

    <https://lammps.sandia.gov/doc/Howto_triclinic.html>.

You can switch between both cases using

    change_box all ortho

and

    change_box all triclinic

at any time. The first command requires the box to actually be
orthogonal, though.

Let's distinguish from now on between the cartesian directions x, y,
and z and the three vectors a, b, and c that span the simulation cell
(which is always a parallelepiped). In order to simplify the
implementation, a must always point in x direction and b must always
lie in the xy plane. The origin of the cell lies at (xlo, ylo, zlo).
The cell vectors are now not only defined in terms of Lx, Ly, and Lz,
but also in terms of the tilt factors Xy, Xz, and Yz:

    a = (Lx,  0,  0)
    b = (Xy, Ly,  0)
    c = (Xz, Yz, Lz)

Any general parallelepiped can be converted into this form by
rotation. Changing a tilt factor does not change the volume of the
simulation cell.

The tilt factors are useful, since they can easily be converted into
the engineering definitions of the shear strain (approximation only
strictly valid for small strains):

    γ_xy = Xy / Ly
    γ_xz = Xz / Lz
    γ_yz = Yz / Lz

Note that these are shears in Voigt notation. A conversion into
tensorial shears includes a factor ½:

    ε12 = ½ γ_xy
    ε31 = ½ γ_xz
    ε23 = ½ γ_yz


Shear deformation
=================

We can reuse the data file from the equilibration simulation of the
previous step of the tutorial.

Copy the tensile test input file. After "read_data", convert the
simulation cell to a triclinic one.

Change the "fix deform" command to perform xz shear.

Side notes:

  A small note on the definitions: The shear rate is also given in
  terms of γ as indicated above, so it is twice that in terms of
  ε. Fortunately, the engineering shear strain does not depend on the
  amount of intial shear, so applying the same engineering shear rate
  two boxes with different initial shear results in the same true
  shear rate.

  There are some issues with larger strains. In the standard
  definition of xz shear,

    ε = (  0   0 ε31)
        (  0   0   0)
        (ε31   0   0),

  the values of γ_xz and γ_zx are obviously identical. The LAMMPS
  version,

    ε = (   0    0    0)
        (   0    0    0)
        (γ_xz    0    0),

  is not just a rotation of the above. With larger deformations, the
  definition will deviate and a tensile stress in z direction appears,
  which disturbs the symmetry.

We are quite happy with ignoring these complexities for now. Instead,
we will look at plastic events in the simulation. For this, we need to
visualize the atomic positions. LAMMPS can produce "dump files"
containing all sorts of per-atom information. These are quite
flexible, but I tend to use somthing like this:

    dump         MyDump all custom 10000 structure.dump.*            &
                 id type x y z vx vy vz ix iy iz
    dump_modify  MyDump pad 10

The number in the "dump" command indicates at which timesteps dump
files should be written, here at multiples of 10000. In this example,
we are writing the following properties of the atoms to the dump file:

    id       - a unique number for each atom (counting from one)
    type     - the numeric type of the atom
    x,y,z    - the position of the atom in cartesian coordinates
    vx,vy,vz - the velocity of the atom
    ix,iy,iz - the image of the atom

The latter (ix,iy,iz) is sometimes nice to have: It indicates in which
periodic image an atom is located. What does that mean? All atoms
start in image 0. If any atom crosses the periodic boundary in
positive x direction once, ix is updated to 1. Two additional
crossings in negative x direction first bring the atom back to ix = 0
and then to ix = -1.

This data, together with the interatomic potential, completely
describe the state of the system. Energies, forces, stresses, etc. can
be derived.

The file names are all of the format "structure.dump.*", where "*" is
replaced with the timestep. The "dump_modify" command enforces that
the timestep will be left-padded with zeros until the string has
length 10. This ensures correct sorting in file managers and on the
command line.

* Add the dump command and adjust the frequency of dumps: You will not
  want to have too many, since that takes too much storage space, but
  you will not want too few, since that loses information. This needs
  some experimentation.

* Run a shear simulation up to 20% shear.

* What is the shear modulus?

* Visualize the dump files, for example using Ovito <https://ovito.org>.
  Can you detect dislocation activity?
