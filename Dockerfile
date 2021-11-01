FROM python:3-slim-buster

EXPOSE 8080/TCP

# Keep Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=0

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]