import pandas as pd
import csv

# col_list = ["postcode", "openbareruimtenaam", "huisnummer", "classification", "buildingtype", "buildingtype_eib_ezk"]
# reading csv data
df = pd.read_csv("DATABASE_OF_LOCATIONS.csv", encoding="latin-1")
    
def get_location_data(n_classes):
    n_classes += 1
    for i in range(1,n_classes):
        # requesting 'postcode', 'openbareruimtenaam', 'huisnummer' for input get_request
        loc_data = df.loc[(df["classification"] == i), ["postcode", "openbareruimtenaam", "huisnummer"]]
        # writing streetnames to their class folder in .csv
        loc_data.to_csv("locations_" + str(i) + ".csv", index=False)

get_location_data(12)




            

