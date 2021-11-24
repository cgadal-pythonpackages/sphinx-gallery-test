"""
============
Example 3
============

test

"""

import numpy as np
import sys
sys.path.append('../../')
from mytoolbox.submodule.module2 import my_histo

x = np.random.normal(100, 100, 100)

my_histo(x)
