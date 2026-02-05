# -*- coding: utf-8 -*-
"""

------------------------------main.py------------------------------------------

Script master para execução das minhas funções
Created on Thu Feb  5 15:20:21 2026

@author: Ewerthon Bernardi
"""

import first_script
import numpy as np


arr = np.random.rand(100,100)

first_script.timeSeriesPlot(arr)