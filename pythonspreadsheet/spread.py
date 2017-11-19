import gspread
from oauth2client.service_account import ServiceAccountCredentials	
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_config.json',scope)
client = gspread.authorize(creds)

sheet = client.open('data').sheet1

# pp = pprint.PrettyPrinter()

sara = sheet.get_all_records()

print(sara) 		
