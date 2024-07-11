
FROM python:3.9
RUN apt-get update -y && apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]