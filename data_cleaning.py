
"""
Created on Tue June 29th 2020
@author: Jordyn Ojeda
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# Salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)  # Create a new category of hourly
                                                                                           # When in the Salary Estiamte "hourly" shows up and put if a 1 in the box for per hour
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)  # Create a new category of employer_provider
                                                                                                                       # When in the Salary Estiamte "employer provided salary:" shows up and put if a 1 in the box for per hour

df = df[df['Salary Estimate'] != '-1'] # Gets ride of the -1 salary estimates
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) # Removes the (Glassdoor est.) from the Salary Estimate
remove_kd = salary.apply(lambda x: x.replace('K','').replace('$','')) # Removes the K and $

min_hr = remove_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:','')) # Removes per hour and employer provided salary:

df['min_salary'] = min_hr.apply(lambda x: int(x.split("-")[0]))  # Grabs the minimum salary
df['max_salary'] = min_hr.apply(lambda x: int(x.split("-")[1]))  # Grabs the maximum salary
df['average_salary'] = (df.min_salary + df.max_salary) / 2       # Finds the average of the two salaries

# Company name text only
df['comapny_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1) # Gets ride of the rating of the company and just has the name

# State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1]) # Retrieves the state only (Excludes the city)
df.job_state.value_counts() # Shows how many jobs are in a certain state

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1) # Makes a category of "same_state"
                                                                                          # If the headquarters is in the same state make it 1 otherwise 0
# Age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x) # Finds the age of the company


# Parsing the job description (python, ect.)

# python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0) # Make a new category called 'python_yn' and puts 1 if they want python or 0 if not

# r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0) # Make a new category called 'R_yn' and puts 1 if they want python or 0 if not
df.R_yn.value_counts() # Shows how many companies ask for R

# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0) # Make a new category called 'spark' and puts 1 if they want python or 0 if not
df.spark.value_counts() # Shows how many companies ask for spark

# aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0) # Make a new category called 'aws' and puts 1 if they want python or 0 if not
df.aws.value_counts() # Shows how many companies ask for aws

# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0) # Make a new category called 'excel' and puts 1 if they want python or 0 if not
df.excel.value_counts() # Shows how many companies ask for excel

df.to_csv('salary_data_cleaned.csv',index = False)  # Makes a new file with the changes to "glassdoor_jobs.csv"


