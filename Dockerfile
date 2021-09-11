FROM python:3.8.10

WORKDIR /app

COPY ./la1.py .

CMD ["python", "la1.py"]
