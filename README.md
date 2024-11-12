# AeroKit: An aerodynamics toolbox for Python

The vision for this repository is to host a Python package capable of basic calculations similar to those found in undergraduate aerospace engineering coursework. This package heavily relies on symbolic computation.

The concept of operations for this package will revolve around a `Node()` class. This may be expanded in the future. Essentially, different regions or points in a flow can be expressed as a `Node()`, then different effects (e.g. a normal shockwave) can be applied to a `Node()` object, returning another `Node()` object representing the flow after the application of the effect.
