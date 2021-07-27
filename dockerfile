#Create a ubuntu base image with python 3 installed.
FROM python:3.9.1-slim-buster

#Set the working directory
WORKDIR /usr/src/app

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 8000

#Run the command
CMD [“python3”, “./main.py”]