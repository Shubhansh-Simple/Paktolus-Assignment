# Paktolus Take Home Assignment
It's an assignment task from paktolus

# Getting Started

### Installation Guide
* Clone the repo.
* Navigate to project directory
* Install pipenv if not installed already
* Run `pipenv shell`, it's activates Pipenv virtual environment
* `pip install -r requirements.txt`
* `python manange.py runserver`
* Open your favourite browser and run `http://localhost:8000/`

## System Requirements

- Python >= 3.10.12
- Django == 4.2.0 (LTS version)

## Running the Application
### 1. Start redis server ( install in your system if not already )
```
 redis-server --port 6739
```
### 2. Run Django development server
```
 python manage.py runserver
```
### 3. Start Celery worker (in a new terminal)
```
  celery -A Core worker --loglevel=INFO
```

### API Endpoints
<b>NOTE</b> : Requests must include <i><b>strict forward slashes</b></i> at the end for proper routing
| HTTP Verbs | Authentication | Endpoints | Action |
| --- | --- | --- | --- |
| GET |  NO |/events/  | To retrieve all events |
| POST | NO |/events/  | To create a new event |
| GET |  NO |/events/:pk/  | To retrieve details of a single event |


## Overview
This document provides detailed documentation for the Paktolus-Assignment REST API. It includes information on how to interact with the API, available endpoints, request/response format and examples.

#  Creating a new event view
<p align="center">
  <a href="https://shub.pythonanywhere.com/profile">
    <img alt="Celery-Success" 
         src="https://raw.githubusercontent.com/Shubhansh-Simple/Paktolus-Assignment/refs/heads/main/Screenshots/Celery-Execution-Success.png"
         height="500" width="900" /> 
  </a>
</p>

<hr>

## Base URL

The base URL for all API endpoints is:

```
https://localhost:8000/events/
```

## Available Endpoints

### Endpoint 1

- **URL**: `/events/`
- **Method**: `POST`
- **Description**: Create a new event
- **Parameters**: N/A

- **Example Request**:
  ```http
  POST /events HTTP/1.1
  Host: http://localhost:8000/events/
  Content-Type: application/json
  ```
  ```json
  {
    "event_type" : "testing celery",
    "source"     : "apis"
  }
  
  ```
- **Example Response**:
  ```json
   {
      "id": 26,
      "detail": "Event 'testing celery' created successfully"
   }
  ```


### Endpoint 2

- **URL**: `/events/`
- **Method**: `GET`
- **Description**: List all events
- **Parameters**: N/A

- **Example Request**:
  ```http
  GET /events HTTP/1.1
  Host: http://localhost:8000/events/
  Content-Type: application/json
  ```

- **Example Response**:
  ```json
   [
    {
        "id": 1,
        "event_type": "Login",
        "source": "mobile",
        "timestamp": "2025-05-08T14:49:50.329578+05:30"
    },
    {
        "id": 26,
        "event_type": "testing celery",
        "source": "apis",
        "timestamp": "2025-05-09T09:52:54.892060+05:30"
    }
   ]
  ```

## Error Handling

The API returns standard HTTP status codes for errors. Error responses will include a JSON object with details about the error.

Example error response:

```json
{
  "event_type" : [
    “This field is required“
  ],
   "source" : [
    “Ensure this field has no more than 20 characters.“
  ],
  "detail" : “X-Request-ID header is required“
}
```
<hr>

## Conclusion

This concludes the documentation for the Paktolus-Assignment REST API.

