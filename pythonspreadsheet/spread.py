import gspread
from oauth2client.service_account import ServiceAccountCredentials	
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_config.json',scope)
# Load your config file
client = gspread.authorize(creds)

sheet = client.open('data').sheet1

pp = pprint.PrettyPrinter()

# sara = sheet.get_all_records()

# sara = sheet.col_values(2)

#sara = sheet.cell(2,3).value

# sheet.update_cell(3,3,"gomalvyas007@gmail.com")
# sara = sheet.cell(3,3).value
# row = ["haseeb",21,"haseeb@gmail.com"]
# index = 4

# sara = sheet.insert_row(row,index) 


# sheet.delete_row(4)

print(sheet.row_count)
#pp.pprint(sara) 		
