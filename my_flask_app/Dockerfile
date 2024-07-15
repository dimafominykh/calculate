
FROM python:3.9
RUN apt-get update -y && apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && \
      apt-get -y install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker
CMD ["python3", "app.py"]
