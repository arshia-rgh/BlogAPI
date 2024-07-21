# Blog API Project
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-009688?logo=django&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2B2B2B?logo=python&logoColor=white)

# important !
### API Implementation Variations

In this project, I utilize various Django and Django REST Framework views to cater to different API needs. This approach allows us to leverage the strengths of each view type across our CRUD operations. Below is an overview of the view types used:

### Django Views
- **Function-Based Views (FBVs):** Traditional Django views using functions to handle requests. Ideal for simple operations and custom behavior.

### Django REST Framework Views
- **Function-Based Views (FBVs):** Utilize Django REST Framework's `@api_view` decorator to create API views. These are used for straightforward API endpoints.
- **Class-Based Views (CBVs):** Offer more structure and reusability by handling API requests with classes. Suitable for more complex logic.
- **ViewSets:** Abstract away the need to create separate views for different CRUD operations. They provide a more concise way to organize API logic.

Each type of view is selected based on the specific requirements of the API endpoint, ensuring optimal performance and maintainability.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Accessing the API](#accessing-the-api)
  - [Endpoints](#endpoints)
  - [Using Python `requests` to Interact with the API](#using-python-requests-to-interact-with-the-api)
## Overview
This Blog API project is designed as a backend service using Django and Django REST Framework, providing a robust platform for blog operations such as creating, reading, updating, and deleting blog posts. Additionally, it includes examples of using Python `requests` library to interact with the API, serving as a client for testing and interaction purposes.

## Features
- CRUD operations for blog posts.
- User authentication and authorization.
- Pagination and filtering.
- Customizable blog post categories.
- Comment system for each blog post.

## Technologies
- **Backend**: Django, Django REST Framework
- **Client**: Python `requests` library

## Getting Started

### Prerequisites
- Python 3.12
- pip
- Virtualenv (optional)

### Installation
1. Clone the repository
2. Navigate to the project directory:

```cd BlogAPI ```

3. Create a virtual environment (optional):

``` python3 -m venv .venv```

```source .venv/bin/activate ```

4. Install the requirements:

``` pip install -r requirements.txt``` 

5. Navigate to backend section of project:

``` cd backend ```

6. Migrate the database:

``` python3 manage.py migrate ```

7. Run the server:

``` python manage.py runserver ```

## Usage

### Accessing the API
You can access the API through the following endpoint: `http://localhost:8000/api/`

### Endpoints

#### ---Will be updated soon---

[//]: # (- `/api/posts/` - GET, POST: Retrieve all posts or create a new post.)

[//]: # (- `/api/posts/<id>/` - GET, PUT, DELETE: Retrieve, update, or delete a specific post.)

[//]: # (- `/api/comments/` - GET, POST: Retrieve all comments or create a new comment.)

[//]: # (- `/api/comments/<id>/` - GET, PUT, DELETE: Retrieve, update, or delete a specific comment.)

### Using Python `requests` to Interact with the API

1. Navigate to the client section of project:

``` cd client``` 

2. Run the main python script:

``` python3 main.py``` 