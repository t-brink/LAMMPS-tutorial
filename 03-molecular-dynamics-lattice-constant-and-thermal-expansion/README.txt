Background
==========

In step 2, we used the NVE ensemble, which is often not very useful.
Experiments are performed at, for example, constant temperature and
constant pressure, not constant energy and volume (think about a piece
of metal sitting on a table).

How is constant temperature and pressure achieved in reality? Well,
the experiment takes place in an environment. The room is full of
air, which is at a given temperature and pressure and will tend
towards equilibrium with our experiment.

Since we do not want to model the whole room, we make some assumptions
(this is basic thermodynamics): We assume that the room serves as a
reservoir of heat and volume and that the temperature and pressure
properties of the room do not change when equilibrating with the
experiment (the room is infinitely big). If we were theoreticians, we
could then write down some formulas.

In simulation, we can model the reservoir using thermostats and
barostats, which will add/remove heat to keep a desired temperature
and which can adjust the volume to keep a desired pressure state. For
the theory see the LAMMPS documentation and the references therein.

Lattice constant at a given temperature
=======================================

Copy your input file from step 2.

We need to replace the fix for nve with "npt" to allow lattice
expansion (constant pressure) at a given temperature.

The fix is

    fix 1 all npt temp 300 300 0.1 iso 0 0 1.0

It needs some additional arguments compared to "nve". The temperature
has to be provided twice (one can run simulations where the
temperature is ramped linearly from a starting value to a final
value). The same for the pressure. We use 0, since 1 bar is
insignificant for solids. Feel free to use it and see if there is any
difference (and compare to the noise of the resulting pressure of the
simulation).

The final argument for both temperature and pressure is a damping
parameter. This is a numerical parameter that describes the strength
of the coupling to the reservoir. The LAMMPS manual advises to set the
thermal damping parameter to roughly 100 times the length of the time
step and the pressure damping parameter ten times higher. You can play
around with them to see the effect (if any).

Now for your tasks:

- Run the simulation at different temperatures (how about 300K, 400K,
  500K, and 600K?) and obtain the lattice constant. Note that the
  lattice constant fluctuates from step to step, so you will need an
  average. Do not include the equilibration phase in the average.
  Check if your simulation ran long enough or for too long. Adjust the
  number of time steps as necessary. Don't waste CPU time!

- What is the thermal expansion coefficient of copper according to the
  potential we use?

  α = 1/V (dV/dT)_p
