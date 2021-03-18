FROM python:3
ENV PYTHONNUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . /code/
