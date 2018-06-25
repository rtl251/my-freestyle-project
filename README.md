# Project Planning

## Problem Statement

### Primary User
Me (student in python programming and software development class)

### User Needs statement

I am looking for a way to save the information of recently sold listings on Ebay.

Currently a user of Ebay can manually retrieve records of items
that have been sold on the Ebay platform within the last 3 months.

But instances beyond 3 months are deleted from Ebay's searchable records. This 3-month period
is rolling: If today is 6/16/2018, you will be able to retrieve sold listings on 3/16/2018, but 
tomorrow you will no longer be able to retrieve that data.

A program that would be able to search for sold listings and save the data in a 
csv file would prove useful to users would wish to track the sales history of a particular item 
for periods beyond 3 months, as this functionality currently isn't available.

### Program Steps:

1. Program will ask user to type name of item that they would like to research recently sold data on Ebay.
2. Program will ask user if they want to filter the data on sold listings of new items, used items, or both new and used (unspecified).
3. Program sends a request to Ebay API to retieve the most recent sold listings, starting with the item that was sold most recently.
4. The program will generate a csv file. The file will contain a list of sold listings, with each listing including its Ebay ID, Item Description, Date Sold, and price that the item sold for.
5. This list can be kept and revisited even after ebay removes the historical listing data from its records and is no longer retrievable through Ebay's API.

## Information Requirements

### Information Inputs

A  record of a particular item that was sold on Ebay and its attributes, including auction end date, ending price, 
shipping cost, Ebay seller name, size (if applicable) and description. (possibly pictures as well)

### Information Outputs
The inputted data written neatly in a csv file (list of data dictionaries), with future inputs to be added
in the same format.

## Technology Requirements

### APIs and Web Service Requirements
Ebay API

### Python Package Requirements
Ebaysdk - interface into the Ebay APIs

Beautiful Soup - for parsing Ebay data

pytest - for testing 

csv - for csv writing

### Hardware Requirements
This application will run from my personal machine, with no plans to run this application
on a public server.

