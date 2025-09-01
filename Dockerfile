FROM python:3.10-slim-bookworm
#From Docker hub takes a base image of linux base image

WORKDIR /app
#Create a app folder
COPY . /app
#Copy the entire project to the app folder
RUN apt-get update -y && apt install awscli -y
# Update all the packages 
RUN pip install -r requirements.txt

CMD ["python3","app.py"]
# Used to run the python file with app.py