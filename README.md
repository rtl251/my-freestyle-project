# Ebay Recently Sold Listings Generator!

Takes user search inputs of auction items and provides a csv file that contains up to 100 recently sold listings.
User can provide any search terms and can also customize the search to contain listings of new items, used items, or both (unspecified).


## Prerequisites

Requires Python 3.x, Joining Ebay Developer's Program, Registering for a Ebay Production Application Key (Client Id)

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


Populate `db/submissions.csv` with entries like the following:

    github_username, repository_url
    user123, https://github.com/user123/some-repo
    user456, https://github.com/user456/another-repo-py/tree/my-branch
    "partner1, partner2, partner3", https://github.com/partner2/group-repo

> NOTE: All repository urls are assumed to be valid. It's ok if they point to certain branches (i.e. urls with "`repo_name`/tree/`branch_name`")

To take advantage of file-checking features, also populate the `db/filenames.csv` file with a list of files and/or directories each repository should contain, for example:

    filepath
    .env.example
    LICENSE
    README.md
    products_app/app.py
    products_app/db/products_default.csv
    tests

## Usage

Download all the repos:

```sh
python3 app/repo_downloader.py # this will populate the `repos` directory!
```

Analyze contents of each repo to detect presence of files at specified locations:

```sh
python3 app/file_checker.py # this will write a report to `db/file_checks.csv`
```

## Testing

Run tests:

```sh
pytest tests/ # specify filepath to exclude tests from downloaded repos
```

## [License](LICENSE.md)
