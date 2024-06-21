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

### Virutal Environment and Running

1. Create a virtual environment
2. pip install -r requirements.txt in this directory
3. To run the application, run the command **python app.py**

### Folder Structure

```
PropelTechnicalInterview
├── README.md
├── requirements.txt
├── static/
│   └── styles.css
│   └── table.css
├── templates/
│   └── 404.html
│   └── add.html
│   └── edit.html
│   └── delete.html
│   └── home.html
│   └── list.html
│   └── search.html
├── tests/
│   └── test_app.py
├── address_book.json
├── .gitignore
└── app.py
└── forms.py

```

## Testing

For testing I used unit testing to test the API through different test case scenarios. The tests are located in the tests folder and can be run by running the command **python -m unittest discover -s tests**
