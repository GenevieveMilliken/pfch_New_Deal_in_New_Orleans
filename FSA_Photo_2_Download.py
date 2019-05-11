import json
import urllib.request

# function to download images and write to file
def download_image(url, file_path, name):
	full_path = file_path + name + '.jpg'
	try:
		urllib.request.urlretrieve(url, full_path)
	except urllib.error.HTTPError:
		pass

# open json file, extract information, write images to file
with open('FSA_Photo_Collection.json') as f_object:
	text = json.load(f_object)
	for data_dict in text:
		call_number = data_dict['LOC Call Number']
		photographer = data_dict['Photographer']
		url = data_dict['Image URL']
		name = photographer + "_" + call_number
		download_image(url, "FSA_Images/", name)
		