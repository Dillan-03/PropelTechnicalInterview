# PropelTechnicalInterview
### System Progression
#### 1 - Initial Build
Using Python.
Making sure the user can first list, amend and search all records
#### 2 - Integrating the API
### Rough Notes

API is a way for two different systems to communicate with each other. It is a set of rules that allows one piece of software application to talk to another.

Most APIs use standard HTTP methods to make requests and responses
**_GET_** - Retrieve data from a server
**_POST_** - Send data to a server
**_PUT_** - Update data on a server
**_DELETE_** - Remove data from a server

### Virutal Environment

1. Create a virtual environment
2. pip install -requirements.txt

### Folder Structure

```
PropelTechnicalInterview
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   └── models.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_app.py
│   ├── config.py
│   ├── address_book.json
│   └── utils.py
├── migrations/
└── run.py
```
