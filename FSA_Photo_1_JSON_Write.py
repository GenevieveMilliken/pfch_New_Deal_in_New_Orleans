# This python script uses web scraping techniques to capture metadata and images of photos taken in New Orleans
# by the United States Farm's Security Administration and Office of War Information (FSA-OWI) hosted by Yale's  
# Photogrammar.

from bs4 import BeautifulSoup
import requests
import re
import json

all_my_data = []

for pages in range(0,5):
	url = f"http://photogrammar.yale.edu/search/results.php?start={pages*60}&search=%22New+Orleans%22&pname=&lot=&van=&state=&county=&city=&year_start=1935&month_start=0&year_stop=1945&month_stop=12"
      
	results_page = requests.get(url)
	results_page_html = results_page.text
	soup = BeautifulSoup(results_page_html, "html.parser")

	items = soup.find_all("div", attrs = {'class':'results-image'})

	for item in items:

		my_data = {
			"Item URL": None,
		 	"Caption": None,
		 	"Photographer": None,
		 	"Created": None,
		 	"Location": None,
		 	# "Call Number (Library of Congress)": None,
		 	"Image URL": None,
		 	"LOC URL": None,
		 	"LOC Call Number": None,

		 }

		print('------------')
		item_link = item.find('a')
		abs_url = "http://photogrammar.yale.edu/" + item_link['href']
		my_data['Item URL'] = abs_url
		# print(abs_url)


		item_request = requests.get(abs_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")

		all_field_divs = item_soup.find_all("div", attrs={'id':'record-meta'})

		for field in all_field_divs:

			#get 'Caption' field and assign it to dictionary 
			caption = field.find('span', attrs = {'class': 'record-text'})
			caption = caption.text
			my_data['Caption'] = caption
			# print(caption)

			#get 'Photographer' field and assign it to dictionary 
			photographer = field.find('a', attrs = {'class': 'record-text'})
			photographer = photographer.text
			my_data['Photographer'] = photographer
			# print(photographer)

			#get 'Created' field and assign it to dictionary
			#use regex to remove unwanted text 
			date = field.find('div', attrs = {'id': 'record-created'})
			date = date.text
			date_short = re.sub(r'Created',"", date)
			my_data['Created'] = date_short
			# print(date_short)

			#get 'Location' field and assign it to dictionary
			#use regex to remove unwanted text 
			location = field.find('div', attrs = {'id': 'record-notes'})
			location = location.text
			location_short = re.sub(r'Location',"", location)
			my_data['Location'] = location_short
			# print(location_short)

		# # Commented out bc Photogrammar does not use full LOC call number
		# 	call_number = field.find('div', attrs = {'id': 'record-digitalid'})
		# 	call_number = call_number.text
		# 	call_number_short = re.sub(r'Call Number', "", call_number)
		# 	call_number_shorter = re.sub(r' \(Library of Congress\)', "", call_number_short)
		# 	my_data['Call Number (Library of Congress)'] = call_number_shorter
		# 	print(call_number_shorter)

		all_photo_urls = item_soup.find_all("div", attrs={'id': 'record-image'})

		for photo_url in all_photo_urls:
			photo = photo_url.find('a')
			photo_abs_url = "http://photogrammar.yale.edu/" + photo['href']
			my_data['Image URL'] = photo_abs_url
			# print(photo_abs_url)

		all_loc_links = item_soup.find_all("div", attrs={'id': 'record-digitalid'})

		for loc_link in all_loc_links:
			link = loc_link.find('a')
			loc_abs_url = link['href']
			my_data['LOC URL'] = loc_abs_url
			# print(loc_abs_url)
			
		#get call number from LOC website
		loc_item_request = requests.get(loc_abs_url)
		loc_item_html = loc_item_request.text
		item_soup = BeautifulSoup(loc_item_html, "html.parser")

		all_bib = item_soup.find_all("div", attrs={'id':'onsite'})
		# print(all_bib)

		for loc_call_number in all_bib:
			loc = loc_call_number.find('span')
			loc = loc.text
			loc = loc.split(' [')[0]
			my_data['LOC Call Number'] = loc
			# print(loc)
			

		all_my_data.append(my_data)

# print(all_my_data)

with open('FSA_Photo_Collection.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print('Your file is now ready')

			


	
	







	

	

	
	





