import json
import urllib.request

# function for downloading images to a file
def download_image(url, file_path, name):
	try:
		full_path = file_path + name + '.jpg'
		urllib.request.urlretrieve(url, full_path)
	except urllib.error.HTTPError:
		pass

unique_name = ''

with open('WPA_Lakefront_Collection.json') as f_object:
	text = json.load(f_object)
	for i in range(1,77):
		s_number = (text[i]['series_number'])
		for url in text[i]['digital_photos']:
			photo_url = url
			unique_number = photo_url[-6:-4]
			unique_name = s_number + "_" + str(unique_number)
			download_image(photo_url, 'WPA_Lakefront_Images/', unique_name)
