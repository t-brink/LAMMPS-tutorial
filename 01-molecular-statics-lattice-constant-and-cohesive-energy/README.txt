In the first step, we will obtain the lattice constant and cohesive
energy of fcc copper.

We will use Mishin et al.'s EAM potential for copper [Mishin et al.,
Phys. Rev. B 63, 224106 (2001)], which nicely reproduces many
properties of copper.

Just follow the tasks below. I am assuming a Linux command line with
bash, but there should be nothing particularly specific to it in this
tutorial.

Prerequisites
=============

We will need the following software:

* A recent LAMMPS version, obviously. See <https://lammps.org/>. Have
  a quick look at its documentation and install it in whatever way is
  practical for you. Be sure to have at least the packages "COMPRESS",
  "MANYBODY", "RIGID", and "REPLICA" installed. If possible, also
  install the "VORONOI" package.

* Python 3 with numpy and scipy. You need this anyway.

* The Python package ASE, see <https://wiki.fysik.dtu.dk/ase/> for
  installation instructions.


Create an fcc lattice
=====================

While LAMMPS can do this (see documentation for the commands "lattice"
and "create_atoms"), I find ASE to be more flexible and easier to use.

The ASE script is ready, so study it to see what it does any run it:

    python3 create_input.py

This should yield an output file "Cu-fcc.data.gz".

Run molecular statics
=====================

I always name my input files "lmp.in" and this is reflected in this
tutorial. Feel free to adjust this to your preference later on.

Note: The LAMMPS executable can have different names depending on
      where it comes from and how it was compiled. I am assuming "lmp"
      here, but your system might be different!

Before running the LAMMPS input file, study it. It contains useful
comments describing the commands. Also have a look at the LAMMPS
documentation for each command, it is quite good!

Finished reading? Let's run it:

    lmp -in lmp.in

Analyze
=======

Have a look at the log file, it is always named "log.lammps". Be
careful: When running LAMMPS again, it will be overwritten.

Try to find out the following properties of copper:

* lattice constant in Å

* cohesive energy in eV/atom

Note: In molecular dynamics, we mostly deal with cohesive energies.
      Those are defined as the energy difference between an isolated
      atom and a bonded atom. Isolated atoms will always have a zero
      energy in classical potentials, thereby setting the energy scale
      in MD.

Check your values against the literature (tip: see the paper by Mishin
et al., where the potential is described).

If everything worked, play a bit with the input script to see what
different options do and verify that you understood everything.
