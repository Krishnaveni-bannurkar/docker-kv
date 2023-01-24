FROM python:latest
COPY app.py /
RUN mkdir /templates
COPY /templates/hello.html /templates/
RUN pip install --upgrade pip
RUN pip install Flask
ENTRYPOINT  [ "python", "./app.py" ]
EXPOSE 4043
