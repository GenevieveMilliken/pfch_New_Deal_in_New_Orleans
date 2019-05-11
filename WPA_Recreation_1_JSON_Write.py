
from bs4 import BeautifulSoup
import requests
import json 

url = "http://nutrias.org/~nopl/photos/wpa/wpa36.htm"

all_my_data = []

home_page = requests.get(url)
home_page_html = home_page.text
soup = BeautifulSoup(home_page_html, 'html.parser')

column_map = {
	1: "series_number",
	2: "project",
	3: "series_title",
	4: "description",
	5: "date_taken",
	6: "project_dates",
	7: "OP",
	8: "negatives",
	9: "contact_prints",
	10: "8x10_prints",
	11: "digital_photos",
}

records = soup.find_all('tr')

for record in records: 
	my_data = {
	}
	
	fields = record.find_all("td")

	counter = 0

	for entry in fields:
		counter = counter + 1
		label = column_map[counter]

		try:
			data_rows = entry.find("p")
			data_rows = data_rows.text
			my_data[label] = data_rows
			
		except AttributeError:
			continue 
	
	image_urls = []	
	item_link = record.find_all('a')
	for link in item_link:
		abs_url = "http://nutrias.org/~nopl/photos/wpa/" + link['href']
		image_urls.append(abs_url)
		my_data[label] = image_urls
		
	all_my_data.append(my_data)

with open('WPA_Recreation_Collection.json', 'w') as f_object:
	json.dump(all_my_data, f_object, indent=2)
	print("Your file is now ready")

