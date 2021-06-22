#!/usr/bin/env python
# coding: utf-8

# # UMich Covid19 Bibliometrics Python Tools
# Setup
from collections import Counter
import csv
import os
from pathlib import Path
import glob

# functions for python workflow to identify new DOIs

def collate_csvs(combine_date, csv_dir, combined_dir, inventory_dir):
    '''
    This function searches the `source-CSVs` directory to identify 
    CSV files that contain the citations that are pulled from 
    the Dimensions database. These results represent the search 
    results created by the database to list publications by U of Michigan
    authors relating to the Covid-19 coronavirus (SARS-CoV-2). It combines
    these CSVs into a single CSV, creating consistent columns and removing 
    extra data from Dimensions.
    
    Requires:
      combine_date - a datestring in YYYYMMDD format representing the date of the most recent update
      
    Outputs:
      a full CSV titled `combination-list-py-YYYYMMDD.csv`
      an inventory log that lists the CSV files combined
      info for the project logs    
    '''
    
    #csv processing setup
    csv_count = 0 
    #some fields contain more characters than the default limit; this increases the field limit
    csv.field_size_limit(150000)
    csv_list = csv_dir.glob('Dimensions-Publication-2020*.csv')
    
    #create headers for csv; current as of May 2021
    fields = 'Rank,Publication ID,DOI,PMID,PMCID,Title,Abstract,Acknowledgements,Source title,Anthology title,MeSH terms,Publication Date,PubYear,Volume,Issue,Pagination,Open Access,Publication Type,Authors,Authors (Raw Affiliation),Corresponding Author,Authors Affiliations,Research Organizations - standardized,GRID IDs,Country of Research organization,Funder,Times cited,Recent citations,RCR,FCR,Altmetric,Source Linkout,Dimensions URL,FOR (ANZSRC) Categories,Sustainable Development Goals,Publication Date (print),Publication Date (online),Publication Date'
    fieldnames = list()
    for name in fields.split(','):
        fieldnames.append(name)
    
    # empty list for combined items (ie, rows)
    item_list = list()
    
    # output files
    combined_file_name = 'combination-list-py-' + str(combine_date) + '.csv'
    combinelog_file_name = 'combinelog_' + str(combine_date) + '.tsv'
    inventory_file_name = 'csv_inventory_' + str(combine_date) + '.tsv'

    #for inventory log
    lines = 0
    inventory_log = 'File \tNumber of CSVs \tLines \t Cumulative Lines\n'


    # collate and combine the Dimensions CSVs
    for f in csv_list:
        if f.is_file() == True:
            print('Collating',f)
            csv_count += 1
            inventory_log += str(f) + ' \t' + str(csv_count) + '\t'
            with f.open(mode = 'r', newline = '', encoding='utf-8') as bibs:
                #skip first line
                itemdata = bibs.readlines()[1:] # skip the header information
                linecount = len(itemdata)
                lines = lines + linecount
                print(linecount,'lines;',lines,'cumulative lines')
                inventory_log += str(linecount) + ' \t' + str(lines) + '\n'
                items = csv.DictReader(itemdata, delimiter=',', restval='Blank')
                for item in items:
                    item_list.append(item)
        else:
            print('Not a file:',str(f))
    print('Collated ' + str(csv_count) + ' csv files and ' + str(lines) + ' lines on ' + str(combine_date)+'.')
    total_items = len(item_list)

    # write the CSVs to a single file
    with open(Path(combined_dir,combined_file_name), 'w') as f:
        combination_file = csv.DictWriter(f, fieldnames=fieldnames, restval='Blank', extrasaction='ignore') # use restval to add where no values are recorded and extrasaction set to ignore errors when fieldsets do not match
        combination_file.writeheader()
        combination_file.writerows(item_list)

    print('Combined csv files into: ' + str(combined_dir) + '/' + str(combined_file_name))
    
    #create CSV inventory for this update
    with open(Path(inventory_dir,inventory_file_name), 'w', encoding='utf-8') as logfile:
        logfile.write(inventory_log)
        print('Logged CSV list in: ' + str(inventory_dir) + '/' + str(inventory_file_name))
    
    # store collation numbers
    collate_csv_report = {
        'combine_date': combine_date,
        'csv_count'   : csv_count,
        'total_items' : len(item_list), 
        'combined_file_name': str(Path(combined_dir,combined_file_name)),
        'inventory_file_name': str(Path(inventory_dir,inventory_file_name)),
    }
    
    return collate_csv_report

