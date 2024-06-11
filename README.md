# PropelTechnicalInterview

### System Progression

#### 1 - Initial Build

Using Python.
Need to be able to list, view, add, edit and delete records

#### 2 - Integrating the API

### Rough Notes

API is a way for two different systems to communicate with each other. It is a set of rules that allows one piece of software application to talk to another.

Most APIs use standard HTTP methods to make requests and responses
**_GET_** - Retrieve data from a server
**_POST_** - Send data to a server
**_PUT_** - Update data on a server
**_DELETE_** - Remove data from a server

### Virutal Environment and Running

1. Create a virtual environment
2. pip install -requirements.txt in this directory
3. To run the application, run the command **python app.py**

### Folder Structure

```
PropelTechnicalInterview
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── init.py
│   ├── api/
│   │   ├── views.py
│   ├── tests/
│   │   └── test_app.py
│   ├── config.py
│   └── utils.py
├── migrations/
├── address_book.json
├── .gitignore
└── app.py
```

## Testing

For testing I used Postman Agent to test the API locally and see if it works as intended
For the complexity of this task, I decided to manually test the response section in Postman to verify the correct return status is being returned.
