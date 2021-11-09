FROM --platform=linux/amd64 python:3

EXPOSE 8080

# Keep Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=0

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    build-essential

COPY . /app
WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#ENTRYPOINT ["python3"]
CMD ["python3", "app.py"]
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]