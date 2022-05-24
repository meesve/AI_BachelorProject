import google_streetview.api
import google_streetview.helpers
import csv
import os 
        
def get_request_gsv(locations, name):
        #Parameters
        param = {
        'size': '640x640', # max 640x640 pixels
        'location': locations,
        'fov': '50', # field of view 
        'radius': '5', # radius in meters for image around the location
        'pitch': '12', # ptich of the camera 0 = ground level
        'source': 'outdoor', # source of the SV image 'default' = indoor and outdoor SV images
        'key': 'YOUR_OWN_API_KEY' # API key used to get images from GSV
        }

        api_list = google_streetview.helpers.api_list(param)

        results = google_streetview.api.results(api_list)
        
        #Downloading images to a new folder with metadeta
        results.download_links('class_{}'.format(name))

#Opening the .csv files with the locations
for file in os.listdir("TO/YOUR/LOCATIONS/DIR"):
        with open("YOUR/LOCATION/" + file, 'r') as f:
                next(f) # skip header line
                locs = ';'.join(f) # join the locations with ; string format
                get_request_gsv(locs, file) 