
"""
Created on Fri May 29th 2020
@author: Jordyn Ojeda
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/jordynaojeda/Documents/Portfolio_Projects/data_science/chromedriver" # Path to use chromedriver

df = gs.get_jobs('data scientist', 1000, False, path, 15)  # Calls what job to find and how many

df.to_csv('glassdoor_jobs.csv', index = False)  # Stores the data in a file glassdoor_jobs.csv

df