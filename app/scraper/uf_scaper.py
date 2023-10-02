import requests
import locale
from bs4 import BeautifulSoup
from fastapi import HTTPException

# Configure to then get the name of the month in Spanish
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

BASE_URL_UF = "https://www.sii.cl/valores_y_fechas/uf/uf"

def scrape_uf_value(date):
    """ Obtains the value of the Unidad de Fomento (UF) for a specific date.
         Args:
             date (datetime.date): The date for which the UF value is searched.
         Returns:
             The value of the UF as a BeautifulSoup tag or None if not found.
     """
    url = f"{BASE_URL_UF}{date.year}.htm"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="The SII page could not be accessed")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    uf_value = None

    uf_value = scrape_uf_value_specific_date(date, soup)

    return uf_value


def scrape_uf_value_specific_date(date, soup):
    """ Get the value of the Unidad de Fomento (UF) for a specific date in the parsed HTML.
         Clarifications: At first I designed the algorithm with two fors, that is: O(nº2),
             Therefore, look for this best option to reduce complexity and increase performance.
     """
    try:
        # Gets the name of the month in Spanish
        month_name = "mes_" + date.strftime('%B')

        # Get the data for the month
        data_month = soup.find('div', id=month_name).find('table')

        find_day = data_month.find('th', string=str(date.day))
        if find_day:
            # Find the value in the following line td and return its value in json format
            uf_value = find_day.find_next_sibling('td')
            return uf_value
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error trying to obtain the units of Fomento : {e}")
