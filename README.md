# UF API

UF API is a Python web application built using FastAPI to retrieve the Unidad de Fomento (UF) value for a specific date. 

## Technologies and Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern web framework for building APIs with Python.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): A library for web scraping HTML and XML documents.
- [Pydantic](https://pydantic-docs.helpmanual.io/): A data validation and parsing library used for defining API request and response models.
- [pytest](https://docs.pytest.org/en/latest/): A testing framework for Python.
- [requests](https://docs.python-requests.org/en/latest/): A library for making HTTP requests.
- [locale](https://docs.python.org/3/library/locale.html): A module for internationalization and localization.

## Prerequisites

- [docker](https://www.docker.com/): A containerization platform for building, packaging, and distributing applications.

## Installation

1. Clone this repository to your local machine: `git clone git@github.com:nicoreinaldo/UF-Api.git`
2. Navigate to the project directory: `cd UF-Api`

## Run

1. `docker-compose up --build`
2. Open your web browser and access the following URL to interact with the application: http://localhost:8000

## API Documentation

You can access the API documentation by navigating to the following URL in your web browser:

http://localhost:8000/docs

This documentation provides detailed information on how to use the API, including available endpoints, request parameters, and response formats. It's a helpful resource for understanding how to interact with the application programmatically.

To access the API documentation, make sure that the application is running locally using Docker Compose as described in the previous section, and then open the provided URL in your web browser.

Example curl : curl --location 'http://localhost:8000/api/v1/uf/30-05-2023'

<img width="1511" alt="documentation-api" src="https://github.com/nicoreinaldo/UF-Api/assets/22691843/434730bf-41ed-44c6-bcaf-291bcc5a46d9">


## Test

Run the following command to start the tests:
`pytest`

<img width="1640" alt="test" src="https://github.com/nicoreinaldo/UF-Api/assets/22691843/e2884e6b-a3a1-4bf2-8c63-b5d58a885f5e">


## Stop Aplication

For stop the application and remove the containers, you can press Ctrl+C in the terminal where Docker Compose is running or run the following command:
`docker-compose down`



