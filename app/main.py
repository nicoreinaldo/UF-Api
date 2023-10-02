from fastapi import FastAPI
from app.scraper.uf_scaper import scrape_uf_value
from app.utils.date_validator import DateValidator
from app.model.UfResponse import UfResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a UF API"}


@app.get("/api/v1/uf/{date}", response_model=UfResponse)
def get_uf_current_date(date: str):
    date_obj = DateValidator.is_valid_date(date)    
    
    response = scrape_uf_value(date_obj)
    # Return the model as JSON
    return UfResponse(date=date, uf_value=response.text.strip())