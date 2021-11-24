"""
============
Example 1
============

Test

"""

import numpy as np
import sys
sys.path.append('../')
from mytoolbox.module1 import my_plot

x, y = np.random.random((100,)), np.random.random((100,))

my_plot(x, y)
