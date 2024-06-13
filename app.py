 
from flask import Flask, render_template, redirect, url_for, flash, request,Blueprint
import json
from forms import UserForm
import os
import secrets 




app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


#get file path from folder 
app.config['FILE_PATH'] = 'address_book.json'
def read_data():
    #if file exsits
    file_path = app.config['FILE_PATH']
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            # returns a python object that can be used
            return json.load(f)
    else:
        return []

def write_data(records):
    file_path = app.config['FILE_PATH']
     #Converts the python object to a json string that can be written to a file
    with open(file_path, 'w') as f:
        json.dump(records, f)

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

        records = read_data()
        new_user = {
            "first_name": form.firstname.data,
            "last_name": form.lastname.data,
            "phone": form.phone.data,
            "email": form.email.data
        }
        #Search for any existing records. If the record already exists, don't add it
        for record in records:
            if record['first_name'] == new_user['first_name'] and record['last_name'] == new_user['last_name'] and record['phone'] == new_user['phone'] and record['email'] == new_user['email']:
                flash('Record already exists!')
                return redirect(('/add'))

        records.append(new_user)
        write_data(records)
        flash('Record added successfully')
        return redirect(('/add'))
    
    return render_template('add.html',form=form)

# # GET from the old form
# # POST to the new form if the old form exists in the json file 
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    records = read_data()

    form = UserForm()
     # Check if the ID is within the valid range
    if id < 0 or id >= len(records):
        flash('Record not found!')
        return render_template('404.html'), 404
    else:
        if request.method == 'GET':
        

            # Check if ID is valid
            if id < 0 or id >= len(records):
                flash('Record not found!')
                return render_template('404.html'), 404

            # Extract record data for editing
            record = records[int(id)]
            form = UserForm(firstname=record['first_name'],
                            lastname=record['last_name'],
                            phone=record['phone'],
                            email=record['email'])
            return render_template('edit.html', form=form)

        elif  request.method == 'POST':

            if form.validate_on_submit():
                records[id] = {
                    "first_name": form.firstname.data,
                    "last_name": form.lastname.data,
                    "phone": form.phone.data,
                    "email": form.email.data
                }
                write_data(records)
                flash('Record updated successfully')

    
            
                # return redirect(url_for(''))
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
    records = read_data()

     # Check if the ID is within the valid range
    if id < 0 or id >= len(records):
        flash('Record not found!')
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
        
            write_data(records)
            
            flash('Record updated successfully')
            return redirect(url_for('index'))
    return render_template('delete.html', form=form)

#Displaying all of the records as a table
@app.route('/list')
def list_records():
    records = read_data()
    # print(records)
    return render_template('list.html', records=records)

# Search method to search for any matching records and displaying there after the refresh of the page 
@app.route('/search', methods=['GET', 'POST'])
def search():
    records = read_data()
    search_query = request.form.get('search', '')

    if search_query:
        search_query = search_query.lower()
        records = [records for records in records 
        if search_query in records['first_name'].lower() or
        search_query in records['last_name'].lower() or
        search_query in records['phone'] or
        search_query in records['email'].lower()]
    
    return render_template('search.html', records=records, search_query=search_query)

#Error page for 404
@app.route('/error', methods=['GET'])
def error():
    return render_template('404.html')

# Home Page 
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