def identify_new_dois(combine_date, dois_dir, combined_dir):
    '''
    This function reads in data from the most recent combined list of articles,
    pulls the DOIs (database object identifiers), which are the most consistent
    identifiers for articles and can be reused in bibliographic citation software,
    then combines them, identifies how many unique dois are in the list, and 
    identifies new DOIs that did not appear in previous data pulls

    Requires:
      combine_date - a datestring in YYYYMMDD format representing the date of the most recent update

    Output:
      writes a text file with the new DOI list
      returns numbers for the project and update logs 
    '''
    
    # DOI processing setup
    combined_dois = list()
    doi_key_errors_c = 0 
    doi_blanks_c = 0
    #doi_counts = dict()
    unique_dois = 0
    new_dois = list()
    new_doi_c = 0
    
    # location for input CSV with items
    combined_csv_loc = Path(combined_dir,'combination-list-py-' + combine_date + '.csv')

    # list for items (ie, CSV rows)
    item_list = list()
    
    # output files
    doioutput_file_name = 'unique_doi_output-' + str(combine_date) + '.txt'
    
    # create combined_dois list
    with open(combined_csv_loc, 'r', encoding='utf-8') as f:
        item_list = csv.DictReader(f)
        for item in item_list:
            item_doi = item.get('DOI')
            try:
                if item_doi == '':
                    #print('DOI is blank:', item['Title'])
                    doi_blanks_c += 1
                elif item_doi == 'DOI':
                    #print('row is header')
                    continue
                elif item_doi.startswith('10.') == False:
                    print('Invalid DOI:',item_doi)
                else:
                    combined_dois.append(item_doi)
            except KeyError:
                doi_key_errors_c += 1
    total_doi_c = len(combined_dois)
    print('Items with no DOI value or empty string:',doi_blanks_c,'\nKey Errors:',doi_key_errors_c,'\n\nCollated',str(total_doi_c),'DOIs; some may be duplicates.')
    
    # create unique DOI list
    # count the values and identify single occurence DOIs
    c = Counter(combined_dois)
    c.most_common
    doi_counter = dict(c)
    unique_dois_c = len(doi_counter)

    # isolate the unique DOIs (that is, the "new" ones that only occur once in the list)
    for k,v in doi_counter.items():
        if v < 2:
            new_dois.append(k)
    new_doi_c = len(new_dois)
    print('Identified',str(new_doi_c),'new DOIs (single occurences).\n')
    
    # write unique dois to file
    # write new DOIs to file
    line_c = 0

    with open(Path(dois_dir,doioutput_file_name), 'w') as fh:
        for doi in new_dois:
            line = str(doi) + '\n'
            fh.write(line)
            line_c += 1
        print(f'Wrote unique dois to file: {doioutput_file_name} ({str(line_c)} lines)')
    
    # store update report
    unique_doi_report = {
        'combine_date'  : combine_date,
        'blank_dois'    : doi_blanks_c,
        'total_doi_c'   : total_doi_c,
        'unique_dois_c' : unique_dois_c,
        'new_doi_c'     : new_doi_c,
        'doioutput_file_name': str(Path(dois_dir,doioutput_file_name)),
    }
    
    return unique_doi_report



def update_project_log(combine_date, csv_update, doi_update, logs_dir):
    '''
    This function should be run after the CSVs are compiled and unique DOIs are identified.
    
    This function will update the project log to record the update as of the combine_date.

    Inputs:
      combine_date should be a date formatted YYYYMMDD
      csv_update should be a dictionary generated by the collate_csvs() function
      doi_update should be a dictionary generated by the identify_new_dois() function
      
    Outputs:
      append a new line to the `project_log.tsv` that shows information about the current update
    '''

    # log file name
    projectlog_file_name = 'project_log.tsv'

    # prepare the log information
    project_update_entry = str(combine_date) + '\t' + str(csv_update['csv_count']) + '\t' + str(csv_update['total_items']) + '\t' + str(doi_update['total_doi_c']) + '\t' + str(doi_update['unique_dois_c']) + '\t' + str(doi_update['new_doi_c']) + '\tNo note recorded\t' + str(csv_update['combined_file_name']) + '\t' + str(csv_update['inventory_file_name']) + '\t' + str(doi_update['doioutput_file_name'])

    with open(Path(logs_dir,projectlog_file_name), mode='a', newline='') as logfile:
        logfile.write('\n')
        logfile.write(project_update_entry)
        print('Updated project log file: project_log.tsv\nIf you need to record a note about this update, open the log and enter it.')

    # create a separate log file for the  current update? 
    #logfile.write(projectlog_file_name)
    #logfile.write('projectlog.tsv')
    print('\nUpdated project log for',str(combine_date),'update.')


# Create Log file 
def create_log(log_name):
    '''
    Writes logs for the current update and adds information to a new, overall project log file.
    
    Warning: running this script may overwrite project log files, use with caution.
    
    Requires:
      combine_date - a datestring in YYYYMMDD format representing the date of the most recent update
    '''

    log_name = str(log_name) + '.tsv'
    
    headers = 'Date_of_update \tCollated CSV files \tNumber of items/articles in update \tNumber of DOIs in update \tUnique DOIs in update (one or more occurrence) \tNew DOIs in update (only one occurence) \tNote \tCombined CSV file \t CSV Inventory file \tNew DOI file'
#    sample_project_update = 'test update'

    with open(Path('..',log_name), mode='w', encoding='utf-8') as new_log:
        new_log.write(headers + '\n')
    print('Wrote new log file:', log_name)

    #create_log('project_log.tsv')