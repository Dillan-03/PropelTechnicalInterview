from flask import Blueprint, request, jsonify
from app.utils import read_data, write_data

#using blueprint to define api routes
api_blueprint = Blueprint('api', __name__)
#get file path from folder 
FILE_PATH = 'app/address_book.json'

# ----------------- API Routes -----------------

# GET /records
# List all records
# Returns a list of records
@api_blueprint.route('/records', methods=['GET'])
def list_records():
    data = read_data(FILE_PATH)
    #returns the data is a json format with 200 (ok) server code
    return jsonify(data), 200

# POST /records
# Add a new record
# Returns the newly added record
@api_blueprint.route('/records', methods=['POST'])
def add_record():
    #get the new record from the request
    #request.json is a dictionary that contains the JSON data 
    #append the new record to the data
    #write the data back to the file
    new_record = request.json
    data = read_data(FILE_PATH)
    data.append(new_record)
    write_data(FILE_PATH, data)

    #return created status code 201 
    return jsonify(new_record), 201

# GET /records/<record_id>
# Get a record by ID
# Returns the record with the given ID
@api_blueprint.route('/records/<int:record_id>', methods=['PUT'])
def edit_record(record_id):
    #get the updated record from the request
    #read the data
    #check if the record_id is valid
    #if it valid update the record 
    updated_record = request.json
    data = read_data(FILE_PATH)
    if 0 <= record_id < len(data):
        data[record_id] = updated_record
        write_data(FILE_PATH, data)
        #return ok server code
        return jsonify(updated_record), 200
    else:
        #error message with 404 server code
        return jsonify({'error': 'Record not found'}), 404

# DELETE /records/<record_id>
# Delete a record by ID
# Returns the deleted record
@api_blueprint.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    #read the data
    #check if the record_id is valid
    #if it valid delete the record via pop 
    #write the data back to the file
    data = read_data(FILE_PATH)
    if 0 <= record_id < len(data):
        deleted_record = data.pop(record_id)
        write_data(FILE_PATH, data)
        #return ok server code
        return jsonify(deleted_record), 200
    else:
        return jsonify({'error': 'Record not found'}), 404

# GET /records/search
# Search records by query
# Returns a list of records that match the query
'''
for example URL: http://127.0.0.1:5000/records/search?first_name=David&last_name=Platt
will return all records with first_name as David and last_name as Platt
'''
@api_blueprint.route('/records/search', methods=['GET'])
def search_records():
    #get the user serach request via args
    #args can contain several records for a search. which is stored as a dictionary
    query = request.args
    data = read_data(FILE_PATH)
    results = [] #store the matching records
    #loop through the data and find matchign records
    for records in data:
        for k,v in query.items():
            if records.get(k) == v:
                results.append(records)
            else:
                break
    return jsonify(results), 200
