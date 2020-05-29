
"""
Created on Fri May 29th 2020
@author: Jordyn Ojeda
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/jordynaojeda/Documents/Portfolio_Projects/data_science/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)