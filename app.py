 
from flask import Flask, render_template, redirect, url_for, flash, request,Blueprint
import json
from forms import UserForm
import os
import secrets 




app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


#get file path from folder 
FILE_PATH = 'address_book.json'

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


# # ----------------- API Routes -----------------

# POST /records
# Add a new record
# Returns the newly added record
@app.route('/add', methods=['GET','POST'])
def add_record():
    #get the new record from the request
    #request.json is a dictionary that contains the JSON data 
    #append the new record to the data
    #write the data back to the file

    form = UserForm(request.form)

    if request.method == 'POST' :
     #   print("Form Data Received:", request.form)

        records = read_data(FILE_PATH)
        new_user = {
            "first_name": form.firstname.data,
            "last_name": form.lastname.data,
            "phone": form.phone.data,
            "email": form.email.data
        }
        records.append(new_user)
        write_data(FILE_PATH, records)
        flash('Record added successfully', 'success')
        return redirect(('/'))
    
    return render_template('add.html',form=form)

# # GET from the old form
# # POST to the new form if the old form exists in the json file 
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    records = read_data(FILE_PATH)
    #print(records)

     # Check if the ID is within the valid range
    if id < 0 or id >= len(records):
        flash('Record not found!', 'error')
        return render_template('404.html'), 404
    else:
        form = UserForm()
        record = records[int(id)]

        form.firstname.data = record['first_name']
        form.lastname.data = record['last_name']
        form.phone.data = record['phone']
        form.email.data = record['email']
        if request.method == 'POST' and form.validate_on_submit():
            records.pop(id)
            print(form.firstname.data)
            new_user = {
            "first_name": form.firstname.data,
            "last_name": form.lastname.data,
            "phone": form.phone.data,
            "email": form.email.data
            }
            records.append(new_user)
            write_data(FILE_PATH, records)
            
            flash('Record updated successfully', 'success')
            return redirect(url_for('index'))
    return render_template('edit.html', form=form)

# DELETE /records/<record_id>
# Delete a record by ID
# Returns the deleted record
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_record(id):
    #read the data
    #check if the record_id is valid
    #if it valid delete the record via pop 
    #write the data back to the file
    records = read_data(FILE_PATH)

     # Check if the ID is within the valid range
    if id < 0 or id >= len(records):
        flash('Record not found!', 'error')
        return render_template('404.html'), 404
    else:
        form = UserForm()
        record = records[int(id)]

        form.firstname.data = record['first_name']
        form.lastname.data = record['last_name']
        form.phone.data = record['phone']
        form.email.data = record['email']
        if request.method == 'POST' and form.validate_on_submit():
            records.pop(id)
        
            write_data(FILE_PATH, records)
            
            flash('Record updated successfully', 'success')
            return redirect(url_for('index'))
    return render_template('delete.html', form=form)

#Displaying all of the records as a table
@app.route('/list')
def list_records():
    records = read_data(FILE_PATH)
    print(records)
    return render_template('list.html', records=records)

# Search method to search for any matching records and displaying there after the refresh of the page 
@app.route('/search', methods=['GET', 'POST'])
def search():
    records = read_data(FILE_PATH)
    search_query = request.form.get('search', '')

    if search_query:
        search_query = search_query.lower()
        records = [records for records in records 
        if search_query in records['first_name'].lower() or
        search_query in records['last_name'].lower() or
        search_query in records['phone'] or
        search_query in records['email'].lower()]
    
    return render_template('search.html', records=records, search_query=search_query)

@app.route('/error', methods=['GET'])
def error():
    return render_template('404.html')



@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


