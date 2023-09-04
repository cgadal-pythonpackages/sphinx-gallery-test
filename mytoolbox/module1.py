"""
Module 1 description

"""

import matplotlib.pyplot as plt
import matplotlib.patches as mptch
import numpy as npt
import numpy as np


def my_plot(x, y):
    """Short summary.

    Parameters
    ----------
    x : type
        Description of parameter `x`.
    y : type
        Description of parameter `y`.

    Returns
    -------
    type
        Description of returned object.

    Examples
    --------
    Examples should be written in doctest format, and
    should illustrate how to use the function/class.
    >>>

    """

    plt.figure()
    plt.plot(x, y)
    plt.show()


class Circle:
    """
    A class representing a circle

    Parameters
    ----------
    O : npt.ndarray
        circle center coordinates
    r : float
        circle radius
    """

    def __init__(self, O: npt.ndarray, r: float) -> None:
        """
        Parameters
        ----------
        O : npt.ndarray
            circle center coordinates
        r : float
            circle radius
        """
        self.O = O  #: circle center coordinates
        self.r = r  #: circle radius
        #
        self.p = 2 * np.pi * r  #: circle perimeter
        self.a = np.pi * r**2  #: circle area

    def plot(self, ax, **kwargs) -> None:
        """
        plot the circle on a given matplotlib ax

        Parameters
        ----------
        ax : _type_
            _description_
        **kwargs: __type__
            _description_
        """
        ax.add_artist(mptch.Circle(self.O, self.r, **kwargs))
