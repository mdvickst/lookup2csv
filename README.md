# lookup2csv
Query Twilio Lookup Line Type Intelligence API for a list of numbers in a CSV and output results as a CSV

# Prerequitsites
- [Python3](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

# Installation
- Download Repository and unzip
- Navigate to the directory `cd lookup2csv-main1`
- Install python-dotenv `pip install python-dotenv`
- Add desired phone numbers to the **input.csv** file (keep the *phone_number* header)
- copy the EXAMPLE.env file and name it **.env**. Then add your Twilio Account SID and Auth Token to to the file. 
- Run the script `python lookup2csv.py`
Results will create a new file **lookupResults.csv** with a colum for each field in the Line Type Intelligence lookup. 
