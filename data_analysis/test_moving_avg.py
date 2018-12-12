#!/usr/bin/env python
import numpy as np
from .data_analysis import moving_average

def testing_moving_average():
    moving_avg=moving_average(np.ones(1000).astype(np.float),4)
    assert np.all(np.isnan(moving_avg[0:4])),"Head fails"
    assert np.all(np.isnan(moving_avg[-4:])),"Tail fails"
    assert np.allclose(moving_avg[4:-4],1.0),"Body fails"
