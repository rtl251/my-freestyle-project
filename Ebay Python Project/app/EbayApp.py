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

load_dotenv()


#connecting to Ebay API key from env file
api = finding(appid=(os.environ.get("api_key")),headers=str(), config_file=None)
#api = finding(appid="RobertLa-4-PRD-d66850dff-b909ea31", config_file=None)

#Asks user what they want to search for in ebay
search_words = input("Enter the name of item for which you want to view recently sold data on Ebay:")
print("")
print(f"Enter \"1\" to see sold listings related to {search_words} that are new,")
print(f"Enter \"2\" to see sold listings related to {search_words} that are used,")
condition_input = input(f"Or enter \"3\" to see sold listings related to {search_words} that are both new and used (unspecified):")
accepted_inputs=["1","2","3"]
while condition_input not in accepted_inputs:
    condition_input=input("Input not recognized. Please enter \"1\", \"2\", or \"3\"")

if condition_input =="1":
    condition_value="New"
elif condition_input=="2":
    condition_value="Used"
else:
    condition_value="Unspecified"

condition_value_format=condition_value.lower()

print("")
print(f"Generating list of most recent sold auctions related to {search_words} in {condition_value_format} condition...")

try:

#Full input request to ebay- search term, 100 results (if applicable), sorted by recently sold, new items only, located in U.S. only, Sold Items Only, currency in USD
    ebay_api_request ={
        "keywords": search_words,
        "paginationInput":[
            {"pageNumber": "1"},
            {"entriesPerPage": "100"}],
            "sortOrder": "EndTimeSoonest",
            "itemFilter": [
            {"name": "Condition", "value": condition_value},
            {"name": "LocatedIn", "value": "US"},
            {"name": "SoldItemsOnly", "value": True},
            {"name": "Currency", "value": "USD"}]}

#Response from Ebay API: using beautifulsoup and lxml parser to extract the items that we are looking for

    ebay_response = api.execute("findCompletedItems", ebay_api_request)
    soup = BeautifulSoup(ebay_response.content, "lxml")
    souptext=soup.get_text
    timestamp=(now.strftime("%Y-%m-%d"))
    file_name = search_words + "_" + condition_value_format + "_" + timestamp + ".csv"


#print(souptext)
    ID=[]
    for a in soup.find_all("itemid"):
        id_int=a.text
        id_int=int(id_int)
        ID.append(id_int)


    Description=[]
    for a in soup.find_all("title"):
        Description.append(a.text)


    Sold_Date=[]
    for a in soup.find_all("endtime"):
        item_date = a.text[:10] +" " + a.text[11:19]
        item_date_format =datetime.strptime(item_date, '%Y-%m-%d %H:%M:%S')
        item_date_final = item_date_format.strftime("%Y-%m-%d %I:%M%p")
        Sold_Date.append(item_date_final)

    Sold_Price=[]
    for a in soup.find_all("currentprice"):
        item_price = float(a.text)
        item_price_usd = "${0:,.2f}".format(item_price)
        Sold_Price.append(item_price_usd)

        ebay_history = [{"Ebay ID":ID,"Description": Description,"Sold_Date":Sold_Date,"Sold_Price":Sold_Price} for ID, Description, Sold_Date, Sold_Price
        in zip(ID, Description, Sold_Date, Sold_Price)]

        with open(file_name, "w",  encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Ebay ID","Description","Sold_Date","Sold_Price"])
            writer.writeheader()
            for soldlisting in ebay_history:
                writer.writerow(soldlisting)

    print("List generation complete. A csv file with the most recent sold data is now available.")

except:
    print("ERROR - There is a known issue with ebaysdk and making requests,")
    print(" preventing this program from recognizing the api_key in the .env file: https://github.com/timotheus/ebaysdk-python/issues/162")
    print("see .env file for work-around instructions")
