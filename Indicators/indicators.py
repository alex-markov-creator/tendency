#-*- coding: utf-8 -*-
"""
*.py - name file.
"""
import sys
import os
sys.path.append(os.path.realpath('..'))
import logging

import pandas as pd
import matplotlib.pyplot as plt
import Indicators.Indicators_Process_B_7_5.production as pr
import Indicators.Indicators_Process_B_7_3.project_and_develop as pad

logger = logging.getLogger('log')
y = pr.Data_Table(pad.data_koef_nov_pri_razr_year)
x = pr.Data_Table(pr.data_ur_neispr_obor_middle_year)
print(x)
print(y)
