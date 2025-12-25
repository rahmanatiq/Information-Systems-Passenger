## Passenger Information System

A simple Passenger Information System built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend.
The system allows users to add, view, edit, and delete passenger information.
All data is stored in a lightweight JSON file, making it easy to run without a database.

## Features

✓ Add New Passengers

1. Enter details such as:

2. Full Name

3. Age

4. Destination

5. Ticket Number

✓ View All Passengers

All passengers are displayed in a clean, responsive table.

✓ Edit Passenger Details

Update any existing passenger’s information.

✓ Delete Passengers

Remove a passenger entry instantly.

✓ JSON-Based Data Storage

No SQL database required — data is stored in data.json.

✓ Responsive UI

Fully responsive design for desktop and mobile devices.

## Technologies Used

Frontend

1. HTML5

2. CSS3 (Responsive styling)

3. JavaScript (Fetch API)

Backend

1. Python 3

2. Flask

3. Flask-CORS

Storage

1. JSON file (data.json)

## How to Run the Project
1. Install Dependencies
   pip install flask flask-cors

2. Start the Server
   python server.py

3. Open in Browser
  http://127.0.0.1:5000
  
## API Endpoints
1. Get All Passengers
    GET /passengers

2. Add Passenger

POST /passengers

Example Request Body:
{
  "name": "John Doe",
  "age": 25,
  "destination": "London",
  "ticket": "T1234"
}

3. Update Passenger

PUT /passengers/<id>

4. Delete Passenger

DELETE /passengers/<id>

## Project Structure
Passenger_system/
│── server.py
│── data.json
│── README.md
│
├── templates/
│    └── index.html
│
└── static/
     ├── style.css
     └── script.js


## References & Inspirations

The project was built using concepts and guidance from:

1. Flask Documentation

2. MDN Web Docs (JavaScript & HTML)

3. W3Schools (CSS styling ideas)https://www.w3schools.com/css/css_icons.asp

4. Json    https://www.w3schools.com/python/python_json.asp

All code is written manually by the student.
