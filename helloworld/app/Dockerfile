FROM python:3.8-slim-buster

WORKDIR /usr/src/app

ENV FLASK_APP="src/app.py"

RUN pip install --upgrade pip

COPY src/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080" ]