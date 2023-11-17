FROM python:3.10.0a7-alpine3.13
RUN apk update && apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]
