import pytest
from app.utils.date_validator import DateValidator
from fastapi import HTTPException

def test_is_valid_date_valid_format():
    date_str = "15-01-2023"  
    date_obj = DateValidator.is_valid_date(date_str)
    assert date_obj.year == 2023  

def test_is_valid_date_invalid_format():
    date_str = "2023-01-15" 
    with pytest.raises(HTTPException):
        DateValidator.is_valid_date(date_str)

def test_is_valid_date_min_date():
    date_str = "01-01-2012"  
    with pytest.raises(HTTPException):
        DateValidator.is_valid_date(date_str)



