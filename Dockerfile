FROM python 3.8
LABEL MAINTAINER="Bahman Pournazari | bahmanpn@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
ADD . /blogpy
ADD requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn","--chdir","blogpy","--bind",":8000","blogpy.wsgi:application"]