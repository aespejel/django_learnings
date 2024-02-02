FROM python:3.13.0a3-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY admin/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./admin /app

CMD python manage.py runserver 0.0.0.0:8000
