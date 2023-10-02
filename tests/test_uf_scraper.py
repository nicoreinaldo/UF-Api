from fastapi import HTTPException
import pytest
from app.scraper.uf_scaper import scrape_uf_value, scrape_uf_value_specific_date
from datetime import datetime
from bs4 import BeautifulSoup

# Mocking to perform a test with simulated objects and make assertions about how they have been used.
@pytest.fixture
def mock_response():
    class MockResponse:
        status_code = 200
        text = "<html>Mock HTML</html>"

    return MockResponse()

# Test the scrape_uf_value function with a successful HTTP response (200)
def test_scrape_uf_value(mock_response, monkeypatch):
    def mock_requests_get(url):
        return mock_response

    monkeypatch.setattr("requests.get", mock_requests_get)
    date = datetime(2023, 1, 15) 

    # I use the real html of the page, to have a more accurate test
    with open("tests/mock_page_sii.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    uf_value = scrape_uf_value_specific_date(date, soup)
    assert uf_value.text.strip() == "35.232,98"

# Test scrape_uf_value function in case of unsuccessful HTTP response (400 Bad Request)
def test_scrape_uf_value_http_exception(mock_response, monkeypatch):
    def mock_requests_get(url):
        mock_response.status_code = 400
        return mock_response

    monkeypatch.setattr("requests.get", mock_requests_get)

    date = datetime(2023, 1, 15)  

    with pytest.raises(HTTPException):
        scrape_uf_value(date)


