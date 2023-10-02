FROM python:3.11.5
RUN apt-get update && apt-get install -y locales && \
    echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen
WORKDIR /app
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
