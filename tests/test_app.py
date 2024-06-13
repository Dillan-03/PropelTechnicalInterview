import unittest
import os
from app import app, read_data, write_data

class FlaskTestCase(unittest.TestCase):
   
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.app = app.test_client()

        # Using a test file
        self.TEST_PATH = 'tests/test_data.json'
        app.config['FILE_PATH'] = self.TEST_PATH


        # Using this to intiial create a test dictionary 
        self.initial_data = [{"first_name": "Jason", "last_name": "Grimshaw", "phone": "01913478123", "email": "jason.grimshaw@corrie.co.uk"}, {"first_name": "Dillan", "last_name": "Kerai", "phone": "123", "email": "1@gmail.com"}, {"first_name": "Ken", "last_name": "Barlow", "phone": "019134784929", "email": "ken.barlow@corrie.co.uk"}, {"first_name": "Rita", "last_name": "Sullivan", "phone": "01913478555", "email": "rita.sullivan@corrie.co.uk"}]
        write_data(self.initial_data)

    #Setup before each unittest
    def tearDown(self):
        # Cleanup data after each test
        if os.path.exists(self.TEST_PATH):
            os.remove(self.TEST_PATH)

    #Testing if a user can be added
    def test_add_user(self):
        response = self.app.post('/add', data=dict(
            firstname="John",
        lastname="Smith",
            phone="1234567",
            email="johnsmith@gmail.com"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Check if the redirection was successful
        data = response.get_data(as_text=True)
        # print(data)

        # Verify the new user is in the data file through the flash message
        self.assertIn("Record added successfully", data)
        updated_data = read_data()
        new_user = {"first_name": "John", "last_name": "Smith", "phone": "1234567", "email": "johnsmith@gmail.com"}
        self.assertIn(new_user, updated_data)
                                 

    #Testing if a user can be added if the user already exists
    def test_add_existing_user(self):
        self.test_add_user()  # Add the user first
        response = self.app.post('/add', data=dict(
            firstname="John",
            lastname="Smith",
            phone="1234567",
            email="johnsmith@gmail.com"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Check if the redirection was successful
        data = response.get_data(as_text=True)
        # print(data)

        # through the flash message
        self.assertIn("Record already exists!", data)
                                    
    def test_edit_user(self):
        #we use the first record that will be tested for edit 

        # Edit the user
        response = self.app.post('/edit/0', data=dict(
            firstname="Jason",
            lastname="Grimshaw",
            phone="1234567890",
            email="jason.grimshaw@corrie.co.uk"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn("Record updated successfully", data)

        # Verify the updated user is in the data file
        updated_data = read_data()
        edited_user = {"first_name": "Jason", "last_name": "Grimshaw", "phone": "1234567890", "email": "jason.grimshaw@corrie.co.uk"}
        self.assertIn(edited_user, updated_data)
        
    #List all the users in the address book and seeing if it is displayed
    def test_list_users(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn("Dillan", data)
        self.assertIn("Jason", data)
       

    #Search for a record in the address book
    def test_search_users(self):

        response = self.app.post('/search', data=dict(search_query="Dillan"))

        self.assertEqual(response.status_code, 200)

        #get the data text from the json from the page
        data = response.get_data(as_text=True)
        self.assertIn("Dillan", data)

   
       
    #Check to see if the user record has been deleted 
    def test_delete_user(self):
        response = self.app.post('/delete/0')
        self.assertEqual(response.status_code, 302)  # Expecting redirect after successful delete
        updated_data = read_data()

        self.assertNotIn({"first_name": "Jason", "last_name": "Grimshaw", "phone": "01913478123", "email": "jason.grimshaw@corrie.co.uk"},  updated_data)

        

   
if __name__ == '__main__':
    unittest.main()
