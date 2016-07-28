#!/usr/bin/env python'
"""Instances of these classes are assigned to different parameter/scopes
by a parameter controller"""

__author__ = "Peter Maxwell"
__copyright__ = "Copyright 2007-2016, The Cogent Project"
__credits__ = ["Peter Maxwell", "Gavin Huttley"]
__license__ = "GPL"
__version__ = "3.0.alpha"
__maintainer__ = "Peter Maxwell"
__email__ = "pm67nz@gmail.com"
__status__ = "Production"


class Setting(object):
    pass


class Var(Setting):
    # placeholder for a single optimiser parameter
    is_constant = False

    def __init__(self, bounds=None):
        if bounds is None:
            bounds = (None, None, None)
        else:
            assert len(bounds) == 3, bounds
        (self.lower, self.value, self.upper) = bounds

    def get_bounds(self):
        return (self.lower, self.value, self.upper)

    def get_default_value(self):
        return self.value

    def __str__(self):
        return "Var"  # short as in table

    def __repr__(self):
        constraints = []
        for (template, bound) in [
                ("%s<", self.lower),
                ("(%s)", self.value),
                ("<%s", self.upper)]:
            if bound is not None:
                constraints.append(template % bound)
        return "Var(%s)" % " ".join(constraints)


class ConstVal(Setting):
    # not to be confused with defns.Const.  This is like a Var,
    # assigned to a parameter which may have other Var values
    # for other scopes.
    is_constant = True

    # Val interface
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)  # short as in table

    def __repr__(self):
        return "ConstVal(%s)" % repr(self.value)

    # indep useful sometimes!
    # def __eq__(self, other):
    #    return type(self) is type(other) and other.value == self.value

    def get_default_value(self):
        return self.value

    def get_bounds(self):
        return (None, self.value, None)
