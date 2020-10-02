Now you will advance to dynamics. For this step, there will still be a
"lmp.in" file that you can run. In the next steps, you will have to
copy and modify that file yourself.

Always use a new directory for each simulation. This keeps order and
preserves all the files.

Prepare
=======

Read the input file.

Run
===

This is the same for dynamics and statics:

    lmp -in lmp.in

Analysis and exploration
========================

Have a look at the log file. Plot the energy and temperature over
time.

Tip: gnuplot makes it easy to plot log files. You can run

    gnuplot
    gnuplot> plot "log.lammps" using 1:2 with lines

to plot column 2 versus column 1. The nice feature of gnuplot is that
it will ignore all the lines in the log file that don't look like
numbers, so it is quite fast to make a quick plot.

- What happens to the temperature? Why? Can you fix this?

- If you modified the simulation correctly, you should get a
  temperature of 150 K. Why? Because of the equipartition theorem.
  Half of the kinetic energy we inserted gets converted to potential
  energy. You can think of the system as a set of harmonic
  oscillators, which are at rest at the beginning of the simulation.
  At any point in time, some oscillators will have minimum potential
  energy and thus the full kinetic energy, others will have zero
  kinetic energy since they are displaced as far as possible given the
  provided energy, and most atoms will be somewhere in between. On
  average this leads to an equal partition between kinetic and
  potential energy.

- Finally, look at the energy. Is it conserved? Make some
  subdirectories and run simulations with different time step. Observe
  how that influences the energy conservation.

