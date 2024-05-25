FROM python:3.12

WORKDIR /app-lecturer-service

COPY Pipfile Pipfile.lock requirements.txt ./

RUN pip install pipenv

# RUN pipenv install --deploy --ignore-pipfile

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
