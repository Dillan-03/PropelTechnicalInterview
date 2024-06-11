#File which performs file mandontary operations like read and writing to the file 

import json
import os

def read_data(file_path):
    #if file exsits
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            # returns a python object that can be used
            return json.load(f)
    else:
        return []

def write_data(file_path, data):
    with open(file_path, 'w') as f:
        #Converts the python object to a json string that can be written to a file
        json.dump(data, f)
