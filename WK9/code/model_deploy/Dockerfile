FROM python:3.10.0a7-alpine3.13
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]
