# University of Michigan Covid-19 Bibliometrics Project

This repository contains the data files, search strings, and scripts
that were used to track and count publications about Covid-19 by 
researchers at the University of Michigan (U-M). The project was initiated by 
the University of Michigan Office of Research (UMOR) in April 2020. 
The files in this repository reflect the expansion of the project up to June of 2021. 
Over that time, the project expanded significantly as the number of publications grew
to encompass scientific and medical studies of the novel coronavirus, the 
epidemiology of the Covid-19 disease, social implications of the pandemic, and 
other topics. The files here reflect the effort to identify scientific, peer-reviewed
publications by researchers at the U-M, and the public bibliography, 
linked at the end of this README, offer a guide to the breadth and extent
of publications by U-M researchers during the Covid-19 pandemic.

Explanation of folders and files contained in this repository:

## new-doi-lists

This folder contains text files of lists of newly-included DOIs in each new
data pull. 

## project-logs

## reports

## source-data

This folder contains the CSV files that were downloaded from the search database. 
To generate lists of articles on the topic of Covid-19, and to limit these 
results to those published by researchers affiliated with U-M, the project team
conducted searches in the U-M's local instance of the Dimensions article database, 
[Michigan Experts](https://experts.umich.edu/discover/experts_publication). 
This interface allowed for publications to be limited to U-M researchers.

We used the following searches:

`up to end of 2020`
`in 2021`

Note that each of the individual files in this folder should contain the 
specific search criteria that generated it, and the date and time that 
the search was executed in the database. 

## workflow-python

Python notebooks and runnable scripts that combine the CSVs from the 
`source-data` folder, create and identify new DOIs for the `new-doi-lists` 
folder, and write logs for the `project-logs` folder.

------

## Bibliography

The resulting bibliography is not contained in this repository but 
shared publicly at https://www.zotero.org/groups/2496143/university_of_michigan_covid_publications.

The bibliography is described as follows:

>> This group collects citations for publications about Covid-19 research that have at least one co-author who is a researcher affiliated with the University of Michigan. The citations were gathered beginning April 30, 2020, and will be updated throughout the following weeks and months to reflect the University of Michigan research output related to Covid-19.
