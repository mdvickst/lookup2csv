import csv
import os
from twilio.rest import Client
from os.path import exists
from dotenv import load_dotenv

load_dotenv()



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

with open('input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    writeHeaders=0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            if not exists('lookupResults.csv'):
                writeHeaders=1
        print(f'Lookup on Phone Number\t{row["phone_number"]}.')
        lookupResults = client.lookups.v2.phone_numbers(row["phone_number"]).fetch(fields='line_type_intelligence')
        with open('lookupResults.csv', 'a') as csv_file:
            writer = csv.writer(csv_file) 
            if lookupResults.line_type_intelligence:
                keysList = list(lookupResults.line_type_intelligence.keys())
                fieldnames = ['phone_number'] + keysList
                if writeHeaders:
                    writer.writerow(["phone_number"] + list(lookupResults.line_type_intelligence.keys()))
                    writeHeaders=0
                writer.writerow([row["phone_number"]] + list(lookupResults.line_type_intelligence.values()))
                print([row["phone_number"]] + list(lookupResults.line_type_intelligence.values()))
            else:
                writer.writerow([row["phone_number"],'','','','',''])
            line_count += 1

    print(f'Processed {(line_count-1)} lines.')