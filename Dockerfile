FROM python:3.12.6-alpine

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY=temporary_key_for_collectstatic
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]