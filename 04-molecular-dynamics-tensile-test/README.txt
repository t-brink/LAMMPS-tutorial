Background
==========

Up to now, we have considered systems in a given equilibrium state.
When investigating mechanical properties, though, we often need to
change the external conditions throughout the simulation or even go
out of equilibrium.

With the tools from step 3, we could already perform a deformation
test: We can linearly vary the pressure of the barostat and observe
the resulting changes of the system state (see the documentation of
fix npt if you do not know how). This is a pressure-controlled,
hydrostatic setup, though, which is only useful in some cases.

We could also do a stress-controlled, uniaxial tensile test (for
example) by only varying the stress in one direction and keeping the
others stress free (for example replace "iso" with individual settings
for "x", "y", and/or "z", see documentation for details).

Here, we want to explore the displacement-controlled tensile test. Not
because it is more useful (that depends on what you want to do), but
to learn about a new fix.

Young's modulus
===============

We want to determine Young's modulus at room temperature. This
consists of two steps, which we will perform separately.

First, we need to equilibrate the system at 300 K. This is basically
the same procedure as in step 3 of the tutorial, so make a new
directory for the equilibration step and copy the input file from step
3 over. We want to make some modifications, though. The system size is
quite small, so we might want to make it a bit bigger in the tensile
direction. You can repeat the simulation cell three times in x
direction with the command

    replicate 3 1 1

immediately after using either "read_data" or "create_atoms" (see
documentation for details, but this one is quite straightforward). Of
course, we could just change the size of the box in the
"create_input.py" script or in the equivalent commands in LAMMPS. The
replicate command is, however, a useful command to know.

Furthermore, we want to store the atomic positions and velocities
after equilibration in order to reuse them in the next step. This can
be achieved using

    write_data output.data

at the very end of the input file.

* Go ahead, make the modifications and run the equilibration. Make
  sure that energy, temperature, pressure, and volume are
  equilibrated.

Now, you can go ahead with the deformation. Make a new directory and
copy the input file from the equilibration step into it. You need to
read the equilibrated input file "output.data". No need to use
"replicate again", of course.

You will also want to remove any "velocity" command from the input
file: The velocities are already initialized due to the equilibration
and you do not want to overwrite this.

Finally, you need to fiddle with the fixes. Add a new one:

    fix 2 all deform 1 x erate 1e-4

This will apply a constant engineering strain rate of 1e-4/ps = 1e8/s
in x direction. You can also apply a true strain rate with "trate".
For small deformations, this should of course be roughly equivalent.
Careful: Engineering strain rates depend on the initial length in
deformation direction, so strictly speaking true strain is
preferable. Engineering strain is easier to handle, though, so we
often make use of it when the difference is small. You might want to
try out both options here.

* Look at the documentation of "fix deform" to understand the details.

* Adjust the "fix npt" command for this setup. Tip: A barostat is
  incompatible with an applied strain rate, of course.

* Run the simulation and plot the stress–strain curve. Note: LAMMPS
  unfortunately uses two different conventions for its stress
  tensors. Global values (such as the ones in the log file) are in
  fact pressure, where a compressed body has a positive pressure and a
  stretched body a negative one. The mechanical definition is the
  opposite: tensile stresses are positive, compressive stresses
  negative. There is also the "compute stress/atom" command (see step
  01a), which follows the definition from mechanics.

* What is the Young's modulus? Can you extract Poisson's ratio?

* Run an additional simulation in compression and compare the results.
