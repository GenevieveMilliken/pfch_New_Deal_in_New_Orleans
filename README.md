This collection of Python scripts scrape two websites: Yale's Photogrammar site and the New Orleans Public Library WPA Photography Collection

(1) Yale's Photogrammar 

Running FSA_Photo_1_JSON_Write.py creates a JSON file that includes metadata information as well as image URLs.

Running FSA_Photo_2_Download.py reads the image URLs from the JSON file created by the first script and downloads them to a local folder named FSA_Images. You will need to create this folder in your local directory before download. 

(2) New Orleans Public Library's WPA Collection 

 Running WPA_COLLECTION NAME_1_JSON_Write.py creates a JSON file that includes metadata information as well as image URLs. 

 Running WPA_COLLECTION_NAME_2_Download.py reads the image URLs from the JSON file created by the first script and downloads them to a local folder named WPA_COLLECTION NAME_Images. You will need to create a folder with the collection name (i.e. WPA_Lib_Images, WPA_Rec_Images) in your local directory before download. Please be advised that the folder name must match the file path in the second script.

 Scripts are available for the following WPA collections:
 
 - Education
 - Drainage
 - Recreation
 - Lakefront
 - Library
 - Music
 - Public Health
