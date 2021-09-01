FROM python:3.7

ADD ./src /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 3000
CMD ["python", "app.py"]
