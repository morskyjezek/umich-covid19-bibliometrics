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

## Update process

1. Pull data from bibliographic databases.
1. Identify new citations by DOI.
1. Request full citations through Zotero. 
1. Remove citations that are not relevant to the bibliography.
1. Add relevant list of citations to [public group bibliography](https://www.zotero.org/groups/2496143/university_of_michigan_covid_publications) and update reports.

The process requires access to these tools: UMich Library login for databases, update tools (this repository), Zotero account, access to group Zotero bibliography.

### Process walkthrough

#### Pull data

As of June 2021, we have used the following search string for bibliographic databases:

```
"2019-nCoV" OR "COVID-19" OR “SARS-CoV-2” OR "HCoV-2019" OR "hcov" OR "NCOVID-19" OR  "severe acute respiratory syndrome coronavirus 2" OR "severe acute respiratory syndrome corona virus 2" OR (("coronavirus"  OR "corona virus") AND (Wuhan OR China OR novel))
```

The search string was developed with input from Informationists at the Taubman Health Sciences Library
and has been updated since May 2021 by UMOR staff. 

Once results are requested, retrieve results in a CSV file. 

#### Collate data

Using the tools in this repository, count and parse the data to identify new citations in the list. 

#### Request full citations

Use the list of new articles, represented as DOIs, to retrieve the full citations in Zotero. 
We have used the desktop application for this task. 

#### Remove irrelevant citations



Explanation of folders and files contained in this repository:

## new-doi-lists

This folder contains text files of lists of newly-included DOIs in each new
data pull. 

## project-logs

This folder contains logs of updates. The main file, `project_log.tsv`, contains a record for each successive update. The log contains these fields for each update: 

* Date_of_update - formatted as YYYYMMDD
* Collated CSV files - a number, representing the number of CSV files that were included in the update
* Number of items/articles in update - a number, representing the total number of citations included; this should roughly correspond to the number of lines in all of the CSV files, disregarding header rows
* Number of DOIs in update - a total number of database object identifiers (DOI) included in the update, this may differ from the toal number of citations since not all citations included a DOI
* Unique DOIs in update (one or more occurrence) - a total number of unique DOIs in the update, this represents the previous list (total DOIs in the update) with duplicates removed
* New DOIs in update (only one occurence) - the total number of DOIs that occur only in the most recent update, this is derived by comparing with the previous lists and removing any DOIs that appear more than once
* Note - a brief text note to explain any major changes that may have affected the update, in cases where there is no change, the field reads "No note recorded"
* Combined CSV file - the  path, relative to this repository collection, and name of the file that has all of the combined citations (number of lines should correspond to the `Number of items/articles in update` field)
* CSV Inventory file - the path, relative to this repository collection, and name of the log file that lists all of the CSVs inventoried at each update
* New DOI file - the path, relative to this repository collection, and name of the list of new DOIs

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
