# Project Planning

## Problem Statement

### Primary User
Me (student in python programming and software development class)

### User Needs statement

I am looking for a way to save the information of recently sold listings on Ebay.

Currently a user of Ebay can manually retrieve records of items
that have been sold on the Ebay platform within the last 3 months.

But instances beyond 3 months are deleted from Ebay's searchable records. This 3-month period
is rolling: If today is 6/16/2018, you will be able to retrieve sold listings on 3/17/2018, but 
in a week from now, you will no longer be able to retrieve that data.

A program that would be able to search for sold listings and save the data in a 
csv file would prove useful to users would wish to track the sales history of a particular item 
for periods beyond 3 months, as this functionality currently isn't available.

### Program Steps:

1. Program will ask user to type name of the item they wish to search Ebay to gather recently sold listings data
2. Program will ask user if they want to filter the data on sold listings on new items, used items, or do they wish to see both new and used (unspecified).
3. Program sends a request to Ebay API to retrieve the most recent sold listings, starting with the item that was sold most recently.
4. The request will seek only items that are located in the United States. The request will ask for a 100 listings maximum, or less if there haven't been 100 sold auctions within the last 3 months that relate to what the user is searching for.
5. The program will generate a csv file. The file will contain a list of sold listings, with each listing including its Ebay ID, item description, date sold, and price that the item sold for.
6. This list can be kept and revisited even after Ebay removes the historical listing data from its records and is no longer retrievable through Ebay's API.

## Information Requirements

### Information Inputs

A request sent to Ebay's API containing keywords, item condition, the maximum number of instances to retrieve, to order the instances starting with the auction that ended most recently, U.S. location, and to see listings that were actually sold to a buyer.

### Information Outputs
Ebay will send a response that will be formatted to csv file (list of data dictionaries), containing recently sold auctions. The list will be sorted by ending auction time (most recent), and will contain Ebay ID, item description, ending auction date, and sold price.

## Technology Requirements

### APIs and Web Service Requirements
-Join Ebay Developer's Program

-Ebay Production Application Key (Client Id)

-Finding API (findCompletedItems)

### Python Package Requirements
from ebaysdk.finding import Connection as finding

from bs4 import BeautifulSoup

import requests

import io

from dotenv import load_dotenv

import os

import csv

import datetime

now = datetime.datetime.now()

from datetime import datetime

### Hardware Requirements
This application will run from my personal machine, with no plans to run this application
on a public server.

