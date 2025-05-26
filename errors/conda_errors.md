# Error 1
```
Error while loading conda entry point: conda-libmamba-solver (libarchive.so.20: cannot open shared object file: No such file or directory)

CondaValueError: You have chosen a non-default solver backend (libmamba) but it was not recognized. Choose one of: classic
```
-  Means the system is missing a required shared library `libarchive.so.20` that the libmamba solver needs, and conda is falling back to classic

## What is a solver in conda
- when we ask conda to install packages or create an environment, it needs to figure out : (Dependency resolution)
    - which packages to install
    - how to satisfy all dependencies
    - how to avoid conflicts
- The software that solves this is called solver.

- Types of solvers in conda
    - classic solver
        - Original solver conda has used for years
        - written in python, reliable but slow on big environments
    - libmamba solver
        - newer, faster
        - based on libmamba c++ library
        - requires some system libraries like libarchive.so.20
- Reason for the error:
    - system is missing libarchive.so.20 that libmamba depends on so libmamba couldn't start and conda threw an error.
- running `conda config --set solver classic` tells conda to use original python based solver that does not need `libarchive.so.20`