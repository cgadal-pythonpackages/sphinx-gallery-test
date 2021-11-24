"""
============
Example 2
============

test

"""

import numpy as np
import sys
sys.path.append('../')
from mytoolbox.submodule.module1 import my_scatter

x, y = np.random.random((100,)), np.random.random((100,))

my_scatter(x, y)
