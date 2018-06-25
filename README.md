# Ebay Recently Sold Listings Generator!

Takes user search inputs of auction items and provides a csv file that contains up to 100 recently sold listings.
User can provide any search terms and can also customize the search to contain listings of new items, used items, or both (unspecified).


## Prerequisites/Setup

Requires Python 3.x, joining Ebay Developer's Program, and registering for a Ebay Production Application Key (Client Id)

JOINING EBAY DEVELOPER'S PROGRAM/REGISTERING FOR EBAY PRODUCTION APPLICATION KEY
-Go to https://go.developer.ebay.com/quick-start-guide

-Click "Join the eBay Developers Program or login" and follow instructions to sign up

-Then go to https://developer.ebay.com/my/keys and request a production Key set

-Use the Production App ID (Client ID) as your api_key.


## Installation

Install packages (listed in pip, but can also be done via pip3 or pipenv)

pip install ebaysdk

pip install bs4

pip install requests

pip install python-dotenv


## Instructions

-Run the ebayapp.py file in the app folder

-When prompted, enter an item search, which will be used to search for recently sold listings

-When prompted, follow the instructions to enter "1","2", or "3" depending on if you want the sold listings to include new items, used items, or both

-Wait for the program to notify you that the csv file containing the list is ready. The name of the file will be based on your parameters, and will appear in the "app" folder.

*NOTE - There is a known issue with ebaysdk and making requests, preventing this program from recognizing the api_key in a.env file
on some machines: https://github.com/timotheus/ebaysdk-python/issues/162.
See .env file for work-around instructions)


## [License]
See License.md file in repository.
