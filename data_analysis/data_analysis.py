#!/usr/bin/env python

# coding: utf-8

# # Example data analysis notebook
# 
# This notebook downloads and analyses some surface air temperature anomaly data from [Berkeley Earth](http://berkeleyearth.org/).

# Import the required libraries.

import numpy as np
import requests
import os


# Use the [requests](http://docs.python-requests.org/) library to download the data file for Australia.

def _url(location,statistic):    
    # Define the URL    
    return f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-{statistic.upper()}-Trend.txt'
def _download(location,statistic):
    # Download the content of the URL
    response = requests.get(url)
    # Save it to a file
    with open(f"data_{location}-{statistic}.txt", 'w') as open_file:
        open_file.write(response.text)

# Load the data using numpy (skip the header records which are marked with a `%`).

def open_data(location,statistic="TAVG"):
    if not os.path.exists(f"data_{location}_{statistic}.txt"):
        _download(location,statistic)
    return np.loadtxt("data.txt", comments="%")

def moving_average(data,window):
    moving_avg = np.full(data.size, np.nan)
    for i in range(window, moving_avg.size - window):
        moving_avg[i] = np.mean(data[i - window:i + window])
    return moving_avg
