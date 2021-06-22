# libraries
from collections import Counter
import csv
import os
from pathlib import Path
import glob
from umich_covid19_bibliometrics_tools import collate_csvs, identify_new_dois, update_project_log

# paths
cur_dir       = Path('.')
inventory_dir = Path('..','combined-CSV-logs')
csv_dir       = Path('..','source-data')
combined_dir  = Path('..','combined-CSVs')
logs_dir      = Path('..','project-logs')
dois_dir      = Path('..','new-doi-lists')

# ask for combine date
combine_date = input('Please enter the date for which you are combining the files [in format YYYYMMDD]:')

# run updates:
#   collate_csvs()
#   identify_new_dois()
#   update_project_log()

csv_update = collate_csvs(combine_date, csv_dir, combined_dir, inventory_dir)
print('Ran collation\n',csv_update)

doi_update = identify_new_dois(combine_date, dois_dir, combined_dir)
print('Identified new DOIs\n',doi_update)

update_project_log(combine_date, csv_update, doi_update, logs_dir)
