We often need the full stiffness tensor (elastic constants) of a given
system. Hooke's law in Voigt notation gives either the strain energy density

   E/V = 0.5 · c_ij ε_i ε_j

or the stresses

   σ_i = c_ij ε_j

as a function of strains (ε) and elastic constants (c). We thus need
to subsequently apply a specific set of strains to obtain the full,
symmetric 6×6 matrix representation of the stiffness tensor (see for
example chapter 8 of "Physical properties of crystals: Their
representation by tensors and matrices" by J. F. Nye).

We could implement this ourselves, but there is a completely automated
example included with LAMMPS (examples/ELASTIC in the LAMMPS source
code).

Make yourself aquainted with that and adapt it to our copper
potential.
