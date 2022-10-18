FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY . /app
RUN pip install -r requirements.txt
