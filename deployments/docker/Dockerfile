## base image should be python3
FROM python:3
## we should copy all files to the image
COPY . /app
## Dfault forder for the image will be /app
WORKDIR /app
## Expose 5000 port for the app
EXPOSE 5000
## Installing all the liberies
RUN pip install -r requirements.txt
## Make sure when contaienr started and application will be started as well
CMD [ "/bin/sh", "-c", "python /app/app.py" ]