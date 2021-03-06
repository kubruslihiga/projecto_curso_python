FROM python:3.7.3-alpine3.9

WORKDIR /root
COPY requirements.txt /root
RUN pip install -r requirements.txt

COPY manage.py ./
ADD /website ./website
ADD /static ./static
ADD /blog ./blog
ADD /projects ./projects

RUN python manage.py makemigrations blog
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN export DJANGO_PRODUCTION=true

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]