from datetime import datetime
from fastapi import HTTPException

class DateValidator:

    @staticmethod
    def is_valid_date(date_str, date_format='%d-%m-%Y') -> str:
        """ Checks if the date entered is valid """
        try:
            date_obj = datetime.strptime(date_str, date_format)
            # Business rule: minimum date 01-01-2013
            min_date = datetime(2013, 1, 1)
            
            if date_obj < min_date:
                raise HTTPException(status_code=400, detail="The minimum date that can be consulted is: 01-01-2013")
                
            return date_obj
        except ValueError:
            raise HTTPException(status_code=400, detail="Date format incorrect, should be: DD-MM-YYYY")
