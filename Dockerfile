FROM python:3.11-slim

WORKDIR /sge

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000